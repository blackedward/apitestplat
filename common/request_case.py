import json

from common.requestoper import requesttool
from common.systemlog import logger


class Api:
    def __init__(self, url, method, params, headers):
        self.url = url
        self.fangsh = method
        self.param = params
        self.headers = headers
        self.requ = requesttool()
        self.response = []

    def testapi(self):
        try:
            if self.fangsh == 'POST' or self.fangsh == 'post':

                response, spend = self.requ.post(url=self.url,
                                                 params=json.loads(self.param),
                                                 headers=json.loads(self.headers))

            elif self.fangsh == 'GET' or self.fangsh == 'get':
                if self.param is None or self.param == "":
                    response, spend = self.requ.get(url=self.url, headers=json.loads(self.headers))
                else:
                    response, spend = self.requ.get(url=self.url, headers=json.loads(self.headers),
                                                    parms=json.loads(self.param))
            elif self.fangsh == 'PUT' or self.fangsh == 'put':
                response, spend = self.requ.putfile(url=self.url, params=self.param, headers=self.headers)
            elif self.fangsh == 'DELETE' or self.fangsh == 'delete':
                response, spend = self.requ.delfile(url=self.url, params=self.param, headers=self.headers)
            else:
                response = ""
                spend = ""
            return response, spend
        except Exception as e:
            print(e)
            logger.exception(e)
            response = "请求出错了"
            spend = "错误"
            return response, spend

    def getJson(self):
        json_data, spend = self.testapi()
        return json_data

    def spend(self):
        json_data, spend = self.testapi()
        return spend

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
