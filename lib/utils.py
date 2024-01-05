import hashlib
import random
from lib.MysqlManager import Mysqldb
import os
import sys
import importlib
from config import SERVER_HOST
from WhiteList import whitelist

def bytesToHexString(bs):
    return ''.join(['%02X' % b for b in bs])


def md5(str):
    return hashlib.md5(str.encode('utf-8')).hexdigest()


def get_random_value(l, w):
    """
    按比例随机抽取列表数据(l:抽样数据列表 w:每个值对应的比例)
    :param l:
    :param w:
    :return:
    """
    rNum = random.randint(0, sum(w) - 1)
    for i, v in enumerate(w):
        rNum -= v
        if rNum < 0:
            return (l[i])


def cut(num, c):
    """
    保留几位小数不四舍五入
    :param num:
    :param c:
    :return:
    """
    str_num = str(num)
    return float(str_num[:str_num.index('.') + 1 + c])


def get_whitelist():
    _whitelist = whitelist[project]
    if SERVER_HOST in _whitelist:
        return _whitelist[SERVER_HOST]
    else:
        return []


def get_random_uids_from_mysql(num):
    """
    从数据库随机取指定数量的uid
    :param num: 需要取多少个uid
    :return:
    """
    SQL = Mysqldb()
    # 130000-135000之间是真实机器人,不能用，否则无法进入空房间，因为机器人不会主动创建房间
    # 10000-90000之间是虚拟机器人,不能用，否则无法进入空房间，因为机器人不会主动创建房间
    result = SQL.get_custom("pppoker", "select uid from user where nickname like '%kk%' and (uid<130000 or uid>135000) and (uid<10000 or uid>90000)")
    user_list = list(result)
    uid_list = []
    wl = get_whitelist()
    while num > 0:
        user = user_list.pop(random.randint(0, len(user_list)-1))
        if user[0] in wl:
            continue
        uid_list.append(user[0])
        num -= 1
    return uid_list

def get_random_register_username_from_mysql(num):
    """
        从数据库随机取指定数量密码为qa123456的注册账
        :param num: 需要取多少个uid
        :return:
        """
    SQL = Mysqldb()
    # result = SQL.get_custom("pppoker","select uid from register_user where pw_encode ='c685847be4692a061bc5810633437875'")
    result = SQL.get_custom("pppoker","select uid from register_user where pw_encode ='c685847be4692a061bc5810633437875'")
    user_list = list(result)
    uid_list = []
    wl = get_whitelist()
    while num > 0:
        user = user_list.pop(random.randint(0, len(user_list) - 1))
        if user[0] in wl:
            continue
        uid_list.append(user[0])
        num -= 1
    return uid_list

def get_random_register_username_from_mysql_username(num):
    """
    从数据库随机取指定数量密码为qa123456的注册账
    :param num: 需要取多少个username
    :return:
    """
    SQL = Mysqldb()
    # result = SQL.get_custom("pppoker","select uid from register_user where pw_encode ='c685847be4692a061bc5810633437875'")
    result = SQL.get_custom("pppoker","select username from register_user where pw_encode ='c685847be4692a061bc5810633437875'")
    user_list = list(result)
    uid_list = []
    while num > 0:
        user = user_list.pop(random.randint(0, len(user_list) - 1))
        uid_list.append(user[0])
        num -= 1
    return uid_list

def get_random_uid_from_kkc(num):
    """
       从数据库随机取指定数量的uid
       :param num: 需要取多少个uid
       :return:
       """
    SQL = Mysqldb()
    # 130000-135000之间是机器人,不能用，否则无法进入空房间，因为机器人不会主动创建房间
    # result = SQL.get_custom("pppoker", "select uid from user where nickname like '%kk%' and (uid<130000 or uid>135000)")
    result = SQL.get_custom("pppoker", "select uid from register_user where pw_encode ='c685847be4692a061bc5810633437875'")
    user_list = list(result)
    uid_list = []
    wl = get_whitelist()
    while num > 0:
        user = user_list.pop(random.randint(0, len(user_list) - 1))
        if user[0] in wl:
            continue
        uid_list.append(user[0])
        num -= 1
    return uid_list

def get_random_device():
    """
    生成随机设备号
    :return:
    """
    numbers = []
    char_list = ['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in range(1,7):
        numbers.append(random.choice(char_list) + random.choice(char_list))
    device = "{}-{}-{}-{}-{}-{}".format(*numbers)
    return device

def get_random_ip():
    """
    生成随机IP
    :return:
    """
    numbers = []
    for x in range(1,5):
        numbers.append(random.randint(1, 256))
    device = "{}.{}.{}.{}".format(*numbers)
    return device

def load_proto(pb):
    if project == 0:
        dir_name = 'kkt'
    elif project == 1:
        dir_name = 'kkc'
    elif project == 2:
        dir_name = 'tph'
    else:
        raise Exception("未定义的项目编号")

    path = os.path.dirname(os.path.dirname(__file__)) + "/proto/" + dir_name
    sys.path.append(path)  # 把协议文档目录加入到path,不然import的时候找不到模块
    # 把协议文件读入内存
    for name in os.listdir(path):
        if name == '__init__.py' or name[-3:] != '.py':
            continue
        module = importlib.import_module("proto.{}.".format(dir_name) + name[:-3])
        for item in dir(module):
            pb[item] = getattr(module, item)


