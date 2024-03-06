from flask_login import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from datetime import datetime


class Permisson:
    ADD = 0x01
    EDIT = 0x02
    DELETE = 0x04
    ONEADMIN = 0x08
    ADMIN = 0xff


class User(db.Model):
    __tablename__ = 't_user'
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    job_number = db.Column(db.String(10))
    is_enable = db.Column(db.Boolean(), default=True)
    created_time = db.Column(db.DateTime(), default=datetime.now())
    update_time = db.Column(db.DateTime(), default=datetime.now())
    real_name = db.Column(db.String(20))
    role_id = db.Column(db.Integer())
    project = db.relationship('Project', backref='users', lazy='dynamic')
    interfacecase = db.relationship('InterfaceCase', backref='users', lazy='dynamic')
    interfacesuite = db.relationship('TestSuite', backref='users', lazy='dynamic')


    def __repr__(self):
        # return str(self.user_id) + self.username

        return self.username

    def is_administrator(self):
        return self.can(Permisson.ADMIN)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Project(db.Model):
    __tablename__ = 't_projects'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    project_user_id = db.Column(db.Integer(), db.ForeignKey('t_user.user_id'))
    project_name = db.Column(db.String(252), unique=True)
    product = db.Column(db.String(50))
    status = db.Column(db.Boolean(), default=True)
    Interfacehuan = db.relationship('Environment', backref='projects', lazy='dynamic')
    Interfacesuite = db.relationship('TestSuite', backref='projects', lazy='dynamic')
    model = db.relationship('Model', backref='projects', lazy='dynamic')
    interfacecase = db.relationship('InterfaceCase', backref='projects', lazy='dynamic')

    def __repr__(self):
        return self.project_name

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Environment(db.Model):  # 环境管理
    __tablename__ = 't_environment'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    make_user = db.Column(db.Integer(), db.ForeignKey('t_user.user_id'))
    url = db.Column(db.String(252))  # 地址
    port = db.Column(db.String(252))  # 端口
    protocol = db.Column(db.String(252))  # 协议
    desc = db.Column(db.String(252))  # 描述
    project = db.Column(db.Integer(), db.ForeignKey('t_projects.id'))  # 环境对应的项目
    status = db.Column(db.Boolean(), default=True)  # 状态

    # testcaseresult = db.relationship('TestcaseResult', backref='ceshihuanjing',
    #                                  lazy='dynamic')
    # task = db.relationship('Task', backref='ceshihuanjing',
    #                        lazy='dynamic')

    def __repr__(self):
        return str(self.id)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Model(db.Model):  # 模块，接口是根据模块来划分的
    __tablename__ = 't_models'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_name = db.Column(db.String(256))
    model_user_id = db.Column(db.Integer(), db.ForeignKey('t_user.user_id'))
    # Interfacetest = db.relationship('InterfaceTest', backref='models', lazy='dynamic')
    # Interface = db.relationship('Interface', backref='models', lazy='dynamic')
    status = db.Column(db.Boolean(), default=False)
    project = db.Column(db.Integer(), db.ForeignKey('t_projects.id'))
    interfacecase = db.relationship('InterfaceCase', backref='models', lazy='dynamic')

    def __repr__(self):
        return self.model_name

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Dbconf(db.Model):  # 数据源中心的配置
    __tablename__ = 't_db'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    db_name = db.Column(db.String(20))
    type = db.Column(db.Integer())
    desc = db.Column(db.String(100))
    url = db.Column(db.String(200))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    status = db.Column(db.Boolean(), default=True)
    test_url = db.Column(db.String(200))
    test_username = db.Column(db.String(100))
    test_password = db.Column(db.String(100))
    dev_url = db.Column(db.String(200))
    dev_username = db.Column(db.String(100))
    dev_password = db.Column(db.String(100))
    stg_url = db.Column(db.String(200))
    stg_username = db.Column(db.String(100))
    stg_password = db.Column(db.String(100))
    prod_url = db.Column(db.String(200))
    prod_username = db.Column(db.String(100))
    prod_password = db.Column(db.String(100))
    datafactory = db.relationship('DataFactory', backref='dbconf', lazy='dynamic')

    def __repr__(self):
        return self.id

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class DataFactory(db.Model):  # 数据源中心的数据工厂
    __tablename__ = 't_datafactory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dbfac_name = db.Column(db.String(100))
    type = db.Column(db.Integer())
    times = db.Column(db.Integer())
    failed_stop = db.Column(db.Boolean(), default=True)
    sql_run_dev = db.Column(db.Integer())
    sql_db_id = db.Column(db.Integer(), db.ForeignKey('t_db.id'))
    sql_str = db.Column(db.Text(65536))
    interfacecase = db.relationship('InterfaceCase', backref='datafactory', lazy='dynamic')
    # interface_suite_id = db.Column(db.Integer(), db.ForeignKey('t_interface_suite.id'))
    # ui_suite_id = db.Column(db.Integer(), db.ForeignKey('t_ui_suite.id'))
    execute_type = db.Column(db.Integer())

    def __repr__(self):
        return self.id

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class InterfaceCase(db.Model):
    __tablename__ = 't_interface_case'
    case_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('t_projects.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('t_models.id'))
    case_protocol = db.Column(db.Integer)
    is_relycase = db.Column(db.Boolean(), default=False)
    rely_dbf = db.Column(db.Integer, db.ForeignKey('t_datafactory.id'))
    url = db.Column(db.String(255))
    method = db.Column(db.Integer)
    desc = db.Column(db.String(1000))
    headers = db.Column(db.Text(65536))
    params = db.Column(db.Text(65536))
    form_data_encoded = db.Column(db.Text(65536))
    form_data = db.Column(db.Text(65536))
    socketreq = db.Column(db.String(255))
    socketrsp = db.Column(db.String(255))
    raw = db.Column(db.Text(65536))
    raw_type = db.Column(db.String(20))
    body_type = db.Column(db.Integer)
    creater = db.Column(db.Integer, db.ForeignKey('t_user.user_id'))
    created_time = db.Column(db.DateTime(), default=datetime.now())
    update_time = db.Column(db.DateTime(), default=datetime.now())
    source = db.Column(db.Integer)
    import_no = db.Column(db.Integer)
    status = db.Column(db.Boolean(), default=True)
    case_assert = db.relationship('InterfaceCaseAssert', backref='interfacecase', lazy='dynamic')
    precase = db.relationship('Precase', backref='interfacecase', lazy='dynamic')

    def __repr__(self):
        return self.id

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class InterfaceCaseAssert(db.Model):
    __tablename__ = 't_interface_assert'
    assert_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assert_name = db.Column(db.String(100))
    case_id = db.Column(db.Integer, db.ForeignKey('t_interface_case.case_id'))
    type = db.Column(db.Integer)
    expression = db.Column(db.String(50))
    operator = db.Column(db.Integer)
    excepted_result = db.Column(db.String(1000))
    order = db.Column(db.Integer)
    status = db.Column(db.Boolean(), default=True)
    created_time = db.Column(db.DateTime(), default=datetime.now())
    update_time = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return self.assert_name

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Precase(db.Model):
    __tablename__ = 't_interface_pre_case'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_case_id = db.Column(db.Integer, db.ForeignKey('t_interface_case.case_id'))
    extract_expression = db.Column(db.String(255))
    pre_case_id = db.Column(db.Integer)
    order = db.Column(db.Integer)
    status = db.Column(db.Boolean(), default=True)
    created_time = db.Column(db.DateTime(), default=datetime.now())
    update_time = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return str(self.id)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class TestcaseResult(db.Model):  # 测试用例结果
    __tablename__ = 't_testcase_results'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('t_interface_case.case_id'), nullable=True)
    result = db.Column(db.Text(65536))
    ispass = db.Column(db.Boolean(), default=False)
    spend = db.Column(db.String(52))
    date = db.Column(db.DateTime, default=datetime.now())
    testevent_id = db.Column(db.Integer, db.ForeignKey('t_environment.id'))

    def __repr__(self):
        return str(self.id)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class TestSuite(db.Model):  # 测试套件
    __tablename__ = 't_testsuite'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    creator = db.Column(db.Integer, db.ForeignKey('t_user.user_id'))
    project = db.Column(db.Integer, db.ForeignKey('t_projects.id'))
    caseids = db.Column(db.Text(255))
    status = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return str(self.id)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
