import gevent
import traceback
import logging
import socket
import errno
import time
from lib.Functor import bind
from lib import DataProcesser
from gevent import Timeout
logger = logging.getLogger()

def process(item):
    while True:
        is_broken = False
        try:
            data = item['socket'].recv(1024)
            if data:
                if 'data' in item:
                    DataProcesser.add(bind(item['data'], 0, data))
            else:
                is_broken = True
        except gevent._socketcommon.cancel_wait_ex:
            is_broken = True
        except BaseException:
            logger.error(traceback.format_exc())
            is_broken = True
        if is_broken:
            if 'error' in item:
                DataProcesser.add(item['error'])
            break

def add(item):
    gevent.spawn(process, item)
