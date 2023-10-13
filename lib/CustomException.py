# coding;utf-8

class TimeOutException(Exception):
    def __init__(self, err='time out'):
        Exception.__init__(self, err)
