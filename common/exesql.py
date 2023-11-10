from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ExeSql(object):
    def __init__(self, db_url):
        self.engine = create_engine(db_url, echo=False, max_overflow=5)
        self.session = sessionmaker(bind=self.engine)()

    def exe_sql(self, sql):
        conn = self.engine.connect()
        conn.execute(sql)
        conn.close()
        # emp_json_list = [dict(zip(item.keys(), item)) for item in result]
        # return emp_json_list
