# -*- coding: utf-8 -*-
import datetime
import importlib
import os
import random
import re
import socket
import struct
import sys
import time
import uuid

import gevent
import requests

import proto
from common.log import logger
from common.Client import Client
from config import G_Distributor, G_SubDistributor, EMAIL_LOGIN_TYPE, SERVER_HOST, PORT, CLIENT_VERSION
from lib.utils import md5

# 获取本机的MAC地址
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
# 格式化MAC地址
formatted_mac = '-'.join([mac[i:i + 2] for i in range(0, 12, 2)]).upper()

global_player = {}


class Player(object):
    def __init__(self, uid=None, host=SERVER_HOST, port=PORT):
        """
        param uid: player uid
        :param host: game server host
        :param port: game server port
        """
        self.host = host
        self.port = port
        self.uid = uid
        self.is_connected = False
        self.client = None
        self.key = ''
        self.nGameServerIP = ''
        self.nGameServerPort = ''

    def add_event(self, event_name, event_func, *args, **kwargs):
        if not self.client:
            self.client = Client(host=self.host, port=self.port)
        self.client.add_event(event_name, event_func, *args, **kwargs)

    def load_proto(self):
        path = os.path.dirname(os.path.dirname(__file__)) + "/proto/"
        sys.path.append(path)  # 把协议文档目录加入到path,不然import的时候找不到模块
        # 把协议文件读入内存
        for name in os.listdir(path):
            if name == '__init__.py' or name[-3:] != '.py':
                continue
            module = importlib.import_module("proto.{}".format(name[:-3]))
            for item in dir(module):
                self.client.pb[item] = getattr(module, item)

    '''
       UID登录
    '''

    def login_by_uid(self, uid, ver=CLIENT_VERSION, key='0d937722b6100ec88a4bce23ad451d0b'):
        # logger.info("[login][function=run,uid={}]start".format(uid))
        # client = Client(uid, self.host, self.port)
        # if hasattr(client, 'is_login') and client.is_login:
        #     logger.info("[login][function=run,uid={}]exit".format(uid))
        #     return [proto.UserLoginRSP(), proto.UserLocationRSP()]

        while uid in global_player and not global_player[uid]:
            gevent.sleep(0.1)
        # if uid in global_player:
        #     return 0, global_player[uid]
        global_player[uid] = None  # 先占位,不然两个协程同时登陆同一个uid会报错
        if not self.client:
            self.client = Client(uid=self.uid, host=self.host, port=self.port)
        if self.client.isStop:
            logger.info("connect host failed,host:{},port:{}".format(self.host, self.port))
            return
        # self.load_proto()
        req = {
            'uid': uid,
            'key': key,
            'ip': '127.0.0.1',
            'login_type': 0,
            'entry_host': '47.91.130.120',
            'entry_port': '10001',
            'mobile_network': '中国移动'
        }
        self.client.uid = uid
        self.key = key
        self.client.send('UserLoginREQ', req)
        msg = self.client.recv("UserLoginRSP")
        if msg.body['code'] == 0:
            logger.info('uid:{} 登录成功'.format(self.client.uid))
            self.is_connected = True
            global_player[uid] = self
            return 0, self
        else:
            global_player.pop(uid)  # 登陆失败取消占位
            logger.error('uid:{} 登录失败 code:{}'.format(self.client.uid, msg.body.code))
            return 1, msg

    def login_php(self, user_name=None, password=None, clientip="211.97.6.100", operating_company="中国 移动",
                  country='Singapore', appid='globle', os='windows', imei='44-E5-17-99-D2-C5', clientvar=CLIENT_VERSION,
                  region=2, platform_type=1, lang='sc', host=None, port=None):
        """
           platform_type=1 default
           platform_type=2 ANDROID FaceBook
           platform_type=4 Iphone or IPad FaceBook
           platform_type=5  Iphone or IPad APPSTORE_INDIVIDUAL_VERSION
       """
        if host and port:
            url = "http://" + host + "/poker/api/login.php"
        elif host and not port:
            url = "http://" + host + "/poker/api/login.php"
        elif not host and port:
            url = "http://" + self.host + ":" + str(port) + "/poker/api/login.php"
        else:
            url = "http://" + self.host + "/poker/api/login.php"

        logger.info(url)
        if not password:
            password = user_name
        data = {
            'type': str(EMAIL_LOGIN_TYPE),
            'region': str(region),
            'username': user_name,
            'password': md5(md5('KKPoker') + md5(md5(password))),
            'distributor': G_Distributor,
            'sub_distributor': G_SubDistributor,
            'country': str(country),
            'appid': str(appid),
            'os': str(os),
            'imei': str(imei),
            'clientvar': str(clientvar),
            'lang': lang,
            'platform_type': platform_type,
            # 'clientip':clientip,
            'operating_company': operating_company,
        }
        lt = []
        for k, v in data.items():
            lt.append(k + '=' + str(v))
        query_string = '&'.join(lt)
        login_url = url + '?' + query_string
        logger.info('____________________{}'.format(login_url))

        headers = {'X-Forwarded-For': clientip}
        # response = requests.post(url,data=data,headers=headers)
        response = requests.get(login_url)
        data = response.json()
        if response.status_code != 200:
            logger.error('登录失败：' + str(data))
            return 1, str(data)
        elif data['code'] == 0:
            uid = data['uid']
            rdkey = data['rdkey']
            gserver_ip = data['gserver_ip']
            gserver_port = int(data['gserver_port'])
            return 0, {'uid': uid, 'rdkey': rdkey, 'gserver_ip': gserver_ip, 'gserver_port': gserver_port}
        else:
            return 1, data['code']

    def login_by_username(self, user_name, password=None, clientip="211.97.6.100", operating_company="中国 移动",
                          country='Singapore', appid='globle', os='windows', imei=formatted_mac,
                          clientvar=CLIENT_VERSION, region=2, platform_type=1, lang='sc', host=SERVER_HOST, port=PORT):
        result = self.login_php(user_name=user_name, password=password, clientip=clientip,
                                operating_company=operating_company, country=country, appid=appid,
                                os=os, imei=imei, clientvar=clientvar, region=region, platform_type=platform_type,
                                lang=lang, host=host, port=port)
        if result[0] == 1:
            logger.error('UserName登录失败')
            return 1, result[1]
        else:
            uid = result[1]['uid']
            key = result[1]['rdkey']
            gserver_ip = result[1]['gserver_ip']
            gserver_port = result[1]['gserver_port']
            self.host = gserver_ip
            self.port = gserver_port
            data = self.login_by_uid(uid, ver=clientvar, key=key)
            if data[0] == 0:
                return 0, data[1]
            else:
                return 1, data[1]

    '''
         注册
    '''

    def register(self, user_name, password=None, clientip="211.97.6.100", operating_company="中国移动", country='CN',
                 appid='globle', os='windows',
                 imei='2C-F0-5D-00-AB-95', clientvar=CLIENT_VERSION,
                 region=2):
        if not password:
            password = user_name
        data = {
            'username': user_name,
            'password': md5(md5(password)),
            'distributor': G_Distributor,
            'sub_distributor': G_SubDistributor,
            'country': str(country),
            'appid': str(appid),
            'os': str(os),
            'imei': str(imei),
            'clientvar': str(clientvar),
            'region': str(region),
            'clientip': clientip,
            'operating_company': operating_company,
        }
        url = "http://" + SERVER_HOST
        url = url + '/poker/api/register.php'
        url = url + '?'
        url = url + 'username=' + user_name
        url = url + '&password=' + md5(md5(password))
        url = url + "&clientip=" + clientip
        url = url + "&distributor=" + G_Distributor
        url = url + "&sub_distributor=" + G_SubDistributor
        url = url + '&country=' + str(country)
        url = url + "&appid=" + str(appid)
        url = url + "&os=" + str(os)
        url = url + "&imei=" + str(imei)
        url = url + "&clientvar=" + clientvar
        url = url + "&region=" + str(region)
        response = requests.get(url, verify=False)
        # response = requests.post(SERVER_HOST+'poker/api/register.php',data)
        code = response.status_code
        data = response.json()

        if code != 200:
            logger.error('HttpRequest Failed, Username= %s' % clientvar)
            return
        elif not data:
            return
        elif data['code'] == 0:
            self.login_by_username(user_name, password, clientip)
            if self.is_connected:
                return 0, self
            else:
                return
        elif str(data['code']) == '-4':
            logger.error('当前设备被封禁：' + str(data))
            return 1, str(data)
        else:
            logger.error('注册失败：' + str(data))
            return 1, str(data)

    '''
    检查用户是否已存在
    '''

    @staticmethod
    def check_user(user_name):
        player = Player()
        url = "http://" + SERVER_HOST + '/poker/api/check_username.php?username=' + user_name

        response = requests.get(url, verify=False)
        if response.status_code == 200:
            if eval(response.content)['code'] == -1:
                return 1
            if eval(response.content)['code'] == 0:
                return 0
        else:
            return -1

    '''
      获取ip,不带端口号
      parm
    '''

    def get_ip(self, link):  # 获取ip,不带端口号
        mode = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        ip = mode.findall(link)
        if (ip == []):
            arr = link.split("/")
            ip.append(arr[2])
        return ' '.join(ip)

    '''
         获取两个时间戳相差多少秒
         parm
         '''

    @staticmethod
    def gettimedifference(time1, time2):
        x = (datetime.datetime.fromtimestamp(time1) - datetime.datetime.fromtimestamp(time2)).seconds
        return x

    '''
         日期转时间戳
         parm
    '''

    @staticmethod
    def Date_to_timestamp(times):
        # 转为时间数组
        timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
        # 转为时间戳
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    '''
      随机生成ip地址
      parm
    '''

    @staticmethod
    def get_random_ip(RANDOM_IP_POOL=['192.168.10.222/0']):
        str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
        str_ip_addr = str_ip.split('/')[0]
        str_ip_mask = str_ip.split('/')[1]
        ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
        mask = 0x0
        for i in range(31, 31 - int(str_ip_mask), -1):
            mask = mask | (1 << i)
        ip_addr_min = ip_addr & (mask & 0xffffffff)
        ip_addr_max = ip_addr | (~mask & 0xffffffff)
        return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

# if __name__ == '__main__':
#     from common.Client import Client
#     from common.player import Player
#     from config import SERVER_HOST, PORT
#
#     host = SERVER_HOST
#     port = PORT
#     php_server = SERVER_HOST
#
#     player = Player(host=host, port=port)
#     for i in range(2, 3):
#         username = 'bba' + str(i)
#         player.login_by_username(username, "wwwww1")
#     # player.login_by_uid(2507859)
#     # client = player.client
#     # client.send('ClubListREQ')
#     # msg=client.recv('ClubListRSP')
#     # logger.info(msg.body)
#     #
#     # logger.info(msg)
#     # result2 = player.login_by_uid(2955)
