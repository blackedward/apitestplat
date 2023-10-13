from request_case import Api
from common.systemlog import logger


class testTT:
    def __init__(self):
        self.url = "https://bbs.hupu.com/api/v2/reply/reply?tid=62345450&pid=79097&maxpid=0"
        self.method = "GET"
        self.params = 'tid=62345250&pid=79097&maxpid=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    def testapi(self):
        api = Api(url=self.url,
                  method=self.method,
                  params=self.params,
                  headers=self.headers)
        json = api.getJson()
        spend = api.spend()
        logger.info(json)
        logger.info(spend)


if __name__ == '__main__':
    dest = {"tid": 62372594, "pid": 27479, "maxpid": 0}
    ise={"ds":"tid","dsevla":200}

    if ise['ds'] in dest:
        dest.replace(ise['ds'],ise['dsevla'])
    print(dest)
