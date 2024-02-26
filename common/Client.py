#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect

from locust import events
import json
import struct
import time
from gevent.event import Event
from common.log import logger
import xxtea
import traceback
from config import SERVER_HOST, PORT
import proto
from gevent import socket, monkey
from lib import SocketProcesser
from lib.event_handler import Handler
from google.protobuf import json_format
from config import is_old_server, is_security
from common.room import Room
from lib.CustomException import *
from common.ClientData import ClientData

PbClass = {}
for name in proto.__dict__:
    # logger.info(name)
    PbClass[name] = getattr(proto, name)


class UnpackType(object):
    RSP = 0
    REQ = 1


class ClientREQHead(object):
    def __init__(self, roomid):
        self.roomid = roomid


class ClientREQ(object):
    def __init__(self, head, body):
        self.head = head
        self.body = body


class ClientRSPHead(object):
    def __init__(self, roomid):
        self.roomid = roomid


class ClientRSP(object):
    def __init__(self, head, body, name):
        self.head = head
        self.body = body
        self.name = name


class Client(object):
    def __init__(self, uid=None, host=SERVER_HOST, port=PORT):
        if hasattr(self, 'uid'):
            return
        self.pb = {}
        self.uid = uid
        self.isStop = True
        # gevent的一个用来控制协程挂起唤醒的东西
        self.recv_event = Event()
        # 心跳包事件，心跳包必须在登录成功后再发，不然服务器会直接杀掉连接
        self.heartbeat_event = Event()
        # 正在监听的事件
        self.events = {}
        # 已经recv到的数据
        self.msgs = []
        # 正在等待recv的数据
        self.wait_msgs = []
        # 当前机器人曾经进入过的房间信息
        self.client_data = ClientData()
        self.connect(host, port)

    def set_uid(self, uid):
        self.uid = uid

    def __del__(self):
        self.isStop = True

    def get_room_obj(self, roomid):
        if roomid not in self.client_data.rooms:
            self.client_data.rooms[roomid] = Room(roomid)
            logger.info("进入if：{}".format(self.client_data.rooms[roomid]))
        return self.client_data.rooms[roomid]

    def add_event(self, event_name, event_func, *args, **kwargs):
        self.events[event_name] = Handler(event_func, *args, **kwargs)

    def stop(self):
        self.isStop = True
        if hasattr(self, 'socket'):
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except Exception:
                logger.error(traceback.format_exc())

    def connect(self, host, port):
        self.socket = socket.socket()
        start_time = time.time()
        logger.info("attempting to connect to %s on port %s" % (host, port))
        try:
            self.socket.connect((host, int(port)))
            logger.info("connected")
            self.isStop = False
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type='socket', name='connect', response_time=total_time,
                                response_length=0)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.info("connected failed")
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type='socket', name='connect', response_time=total_time, exception=e,
                                response_length=0)
            return False
        self.recvBuffer = bytes()
        SocketProcesser.add({
            'socket': self.socket,
            'data': lambda data: self.process_data(data),
            'error': self.on_socket_error,
            'client': self
        })

    def on_socket_error(self):
        if hasattr(self, 'socket'):
            delattr(self, 'socket')
        if hasattr(self, 'wait_msgs') and len(self.wait_msgs) > 0:
            self.recv_event.set()

    def send(self, param0, param1=None, roomid=0):
        start_time = time.time()
        if type(param0) == bytes:
            data = param0
        else:
            if type(param0) == str:
                if param1 is None:
                    msg = self.pb[param0]()
                else:
                    if type(param1) == dict:
                        jsonStr = json.dumps(param1)
                    else:
                        jsonStr = param1
                    msg = json_format.Parse(jsonStr, self.pb[param0](), ignore_unknown_fields=True)
                req = ClientREQ(ClientREQHead(roomid), msg)
            elif type(param0) == ClientREQ:
                req = param0
            else:
                msg = param0
                req = ClientREQ(ClientREQHead(roomid), msg)

            data = self.pack(req)
        if hasattr(self, 'socket'):
            try:
                self.socket.send(data)
                logger.debug("uid:{}|发送消息:{}".format(self.uid, param0))
                # total_time = int((time.time() - start_time) * 1000)
                # self.request_event.fire(request_type="socket", name="send", response_time=total_time,
                #                         response_length=len(data), response=None, context=None, exception=None)
            except OSError as err:
                # total_time = int((time.time() - start_time) * 1000)
                # self.request_event.fire(request_type="socket", name="send", response_time=total_time,
                #                         response_length=0, response=None, context=None, exception=e)
                self.on_socket_error()
                raise err
        else:
            raise (BaseException('socket error, uid:{}'.format(self.uid)))

    def _fill_recv(self, name=None, wait_all=True, timeout=10, timeoutCode=0):
        start_time = time.time()
        isDone = False
        msg = None
        msgs = []
        # 把需要接收的协议名字加入等待列表
        wait_msgs = []
        if type(name) == str:
            wait_msgs.append(name)
        else:
            for i in range(len(name)):
                wait_msgs.append(name[i])
                msgs.append(None)
        self.wait_msgs.extend(wait_msgs)

        while not isDone:
            now_time = time.time()
            pass_time = now_time - start_time
            left_time = timeout - pass_time

            if left_time <= 0:
                # 如果超时了，就把等待返回的信息删掉
                for msg in wait_msgs:
                    if msg in self.wait_msgs:
                        self.wait_msgs.remove(msg)
                if timeoutCode == 0:
                    total_time = int((time.time() - start_time) * 1000)
                    e = TimeOutException('time out, uid:{}'.format(self.uid))
                    events.request.fire(request_type="socket", name=name, response_time=total_time, exception=e,
                                        response_length=0)
                    raise (e)
                    # assert (pass_time < timeout), 'time out'
                else:
                    total_time = int((time.time() - start_time) * 1000)
                    e = TimeOutException('time out, uid:{}'.format(self.uid))
                    events.request.fire(request_type="socket", name=name, response_time=total_time, exception=e,
                                        response_length=0)
                    return timeoutCode
            # 先挂起,等收到消息再唤醒
            if left_time > 0.1:
                self.recv_event.wait(left_time)
            else:
                self.recv_event.wait(0.1)
            if not hasattr(self, 'socket'):
                raise (BaseException('socket error, uid:{}'.format(self.uid)))

            msgs_len = len(self.msgs)
            if msgs_len > 0:
                for index in range(0, msgs_len):
                    msg = self.msgs[index]
                    msg_name = msg.name
                    if name is None:
                        isDone = True
                        break
                    elif type(name) == str:
                        if name == msg_name:
                            msg = self.msgs.pop(index)
                            logger.debug("uid:{}|取出消息:{}|wait_msgs:{}".format(self.uid, msg_name, self.wait_msgs))
                            isDone = True
                            break
                    else:
                        if wait_all:
                            for i in range(len(name)):
                                if msgs[i] is None and name[i] == msg_name:
                                    msgs[i] = self.msgs.pop(index)
                                    logger.debug(
                                        "uid:{}|取出消息:{}|wait_msgs:{}".format(self.uid, msg_name, self.wait_msgs))
                            isDone = True
                            for i in range(len(name)):
                                if msgs[i] is None:
                                    isDone = False
                                    break
                            if isDone:
                                msg = msgs
                        else:
                            if name.count(msg_name) > 0:
                                msg = self.msgs.pop(index)
                                logger.debug(
                                    "uid:{}|取出消息:{}|wait_msgs:{}".format(self.uid, msg_name, self.wait_msgs))
                                isDone = True
                                break
        if (isinstance(name, str)):
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type="socket", name=name, response_time=total_time, response_length=0)
        return msg

    # 接受全部數據包信息
    def full_recv(self, name=None, timeout=6, timeoutCode=0):
        return self._fill_recv(name, True, timeout, timeoutCode)

    def full_recv_one(self, name=None, timeout=6, timeoutCode=0):
        return self._fill_recv(name, False, timeout, timeoutCode)

    # 接受數據包信息
    def recv(self, name=None, timeout=6, timeoutCode=0):
        msg = self.full_recv(name, timeout, timeoutCode)
        if type(msg) == int:
            return msg
        elif type(msg) == list:
            return [item for item in msg]
        else:
            return msg

    def recv_one(self, name=None, timeout=6, timeoutCode=0):
        msg = self.full_recv_one(name, timeout, timeoutCode)
        if type(msg) == int:
            return msg
        else:
            return msg

    def process_data(self, data):
        self.recvBuffer += data
        while True:
            if len(self.recvBuffer) < 4:
                break
            else:
                length = 4
                for i in range(len(self.recvBuffer)):
                    if i < 4:
                        try:
                            length += (ord(self.recvBuffer[i: i + 1]) << (24 - i * 8))
                        except Exception:
                            logger.error(traceback.format_exc())
                    else:
                        break
                if len(self.recvBuffer) < length:
                    break
                else:
                    newRecvBuffer = self.recvBuffer[0: length]
                    msg = self.unpack(newRecvBuffer)
                    if msg is not None:
                        msgName = msg.name
                        logger.debug("uid:{}|收到消息:{}|wait_msgs:{}".format(self.uid, msgName, self.wait_msgs))
                        if msgName in self.events:
                            try:
                                self.events[msgName](self, msg)
                            except Exception:
                                logger.error(traceback.format_exc())
                        if hasattr(self, 'wait_msgs') and self.wait_msgs.count(msgName) > 0:
                            self.msgs.append(msg)
                            logger.debug("uid:{}|保存消息:{}|wait_msgs:{}".format(self.uid, msgName, self.wait_msgs))
                            self.wait_msgs.remove(msgName)
                            self.recv_event.set()
                            self.recv_event.clear()
                    self.recvBuffer = self.recvBuffer[length:]

    def pack(self, req):
        # 4 报文长度 = 2 + n + 4 + l
        # 2 协议名字长度 = n
        # n 协议名
        # 4 房间ID
        # l 协议内容
        global is_security
        global xxtea_key
        if req.body is not None:
            body = req.body.SerializeToString()
            length = 2 + len(req.body.DESCRIPTOR.full_name) + 4 + len(body)
            data = struct.pack("BBBB", length >> 24, (length >> 16) & 0xff, (length >> 8) & 0xff, length & 0xff)

            length = len(req.body.DESCRIPTOR.full_name)
            data += struct.pack("BB", (length >> 8) & 0xff, length & 0xff)

            data += bytes(req.body.DESCRIPTOR.full_name, encoding="utf8")

            data += struct.pack("BBBB", req.head.roomid >> 24, (req.head.roomid >> 16) & 0xff,
                                (req.head.roomid >> 8) & 0xff, req.head.roomid & 0xff)

            data += body

            if is_security:
                while len(xxtea_key) < 16:
                    xxtea_key = xxtea_key + bytes([0])
                data = xxtea.encrypt(data, xxtea_key)
                length = len(data) + 1
                data = struct.pack("BBBBB", length >> 24, (length >> 16) & 0xff, (length >> 8) & 0xff, length & 0xff,
                                   1) + data
                # logger.info(binascii.hexlify(data))

            # logger.info('{} {}'.format(str(data), binascii.hexlify(data)))
            return data

        else:
            logger.error('req body is None')
            return bytes()

    def unpack(self, data, type=UnpackType.RSP):
        global is_security
        global xxtea_key

        if is_security:
            while len(xxtea_key) < 16:
                xxtea_key = xxtea_key + bytes([0])
            if data[4] == 1:
                data = xxtea.decrypt(data[5:], xxtea_key)
            else:
                data = data[5:]

        nameLength = (ord(data[4: 5]) << 8) + ord(data[5: 6])
        name = data[9: 6 + nameLength].decode()
        if not is_old_server:
            roomid = (
                    (ord(data[6 + nameLength: 6 + nameLength + 1]) << 24) +
                    (ord(data[6 + nameLength + 1: 6 + nameLength + 2]) << 16) +
                    (ord(data[6 + nameLength + 2: 6 + nameLength + 3]) << 8) +
                    (ord(data[6 + nameLength + 3: 6 + nameLength + 4]) << 0)
            )
            body = data[6 + nameLength + 4:]
        else:
            roomid = 0
            body = data[6 + nameLength:]

        if name in self.pb:
            body_obj = self.pb[name]()
            body_obj.ParseFromString(body)
            body_dict = json_format.MessageToDict(body_obj, including_default_value_fields=True,
                                                  preserving_proto_field_name=True)
            if type == UnpackType.REQ:
                return ClientREQ(ClientRSPHead(roomid), body_dict)
            else:
                return ClientRSP(ClientRSPHead(roomid), body_dict, name)
        else:
            logger.error(" no such pb." + name)
            return None

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
# if __name__ == '__main__':
#     from common.player import Player
#
#     player = Player()
#     client = Client(uid=2507859, host='beta12s.kkpoker.co', port='4000')
#     result = player.login_by_username("bba1", "wwwww1")
#     # result2 = Player().login_by_uid(2955)
#     # resault = Client(2955)
