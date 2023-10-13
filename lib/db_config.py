from config import *

'''
mysqldb 数据库配置
'''
#预发布
if SERVER_HOST == "pre.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306

#test1
elif SERVER_HOST == "beta10.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306


elif SERVER_HOST == "beta11.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306
elif SERVER_HOST == "beta12.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306
elif SERVER_HOST == "beta13.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306
#test1
elif SERVER_HOST == "beta14.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306
#test1
elif SERVER_HOST == "beta15.kkpoker.co":
        host = SERVER_HOST
        user = "dev"
        passwd = "jL4bTQf1"
        port = 3306

#aws
elif SERVER_HOST == "release.kkpoker.co":
        host = 'prod-mysql-pro.clmbkuendv5r.us-west-2.rds.amazonaws.com'
        user = "root"
        passwd = "meTRvr23"
        port = 3306

elif SERVER_HOST == "dev3.kkpoker.co":
        host = 'dev3.kkpoker.co'
        user = "dev"
        passwd = "123"
        port = 10204


else:
        host = "10.100.5.251"
        user = "ppdev"
        passwd = "e2f0b74118"
        port = 3306

'''
mongodb 数据库配置
'''
def get_mongodbconfig(database,table):
        mongodbconfig={}
        #预发布
        if SERVER_HOST == "47.91.249.89":
                if (database == "playing") or (database == "record" and (table not in ["user_game_record", "game_record"])):
                        host = "47.91.249.89"
                        port = 27017
                        user = "ppbeta_record_rw"
                        password = "163.com"
                elif database == "record" and (table in ["user_game_record", "game_record"]):
                        host = "47.91.249.89"
                        port = 27017
                        user = "ppbeta_record_rw"
                        password = "163.com"
        elif SERVER_HOST == "47.89.53.159":
                if (database == "playing"):
                        host = "47.244.78.224"
                        port = 27019
                        user = "pokerread"
                        password = "pre26c1031f76"
                elif database == "record" and (table in ["user_game_record", "game_record"]):
                        host = "47.75.211.2"
                        port = 27017
                        user = "pre_record_rw"
                        password = "3d204942ab"
                elif database == "record":
                        host = "47.89.53.159"
                        port = 27017
                        user = "pokerread"
                        password = "pre26c1031f76"

        mongodbconfig['host']=host
        mongodbconfig['port']=port
        mongodbconfig['user']=user
        mongodbconfig['password'] = password
        return mongodbconfig



