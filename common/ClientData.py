class ClientData(object):
    def __init__(self):
        # 当前机器人曾经进入过的房间信息
        self.rooms = {}
        self.joined_rooms = []
