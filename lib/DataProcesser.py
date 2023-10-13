import gevent
import traceback
import logging
import time
logger = logging.getLogger()
functors = []


def process():
    start_time = time.time()
    while True:
        functor_num = len(functors)
        start_time = time.time()
        # logger.info('start')
        for i in range(functor_num):
            functor = functors.pop(0)
            try:
                functor()
            except BaseException:
                logger.error(traceback.format_exc())
        end_time = time.time()
        # logger.info("cost %f s, precess %d functors" % (end_time - start_time, functor_num))
        gevent.sleep(0)


def add(functor):
    functors.append(functor)


gevent.spawn(process)
