import random
import string
import requests
from enum import Enum, unique
from lib.utils import *
from lib.CustomException import TimeOutException
from common.log import logger
import traceback


class Room():
    def __init__(self, roomid):
        self.roomid = roomid
        self.seatid = None
        self.chips = 0
        self.roomstatus = False
        self.roominfo = None
        self.roomdata = {}
        self.players = {}
        self.rebuytime = -1
        self.handcards = []
        self.sitdowntime = None
        self.gameid = 1  # 房间当前的gameid

    @staticmethod
    def enter_room(client, roomid):
        """
        进入指定id房间
        :param client:
        :param roomid:
        :return:
        """
        req = {
            "roomid": roomid,
            "password": ""
        }
        try:
            client.send("EnterRoomREQ", req)
            msg = client.recv("EnterRoomRSP")
            if msg.body['code'] == 0:
                logger.info('uid:{}|roomid:{}|EnterRoomRSP success'.format(client.uid, msg.head.roomid))
            else:
                logger.error(
                    'uid:{}|roomid:{}|code:{}|EnterRoomRSP failed.'.format(client.uid, roomid, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def quick_start(client, reqs):
        """
        快速游戏,由服务器分配roomid, 通过传入的reqs里的各项参数控制房间类型及买入
        :param client:
        :param reqs:
        :return:
        """
        req = {
            "type": reqs["type"],
            "lobby_coin": reqs["lobby_coin"],
            "lobby_type": reqs["lobby_type"],
            "boot": reqs["boot"],
            "room_type": reqs["room_type"],
            "room_sub_type": reqs["room_sub_type"]
        }
        try:
            client.send("QuickStartREQ", req)
            msg = client.recv("EnterRoomRSP")
            if msg.body['code'] == 0:
                logger.info('uid:{}| roomid:{}| EnterRoomRSP success'.format(client.uid, msg.head.roomid))
            else:
                logger.error('uid:{}| EnterRoomRSP failed. code:{}'.format(client.uid, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    '''
        进入房间
        通过传入的reqs里的各项参数控制房间类型及买入
        '''

    @staticmethod
    def enter_room_kkc(client, reqs):
        req = {
            "boot": reqs["boot"],
            "room_sub_type": reqs["room_sub_type"]
        }
        try:
            client.send("QuickStartREQ", req)
            msg = client.recv("QuickStartRSP")
            if msg.body['code'] == 0:
                logger.info('uid:{}| QuickStartRSP success'.format(client.uid))
            else:
                logger.error('uid:{}| QuickStartRSP failed. code:{}'.format(client.uid, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    '''
    坐下
    seat_id: 座位id
    '''

    @staticmethod
    def sit_down(client, chips, roomid=0):
        req = {
            'seatid': 0,
            'chips': chips,
            "pc": True
        }
        try:
            for seatid in range(5):
                req['seatid'] = seatid
                client.send('SitDownREQ', req, roomid)
                msg = client.recv('SitDownRSP')
                if msg.body['code'] == 0:
                    logger.info('uid:{}|roomid:{}|seat_id:{}|SitDownRSP success'.format(client.uid, roomid, seatid))
                    break
                elif msg.body['code'] == -1:
                    logger.error("uid:{}|roomid:{}|seat_id:{}|SitDownRSP failed cause chips not enough"
                                 .format(client.uid, roomid, seatid))
                    break
                elif msg.body['code'] == -2:  # 座位上有人坐入失败,不处理,继续坐下一个位置
                    pass
                else:
                    logger.error('uid:{}|roomid:{}|seat_id:{}|SitDownRSP failed.code:{}'
                                 .format(client.uid, roomid, seatid, msg.body['code']))
        except:
            logger.error('uid:{}|seat_id:{}|SitDownRSP time out.'.format(client.uid, req['seatid']))
            logger.error(traceback.format_exc())
            return

    '''
    站起
    client: 站起的客户端
    '''

    @staticmethod
    def sit_up(client, roomid):
        req = {}
        client.send('StandUpREQ', req, roomid)
        try:
            msg = client.recv('StandUpRSP')
            if msg.body['code'] == 0:
                logger.info('uid:{}|roomid:{}|StandUpRSP success'.format(client.uid, roomid))
            else:
                logger.error('uid:{}|roomid:{}|StandUpRSP failed.code:{} '.format(client.uid, roomid, msg.body['code']))
            return msg
        except:
            logger.error('uid:{}|roomid:{}|SitDownRSP time out.'.format(client.uid, roomid))
            logger.error(traceback.format_exc())
            return

    '''
    离开房间
    '''

    @staticmethod
    def leave_room(client, roomid=0):
        req = {}
        try:
            client.send('LeaveRoomREQ', req, roomid)
            msg = client.recv("LeaveRoomRSP", 1)
            if msg.body['code'] == 0:
                logger.info('uid:{}|LeaveRoomREQ success'.format(client.uid))
            else:
                logger.error('uid:{}|LeaveRoomRSP failed. code:{}'.format(client.uid, msg.body['code']))
            return msg
        except TimeOutException:
            logger.error('uid:{}|LeaveRoomRSP time out.'.format(client.uid))
            return
        except BaseException:
            logger.error(traceback.format_exc())
            return

    '''
    打牌行动
    '''

    @staticmethod
    def action(client, action_type, chips=0, roomid=0):
        req = {
            'action_type': action_type,
            'chips': chips
        }
        try:
            client.send("ActionREQ", req, roomid)
            msg = client.recv('ActionBRC')
            if msg:
                logger.info('uid:{}|ActionBRC success action_type:{} chips:{}'.format(str(client.uid), Room.ActionType(
                    msg.body['action_type']), int(msg.body['chips']) / 100))
                return msg
            else:
                logger.error(
                    'uid:{} ActionBRC failed action_type:{} chips:{}'.format(str(client.uid), action_type, chips / 100))
                return
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def teen_action(client, action_type, is_raise=False, roomid=0):
        """
        TP打牌行动
        :param client:
        :param action_type:
        :param is_raise:
        :param roomid:
        :return:
        """
        req = {
            'action_type': action_type,
            'raise': is_raise
        }
        try:
            client.send("TeenActionREQ", req, roomid)
            msg = client.recv('TeenActionBRC')
            if msg:
                logger.info(
                    'uid:{}|TeenActionBRC success | action_type:{} putin:{}'.format(str(client.uid), action_type,
                                                                                    int(msg.body['putin']) / 100))
                return msg
            else:
                logger.error(
                    'uid:{} TeenActionBRC failed | action_type:{} raise:{}'.format(str(client.uid), action_type,
                                                                                   is_raise))
                return
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def get_teen_action_type(msg, roomobj, Operation_type=1, action_weight=[5, 5, 90]):
        """
        根据权重计算TP行动类型
        :param msg:
        :param roomobj:
        :param Operation_type:类型 1：随机 2：PACK 3：SHOW
        :param action_weight:行动的权重,分别对应客户端的3个操作类型:[PACK, SHOW/SIDESHOW, BLIND/CHAAL]
        :return:
        """
        action_type_list = ['PACK', 'SHOW', 'BET']
        action_type = 1  # 默认pack(1:pack, 2:blind, 3:chaal, 4:side show, 5:show)
        is_raise = False
        action_weight = action_weight.copy()  # copy一下，不然会影响下次行动
        if Operation_type == 2:
            pass
        elif Operation_type == 3:
            if "show_flag" in roomobj.teenstatus and roomobj.teenstatus["show_flag"] != 0:
                if roomobj.teenstatus["show_flag"] == 1:  # 1 side show 2 show
                    action_type = 4
                else:
                    action_type = 5
        else:
            if not ("show_flag" in roomobj.teenstatus and roomobj.teenstatus["show_flag"] != 0):
                action_type_list.pop(1)  # 不能show，所以把show操作去掉
                action_weight.pop(1)  # show的权重也要去掉
            action_type_str = get_random_value(action_type_list, action_weight)
            if action_type_str == 'BET':
                if "seen_cards" not in roomobj.teenstatus or roomobj.teenstatus["seen_cards"] != True:
                    action_type = 2  # 未看牌，行动类型是2
                else:
                    action_type = 3  # 已看牌，行动类型是3
                if msg.body['can_raise']:
                    is_raise = random.choice([True, False])
                else:
                    is_raise = False
            elif action_type_str == 'SHOW':
                if "show_flag" in roomobj.teenstatus and roomobj.teenstatus["show_flag"] != 0:
                    if roomobj.teenstatus["show_flag"] == 1:  # 1 side show 2 show
                        action_type = 4
                    else:
                        action_type = 5
        return action_type, is_raise

    @staticmethod
    def teen_see_cards(client, roomid=0):
        """
        TP查看手牌
        :param client:
        :return:
        """
        req = {
        }
        try:
            client.send("TeenSeenCardREQ", req, roomid)
            msg = client.recv('TeenSeenCardRSP')
            if msg:
                logger.info('uid:{}|TeenSeenCardRSP success | seatid:{} cards:{}'.format(str(client.uid),
                                                                                         msg.body['info']['seatid'],
                                                                                         msg.body['info']['cards']))
                return msg
            else:
                logger.error('uid:{} TeenSeenCardRSP failed'.format(str(client.uid)))
                return
        except:
            logger.error(traceback.format_exc())

    @staticmethod
    def teen_response_side_show(client, code=0, roomid=0):
        """
        TP回应玩家的sideshow请求
        :param client:
        :param code:0 同意 1 拒绝
        :return:
        """
        req = {
            "code": code
        }
        try:
            if code == 0:  # 同意sideshow，服务器返回的是TeenSideShowResultBRC
                client.send("TeenSideShowResponseREQ", req, roomid)
                msg = client.recv("TeenSideShowResultBRC")
                if msg:
                    logger.info('uid:{}|TeenSideShowResultBRC success | loser_seatid:{}'.format(str(client.uid),
                                                                                                msg.body[
                                                                                                    'loser_seatid']))
                    return msg
                else:
                    logger.error('uid:{} TeenSideShowResultBRC failed'.format(str(client.uid)))
                    return
            else:  # 拒绝sideshow，服务器返回的是TeenSideShowResponseBRC
                client.send("TeenSideShowResponseREQ", req, roomid)
                msg = client.recv("TeenSideShowResponseBRC")
                if msg:
                    logger.info(
                        'uid:{}|TeenSideShowResponseBRC success | request_seatid:{} | response_seatid:{}'.format(
                            str(client.uid), msg.body['request_seatid'], msg.body['response_seatid']))
                    return msg
                else:
                    logger.error('uid:{} TeenSideShowResponseBRC failed'.format(str(client.uid)))
                    return
        except:
            logger.error(traceback.format_exc())

    @staticmethod
    def teen_button_choice(client, game_type, roomid=0):
        """
        TP庄家选择玩法类型
        :param client:
        :param game_type:玩法类型(,2:Joker,3:AK47,4:Hukam,5:Royal,6:Muflis,7:Lowest Joker,8:999,9:Pot Blind,)
        :return:
        """
        req = {
            "game_type": game_type
        }
        try:
            client.send("TeenButtonChoiceREQ", req, roomid)
            msg = client.recv('TeenGameTypeBRC')
            if msg:
                logger.info('uid:{}|TeenGameTypeBRC success | real_game_type:{}'.format(str(client.uid),
                                                                                        msg.body['real_game_type']))
                return msg
            else:
                logger.error('uid:{} TeenGameTypeBRC failed'.format(str(client.uid)))
                return
        except:
            logger.error(traceback.format_exc())

    #
    # @staticmethod
    # def action_bet(client, action_type, chips=1, roomid=0):
    #     req = {
    #         'putin': action_type,
    #         'dot': chips
    #     }
    #     try:
    #         client.send("DiceBetREQ", req, roomid)
    #         msg = client.recv('DiceBetBRC')
    #         if msg:
    #             logger.info('uid:{}|DiceBetBRC success action_type:{} chips:{}'.format(str(client.uid),msg.body['putin'],msg.body['dot']))
    #             return msg
    #         else:
    #             logger.error('uid:{} DiceBetBRC failed'.format(str(client.uid)))
    #             return
    #     except:
    #         logger.error(traceback.format_exc())
    #         return

    '''
     回到座位
     parm
    '''

    @staticmethod
    def back_to_seat(client, roomid=0, reserve=False):
        req = {
            'reserve': reserve,
        }
        try:
            client.send('ReserveSeatREQ', req)
            msg = client.recv('ReserveSeatRSP', 3)
            return msg
        except TimeOutException:
            logger.error('uid:{}ReserveSeatREQ time out.'.format(client.uid))
            return
        except:
            logger.error(traceback.format_exc())
            return

    '''
    行动判断 
    parm
    Operation_type：类型 1：随机 2：FOLD 3：allin
    action_weight: 行动的权重,分别对应客户端的3个操作类型:[弃牌/过牌, 过牌/跟注, 下注/加注]
    action_type: 行动
    chips:   下注筹码
    '''

    @staticmethod
    def action_judge(msg, Operation_type=1, action_weight=[5, 90, 5]):
        chips = 0
        action_type_list = [1, 3, 4]
        call_need_chips = msg['call_need_chips']
        min_chipin = msg['min_chipin']
        max_chipin = msg['max_chipin']
        if Operation_type == 2:
            action_type = 1
        elif Operation_type == 3:
            action_type = 4
        else:
            action_type = get_random_value(action_type_list, action_weight)
        if action_type == 1:
            if call_need_chips == 0 and Operation_type != 2:
                action_type = 2
        elif action_type == 3:
            chips = call_need_chips
            if call_need_chips == 0:
                action_type = 2
        elif action_type == 4:
            if Operation_type == 3 or min_chipin > max_chipin:
                chips = max(min_chipin, max_chipin)
            else:
                chips = random.randint(int(min_chipin), int(min_chipin))
                # 先去掉取到的随机数的后两位后*100
                chips = chips.__floordiv__(100) * 100
        return action_type, chips

    @staticmethod
    def room_random_action_events(client, roomid, room_eventtype=1, room_eventtype_weight=[80, 5, 10, 5], setid=None):
        """
        房间内随机行动事件
        :param client:
        :param room_eventtype:事件类型 0 不触发  1 随机 2 用户发送表情  3 用户发言 4 用户发送互动道具
        :param room_eventtype_weight:随机事件每个值比例
        :return:
        """
        pass

    @staticmethod
    def room_rummy_take_card(client, roomid, choose):
        """
        rummy玩法摸牌
        :param client:
        :param roomid:
        :param choose: "open" 拿明牌, "close"
        :return:
        """
        req = {
            'choose': choose,
        }
        try:
            client.send('RummyCardREQ', req, roomid)
            msg = client.recv('RummyCardRSP')
            logger.info('uid:{}|RummyCardRSP success | card:{}'.format(str(client.uid), msg.body['card']))
            return msg
        except TimeOutException:
            logger.error('uid:{}|RummyCardRSP time out.'.format(client.uid))
            return
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_rummy_discard_card(client, roomid, req):
        """
        rummy玩法丢牌
        :param client:
        :param roomid:
        :param req:
        :return:
        """
        try:
            client.send('RummyDiscardREQ', req, roomid)
            roomobj = client.get_room_obj(roomid)
            msg = client.recv('RummyDiscardRSP', 3)
            logger.info('uid:{}|RummyDiscardRSP success | card:{}'.format(str(client.uid), msg.body['brc']['discard']))
            return msg
        except TimeOutException:
            logger.error('uid:{}|RummyDiscardRSP time out.'.format(client.uid))
            return
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_rummy_drop(client, roomid):
        """
        rummy玩法弃牌
        :param client:
        :param roomid:
        :return:
        """
        req = {}
        try:
            client.send('RummyDropREQ', req, roomid)
            msg = client.recv('RummyDropBRC')
            logger.info('uid:{}| RummyDropBRC success '.format(str(client.uid)))
            return msg
        except TimeOutException:
            logger.error('uid:{}| RummyDropBRC time out.'.format(client.uid))
            return
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_make_friends(client, target_uid):
        """
        KKC 添加好友申请
        :param client:
        :param target_uid:
        :return:
        """
        req = {
            "target_uid": target_uid
        }
        try:
            client.send('UserFriendREQ', req)
            msg = client.recv('UserFriendRSP')
            if msg:
                if msg.body['code'] == 0:
                    logger.info('uid:{}|target_uid:{}|UserFriendRSP success.'.format(str(client.uid), target_uid))
                elif msg.body['code'] == -1:
                    logger.info('uid:{}|target_uid:{}|UserFriendRSP failed, already friend.'
                                .format(str(client.uid), target_uid))
                else:
                    logger.error('uid:{}|target_uid:{}|code:{}|UserFriendRSP failed.'
                                 .format(str(client.uid), target_uid, msg.body['code']))
            else:
                logger.error('uid:{}|target_uid:{}|UserFriendRSP failed.'.format(str(client.uid), target_uid))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def confirm_friend(client, accept):
        """
        KKC 同意好友申请
        :param client:
        :param accept:
        :return:
        """
        req = {
            "accept": accept
        }
        try:
            client.send('UserConfirmFriendREQ', req)
            msg = client.recv('UserConfirmFriendRSP')
            if msg:
                if msg.body['code'] == 0:
                    logger.info('uid:{}| target_uid:{}|UserConfirmFriendRSP success '
                                .format(str(client.uid), msg.body['accept']))
                else:
                    logger.error('uid:{}| target_uid:{}| code:{}| UserConfirmFriendRSP failed '
                                 .format(str(client.uid), accept, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_invite_friend(client, to_uids, mtt_id, room_type):
        """
        KKC truco_mtt 邀请好友
        :param client:
        :param to_uids:
        :param mtt_id:
        :return:
        """
        req = {
            "to_uids": to_uids,
            "mtt_id": mtt_id,
            "room_type": room_type
        }
        try:
            client.send('NewMttInviteREQ', req)
            msg = client.recv('NewMttInviteRSP')
            if msg:
                if msg.body['code'] == 0:
                    logger.info('uid:{}| to_uids:{} | NewMttInviteRSP success '.format(str(client.uid), to_uids))
                else:
                    logger.error('uid:{}| to_uids:{}| code:{}| NewMttInviteRSP failed '
                                 .format(str(client.uid), to_uids, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_truco_mtt_enter_team(client, mtt_id, room_type, teamid=0):
        """
        KKC truco_mtt 进入队伍
        :param client:
        :param mtt_id:
        :param teamid:
        :room_type:17-ca mtt,16-truco mtt
        :return:
        """
        req = {
            "mtt_id": mtt_id,
            "teamid": teamid,
            "password": "",
            "room_type": room_type
        }
        try:
            client.send('NewMttEnterTeamREQ', req)
            msg = client.recv('NewMttEnterTeamRSP')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|mtt_id:{}|teamid:{}|NewMttEnterTeamRSP success '
                            .format(str(client.uid), mtt_id, teamid))
            else:
                logger.error('uid:{}|mtt_id:{}|teamid:{}|code:{}|NewMttEnterTeamRSP fail '
                             .format(str(client.uid), mtt_id, teamid, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_truco_mtt_register(client, is_register, mtt_id, room_type):
        """
        KKC truco_mtt 报名
        :param client:
        :param is_register: True:报名,False:取消报名
        :param mtt_id:
        :return:
        """
        req = {
            "is_register": is_register,
            "mtt_id": mtt_id,
            "room_type": room_type
        }
        try:
            client.send('NewMttRegisterREQ', req)
            msg = client.recv('NewMttRegisterRSP')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|mtt_id:{}|NewMttRegisterRSP success '.format(str(client.uid), mtt_id))
            else:
                logger.error('uid:{}|mtt_id:{}|code:{}|NewMttRegisterRSP failed '
                             .format(str(client.uid), mtt_id, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_adbh_action(client, req, roomid):
        """
        Andar Bahar 行动
        :param client:
        :param req:
        :param roomid:
        :return:
        """
        try:
            client.send('AdBhActionREQ', req, roomid)
            msg = client.recv('AdBhActionBRC')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|req:{}|AdBhActionBRC success '.format(str(client.uid), req))
            else:
                logger.error('uid:{}|req:{}|code:{}|AdBhActionBRC failed '
                             .format(str(client.uid), req, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_luckywar_action(client, req, roomid):
        """
        Lucky War 行动
        :param client:
        :param req:
        :param roomid:
        :return:
        """
        try:
            client.send('CSWarActionREQ', req, roomid)

            msg = client.recv('CSWarActionBRC')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|req:{}|CSWarActionBRC success '.format(str(client.uid), req))
            else:
                logger.error('uid:{}|req:{}|code:{}|CSWarActionBRC failed '
                             .format(str(client.uid), req, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_get_adbh_pvp_room_list(client):
        """
        Andar Bahar PVP获取房间列表
        :param client:
        :return:
        """
        req = {}
        try:
            client.send('AdBhPVPRoomListREQ', req)

            msg = client.recv('AdBhPVPRoomListRSP')
            if msg:
                logger.info('uid:{}|AdBhPVPRoomListRSP success '.format(str(client.uid)))
            else:
                logger.error('uid:{}|AdBhPVPRoomListRSP failed '.format(str(client.uid)))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_get_lucky_war_pvp_room_list(client):
        """
        Lucky War PVP获取房间列表
        :param client:
        :return:
        """
        req = {}
        try:
            client.send('CSWarPVPRoomListREQ', req)
            msg = client.recv('CSWarPVPRoomListRSP')
            if msg:
                logger.info('uid:{}|CSWarPVPRoomListRSP success '.format(str(client.uid)))
            else:
                logger.error('uid:{}|CSWarPVPRoomListRSP failed '.format(str(client.uid)))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_lob_mtt_register(client, mtt_id, room_type, mtt_sub_type, is_register=True):
        """
        MTT 报名
        :param client:
        :param mtt_id:
        :param room_type:  2:poker,  10:teenpatti
        :param mtt_sub_type: 0为普通mtt  1为人满即开mtt
        :param is_register: True:报名, False:取消报名
        :return:
        """
        req = {
            "mtt_id": mtt_id,
            "is_register": is_register,
            "room_type": room_type,
            "mtt_sub_type": mtt_sub_type
        }
        try:
            client.send('LobMttRegisterREQ', req)
            msg = client.recv('LobMttRegisterRSP')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|mtt_id:{}|LobMttRegisterRSP success '.format(str(client.uid), mtt_id))
            else:
                logger.error('uid:{}|mtt_id:{}|code:{}|LobMttRegisterRSP failed '.format(str(client.uid), mtt_id,
                                                                                         msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())

    @staticmethod
    def room_chatai_action(client, card, x, y, roomid):
        """
        Chatai 行动
        :param client:
        :param req:
        :param roomid:
        :return:
        """
        req = {
            "action_card": {
                "x": x,
                "y": y,
                "card": card
            }
        }
        try:
            client.send('ChataiActionREQ', req, roomid)

            msg = client.recv('ChataiActionRSP')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|roomid:{}|req:{}|ChataiActionRSP success '.format(str(client.uid), roomid, req))
            else:
                logger.error('uid:{}|req:{}|code:{}|ChataiActionRSP failed '
                             .format(str(client.uid), req, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_blackjack_action(client, roomid, action_type, action_chips=0, cards_idx=1, sub_type=0, next_cards_num=0):
        """
        BlackJack 行动
        :param client:
        :param action_type: # 玩家行动类型, 1下注，2购买保险，3双倍注，4分牌，5停止牌，6要牌，7超时停牌（系统使用）
        :param action_chips: # 行动的chips
        :param cards_idx: # 行动的牌堆，有效值从1开始，目前有效值为1与2
        :param sub_type: # 购买保险操作有使用，1购买保险，2放弃购买保险，3超时未购买保险（系统使用）
        :param next_cards_num: # 在action_type为6（要牌）时使用，表示玩家要的是第几张牌（玩家当前牌堆手牌数加1）
        :return:
        """
        req = {
            "action_type": action_type,
            "action_chips": action_chips,
            "cards_idx": cards_idx,
            "sub_type": sub_type,
            "next_cards_num": next_cards_num
        }
        try:
            client.send('BlackJackActionREQ', req, roomid)

            msg = client.recv('BlackJackActionRSP')
            if msg and msg.body['code'] == 0:
                logger.info('uid:{}|roomid:{}|req:{}|BlackJackActionRSP success '.format(str(client.uid), roomid, req))
            else:
                logger.error('uid:{}|req:{}|code:{}|BlackJackActionRSP failed '
                             .format(str(client.uid), req, msg.body['code']))
            return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_dragon_tiger_action(client, roomid, req_hand_id, area_id=0, chips=0):
        """
            Dragon Tiger 行动
            :param client:
            :param req_hand_id: # 针对哪一手牌下注,避免弱网情况下,把注下到了下一手
            :param dragon_chips: # 压龙赢
            :param tie_chips: # 压平局
            :param tiger_chips: # 压虎赢
            :return:
            """
        req_type = random.randint(1, 2)
        if req_type == 1:
            req = {
                "req": {
                    "tie_chips": 0,
                    "dragon_chips": 0,
                    "tiger_chips": 0,
                    "id": area_id,
                    "value": chips
                },
                "req_hand_id": req_hand_id,
                "req_type": 1
            }
        else:
            req = {
                "req_hand_id": req_hand_id,
                "req_type": 2
            }
        try:
            client.send('DgTgActionREQ', req, roomid)
            # msg = client.recv('DgTgActionBRC')  # 没有RSP,就不在这里recv了
            # if msg and msg.body['code'] == 0:
            #     logger.info('uid:{}|roomid:{}|req:{}|DgTgActionBRC success '.format(str(client.uid), roomid, req))
            # else:
            #     logger.error('uid:{}|req:{}|code:{}|DgTgActionBRC failed '.format(str(client.uid), req, msg.body['code']))
            # return msg
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_three_two_action(client, roomid, req_hand_id, area_id=0, chips=0):
        """
        Dragon Tiger 行动
        :param client:
        :param req_hand_id: # 针对哪一手牌下注,避免弱网情况下,把注下到了下一手
        :param id: # 1-player8,2-player9,3-player10,4-player11
        :param value: # 下注数值

        :return:
        """
        req_type = random.randint(1, 2)
        if req_type == 1:
            req = {
                "req": {
                    "id": area_id,
                    "value": chips,
                    "bet_type": random.randint(1, 2)

                },
                "req_hand_id": req_hand_id,
                "req_type": 1
            }
        else:
            req = {
                "req_hand_id": req_hand_id,
                "req_type": 2
            }
        try:
            client.send('ThirtyTwoCardActionREQ', req, roomid)
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def wingo_lottery_action(client, roomid, req_hand_id, area_id=0, chips=0):
        """
        WingoAction行动
        :param client:
        :param roomid:
        :param req_hand_id:
        :param area_id: 100~109对应0~9区  110对应单数区(1/3/7/9)  111对应双数区(2/4/6/8)  112对应特殊区(0/5)
        :param chips:
        :return:
        """
        req_type = random.randint(1, 2)
        if req_type == 1:
            req = {
                "req": {
                    "id": area_id,
                    "value": chips,
                },
                "req_hand_id": req_hand_id,
                "req_type": 1
            }
        else:
            req = {
                "req_hand_id": req_hand_id,
                "req_type": 2
            }
        try:
            client.send('WingoActionREQ', req, roomid)
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def dice_action(client, roomid, req_hand_id, area_id=0, chips=0, req_type=1):
        if req_type == 1:
            req = {
                "req": {
                    "id": area_id,
                    "value": chips,
                },
                "req_hand_id": req_hand_id,
                "req_type": 1
            }
        else:
            req = {
                "req_hand_id": req_hand_id,
                "req_type": 2
            }
        try:
            client.send('DiceActionREQ', req, roomid)
            logger.info("uid:{} | roomid:{} |req :{}".format(str(client.uid), roomid, req))
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def wheel_action(client, roomid, req_hand_id, area_id=0, chips=0, req_type=1):
        if req_type == 1:
            req = {
                "req": {
                    "id": area_id,
                    "value": chips,
                },
                "req_hand_id": req_hand_id,
                "req_type": 1
            }
        else:
            req = {
                "req_hand_id": req_hand_id,
                "req_type": 2
            }
        try:
            client.send('WheelActionREQ', req, roomid)
            logger.info("uid:{} | roomid:{} |req :{}".format(str(client.uid), roomid, req))
        except:
            logger.error(traceback.format_exc())
            return

    @staticmethod
    def room_sent_gift(client, roomid, target_seats, sent):
        """
        牌桌内随机赠送礼物
        :param client:
        :return:
        """
        if sent == 1:
            gift_list = {"gift_shit": 2, "gift_boom": 1, "gift_donkey": 1,
                         "gift_beer": 1, "gift_slipper": 1, "gift_flag_bd": 1, "gift_flag_in": 1,
                         "gift_flag_pk": 1, "gift_kiss": 2,
                         "gift_applaud": 1, "gift_chai": 2, "gift_gun": 1, "gift_nipple": 1,
                         "gift_thumb_down": 2, "gift_chicken": 3, "gift_cigar": 3, "gift_clock": 2,
                         "gift_eid_mubarak": 3,
                         "gift_namaste": 2, "gift_saucepan": 2, "gift_slipper_luxury": 3, "gift_sunglasses": 2,
                         "gift_tabla": 2, "gift_wicket": 2,
                         "gift_wow": 2, "gift_sheep": 3, "gift_christmas": 1
                         }
            gift = random.sample(gift_list.keys(), 1)
            req = {
                "target_seats": target_seats,
                "gift_id": gift[0],
                "gift_lvl": gift_list[gift[0]]
            }
            try:
                client.send('SendGiftREQ', req, roomid)
                # msg = client.recv_one(['UserValueRSP', 'SendGiftRSP','SendGiftBRC'])
                msg = client.recv('SendGiftRSP')
                if msg and msg.body['code'] == 0:
                    logger.info('uid:{}|roomid:{}|req:{}|SendGiftREQ success '.format(str(client.uid), roomid, req))
                else:
                    logger.error(
                        'uid:{}|req:{}|code:{}|SendGiftREQ failed '.format(str(client.uid), req, msg.body['code']))
                return msg

            except:
                logger.error(traceback.format_exc())
                return
        else:
            pass

    @staticmethod
    def room_sent_text(client, roomid, sent):
        """
        牌桌内发送随机文本
        :param client:
        :return:
        """
        if sent == 1:
            context = ''.join(random.sample(
                'abcdefghijkमইনসvwગુજરાતીવધારવા্টলराठीlmnopqrsसvwગુજરાતીવધારવા्vwગુજરાતીવધારવાथापितtuvwગુજરાતીવધારવામાં નxyz!@#$abcdefghijklmnopqrst%^&*()हिंदीবাvwગુજરાતીવધારવાংলা का विस्तार करने ',
                random.randint(20, 60)))
            req = {
                "content": context
            }
            try:
                client.send('TextREQ', req, roomid)
            except:
                logger.error(traceback.format_exc())
                return
        else:
            pass

    @staticmethod
    def room_usetransferCard(client, roomid):
        url = "http://{}:8005/?cmd=new_item_change&uid={}&item_id=6000001&num=1&flow_type=admin&flow_attach=".format(
            SERVER_HOST, client.uid)
        requests.get(url)
        client.send("NewItemGoldProtectREQ", {})
        msg = client.recv("NewItemGoldProtectRSP")
        list_itme = msg.body["list"]
        fixed_val = list_itme[0]["fixed_val"]
        # dynamic_val = msg.body["list"]["dynamic_val"]
        # opt_type = random.randint(1,2)
        opt_type = 1
        if opt_type == 1:
            val = int(fixed_val)
        else:
            val = 0
        req = {
            "opt_type": opt_type,
            "val": val
        }
        client.send("NewItemTableUseGoldProtectREQ", req, roomid)
        msg1 = client.recv("NewItemTableUseGoldProtectRSP")
        logger.info("NewItemTableUseGoldProtectRSP | 金币保护道具使用结果:{}".format(msg1.body['code']))

    @unique
    class ActionType(Enum):
        ACTION_NONE = 0;
        ACTION_FOLD = 1;
        ACTION_CHECK = 2;
        ACTION_CALL = 3;
        ACTION_RAISE = 4;
        ACTION_WAIT = 5;  # 等待下注
        ACTION_SITED = 6;  # 坐下，未入局状态
        ACTION_BET = 7;  # 第一个加注
        ACTION_SB = 8;  # 下小盲
        ACTION_BB = 9;  # 下大盲
        ACTION_ANTE = 10;  # 下前注
        ACTION_FORCE_BB = 11;  # 强制大盲
        # 系统操作产生的类型
        ACTION_SYSTEM_FOLD = 12;  # 系统自动弃牌
        ACTION_SYSTEM_CHECK = 13;  # 系统自动看牌
        ACTION_STRADDLE = 14;
        ACTION_POT = 15;  # 底池限注时，加注满一个pool
        ACTION_FAST_FOLD = 16;  # 快速桌快速弃牌

    @unique
    class HandType(Enum):
        TYPE_NONE = 0  # 小于5张牌，未成牌
        TYPE_FOLD = -1  # 弃牌
        TYPE_HIGH_CARD = 1  # 高牌
        TYPE_PAIR = 2  # 一对
        TYPE_TWO_PAIRS = 3  # 二对
        TYPE_THREE_KIND = 4  # 三条
        TYPE_STRAIGHT = 5  # 顺子
        TYPE_FLUSH = 6  # 同花
        TYPE_FULL_HOUSE = 7  # 葫芦
        TYPE_FOUR_KIND = 8  # 四条
        TYPE_STRAIGHT_FLUSH = 9  # 同花顺
        TYPE_ROYAL_FLUSH = 10  # 皇家同花顺
