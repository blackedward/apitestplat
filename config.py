Interface_Time_Out = 5000  # 超时时间
loglevel = 'INFO'  # 日志输出级别 # DEBUG，INFO，WARNING，ERROR，CRITICAL

# 旧服务没有roomid,报文长度不太一样,需要设置为True
is_old_server = False
is_security = False
CLIENT_VERSION = '3.19.1000'

# --0代表普通版本 1代表企业版本
G_Distributor = "0"
G_SubDistributor = "0"
EMAIL_LOGIN_TYPE = 4

# beta10 test1
SERVER_HOST = "beta12.kkpoker.co"
TOOLBOX_WEB_HOST = "172.31.24.34"
PORT = 4000
PORT_BACKOFFICE = 8081


class BaseConfig(object):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://!1025@localhost:3306/Ktest?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'production&*12808@$!3'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = 'redis://localhost:6379/0'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://@localhost:3306/Ktest?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'development&*5290123'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = 'redis://localhost:6379/0'


class TestingConfig(BaseConfig):
    pass
