from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.log import logger


class ExeSql(object):
    def __init__(self, db_url):
        self.engine = create_engine(db_url, echo=False, max_overflow=5)
        self.session = sessionmaker(bind=self.engine)()

    def exe_sql(self, sql):
        conn = self.engine.connect()
        try:
            result = conn.execute(sql)
            if result.returns_rows:
                data = result.fetchall()
                result.close()
                return data
            else:
                rowcount = result.rowcount
                result.close()
                return rowcount
        except Exception as e:
            logger.error(f"SQL execution failed: {str(e)}")
            return None
        finally:
            conn.close()

        # emp_json_list = [dict(zip(item.keys(), item)) for item in result]
        # return emp_json_list
