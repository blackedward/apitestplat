# coding:utf-8
import gevent
from common.log import logger


class Handler(object):
    def __init__(self, func, *args, **kwargs):
        self._Func = func
        self._Args = args
        self._Kwargs = kwargs

    def __call__(self, client, msg):
        logger.debug("uid:{}|调用处理器:{}".format(client.uid, self._Func))
        gevent.spawn(self._Func, client, msg, *self._Args, **self._Kwargs)

