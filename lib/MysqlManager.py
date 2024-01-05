import pymysql
from common.log import logger
from lib.db_config import *


class Mysqldb(object):
    '''mysql管理器'''

    def __init__(self,charset='utf8'):
        '''初始化数据库'''
        self.__user = user
        self.__passwd = passwd
        self.__host = host
        self.__port = port
        self.__charset = charset
        self.__connect = None
        self.__cursor = None

    def _connect_db(self,db):
        """
        dbManager._connect_db()
        连接数据库
        """
        params = {
            "db": db,
            "user": self.__user,
            "passwd": self.__passwd,
            "host": self.__host,
            "port": self.__port,
            "charset": self.__charset
        }
        # self.db = pymysql.connect()
        self.__connect= pymysql.connect(**params)
        self.__cursor = self.__connect.cursor()

    def _close_db(self):
        '''
        dbManager._close_db()
        关闭数据库
        '''
        self.__cursor.close()
        self.__connect.close()

    def insert(self,db, table, insert_data):
        '''
        dbManager.insert(table, insert_data)
        添加数据到数据库
        str -> table 为字符串
        [{},{}] -> 为列表中嵌套字典类型
        '''
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db(db)


        try:
            if len(insert_data) == 1:
                for key in insert_data:
                    values= insert_data[key]
                sql = "insert into {table} values ({val})".format(table=table, val=values)
                logger.info(sql)
            else:
                # 提取插入的字段
                key = ','.join(insert_data.keys())
                # 提取插入的值
                values = '.'.join(['%s'] * len(insert_data))
                # 构建sql语句
                sql = "insert into {table}({key}) values {val}".format(table=table, key=key,val=tuple(insert_data.values()))
                logger.info(sql)
            try:
                if self.__cursor.execute(sql):
                    logger.info('insert successful')
                    self.__connect.commit()
            except:
                logger.info('insert failed')
        except Exception as error:
            logger.error(error)
        finally:
            self._close_db()

    def delete(self,db,table, condition):
        '''
            dbManager.delete(table, condition)
        删除数据库中的数据
        str -> table 字符串类型
        dict -> condition 字典类型
        '''
        self._connect_db(db)

        # 处理删除的条件
        condition_list = self._deal_values(condition)
        condition_data = ' and '.join(condition_list)

        # 构建sql语句
        sql = "delete from {table} where {condition}".format(table=table, condition=condition_data)

        self.__cursor.execute(sql)
        self.__connect.commit()
        self._close_db()

    def update(self,db,table, data, condition=None):
        """
            dbManager.update(table, data, [condition])
        更新数据
        str -> table 字符串类型
        dict -> data 字典类型
        dict -> condition 字典类型
        """
        self._connect_db(db)

        # 处理传入的数据
        update_list = self._deal_values(data)
        update_data = ",".join(update_list)
        # 判断是否有条件
        if condition is not None:
            # 处理传入的条件
            condition_list = self._deal_values(condition)
            condition_data = ' and '.join(condition_list)
            sql = "update {table} set {values} where {condition}".format(table=table, values=update_data,
                                                                         condition=condition_data)
        else:
            sql = "update {table} set {values}".format(table=table, values=update_data)
        self.__cursor.execute(sql)
        self.__connect.commit()
        self._close_db()

    def get(self,db,table, show_list, condition=None, get_one=False):
        """
        dbManager.get(table, show_list, [condition, get_one]) -> tupe
        获取数据 返回一个元祖
        str -> table 字符串类型
        list -> show_list 列表类型
        dict -> condition 字典类型
        boolean -> get_one 布尔类型

        """
        self._connect_db(db)

        # 处理显示的数据
        show_list = ",".join(show_list)
        sql = "select {key} from {table}".format(key=show_list, table=table)
        # 处理传入的条件
        if condition:
            condition_list = self._deal_values(condition)
            condition_data = ' and '.join(condition_list)
            sql = "select {key} from {table} where {condition}".format(key=show_list, table=table,condition=condition_data)
        self.__cursor.execute(sql)
        # 返回一条数据还是所有数据
        if get_one:
            result = self.__cursor.fetchone()
        else:
            result = self.__cursor.fetchall()
        self._close_db()
        return result

    def get_custom(self,db,sql,get_one=False):
        """
        :param db:数据库库名
        :param sql:需要执行的sql
        :param get_one: 是否只获取一条数据
        :return:
        """
        self._connect_db(db)
        # logger.info(sql)
        self.__cursor.execute(sql)
        # 返回一条数据还是所有数据
        if get_one:
            result = self.__cursor.fetchone()
        else:
            result = self.__cursor.fetchall()
        self._close_db()
        return result

    def _deal_values(self, value):
        """
        self._deal_values(value) -> str or list
            处理传进来的参数

        """
        # 如果是字符串则加上''
        if isinstance(value, str):
            value = ("'{value}'".format(value=value))
        # 如果是字典则变成key=value形式
        elif isinstance(value, dict):
            result = []
            for key, value in value.items():
                # value = self._deal_values(value)
                if isinstance(value, dict):
                    for condition, value in value.items():
                        if condition=="=":
                            if isinstance(value, str):
                                value = ("'{value}'".format(value=value))
                                res = "{key}={value}".format(key=key, condition=condition, value=value)
                        else:
                            if isinstance(value, list):
                                value = [str(i) for i in value]
                                value = '\"' + '\",\"'.join(value) + '\"'
                                res = "{key} {condition} ({value})".format(key=key, condition=condition, value=value)
                            else:
                                if isinstance(value, str):
                                    value = ("'{value}'".format(value=value))
                                res = "{key} {condition} ({value})".format(key=key, condition=condition, value=value)
                else:
                    res = "{key}={value}".format(key=key, value=value)
                result.append(res)
            return result
        else:
            value = (str(value))
        return value

