# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mission_base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mission_base.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x12mission_base.proto\x12\x02pb*\x85\x05\n\x0fMissionGameType\x12\x1d\n\x19MISSION_GAME_TYPE_DEFAULT\x10\x00\x12\x1f\n\x1bMISSION_GAME_TYPE_UNLIMITED\x10\x01\x12\x19\n\x15MISSION_GAME_TYPE_NLH\x10\x02\x12\x1c\n\x18MISSION_GAME_TYPE_6_PLUS\x10\x03\x12\x19\n\x15MISSION_GAME_TYPE_PLO\x10\x04\x12\x19\n\x15MISSION_GAME_TYPE_OFC\x10\x05\x12\x1b\n\x17MISSION_GAME_TYPE_FLASH\x10\x06\x12\x1c\n\x18MISSION_GAME_TYPE_SPINUP\x10\x07\x12\x19\n\x15MISSION_GAME_TYPE_MTT\x10\x08\x12\x19\n\x15MISSION_GAME_TYPE_AOF\x10\t\x12\x1f\n\x1bMISSION_GAME_TYPE_FLASH_PLO\x10\n\x12&\n\"MISSION_GAME_TYPE_FLASH_NLH_6_PLUS\x10\x0b\x12#\n\x1fMISSION_GAME_TYPE_FLASH_NLH_AOF\x10\x0c\x12\x1d\n\x19MISSION_GAME_TYPE_MTT_NLH\x10\r\x12\x1d\n\x19MISSION_GAME_TYPE_MTT_AOF\x10\x0e\x12\x1d\n\x19MISSION_GAME_TYPE_MTT_PLO\x10\x0f\x12#\n\x1fMISSION_GAME_TYPE_ALL_RING_GAME\x10\x10\x12$\n MISSION_GAME_TYPE_ALL_TOURNAMENT\x10\x11\x12\x1d\n\x19MISSION_GAME_TYPE_AOF_PLO\x10\x12\x12\x1d\n\x19MISSION_GAME_TYPE_SK_FLIP\x10\x13*\xc6\x02\n\x11MissionRewardType\x12\x1a\n\x16MISSION_REWARD_DEFAULT\x10\x00\x12\x18\n\x14MISSION_REWARD_MONEY\x10\x01\x12\x18\n\x14MISSION_REWARD_POINT\x10\x02\x12\x17\n\x13MISSION_REWARD_ITEM\x10\x03\x12\x1b\n\x17MISSION_REWARD_GIFT_BAG\x10\x04\x12\x16\n\x12MISSION_REWARD_VIP\x10\x05\x12\x1b\n\x17MISSION_REWARD_ITEM_SET\x10\x06\x12\x18\n\x14MISSION_REWARD_WHEEL\x10\x07\x12\x1d\n\x19MISSION_REWARD_BLIND_COIN\x10\x08\x12\x1f\n\x1bMISSION_REWARD_AVATAR_FRAME\x10\t\x12\x1c\n\x18MISSION_REWARD_CASH_BACK\x10\n*\x90\x01\n\x1bMissionGroupFetchRewardType\x12&\n\"MISSION_GROUP_FETCH_REWARD_DEFAULT\x10\x00\x12$\n MISSION_GROUP_FETCH_REWARD_ORDER\x10\x01\x12#\n\x1fMISSION_GROUP_FETCH_REWARD_LIST\x10\x02*\xb9\x01\n\x10MissionGroupType\x12\x19\n\x15MISSION_GROUP_DEFAULT\x10\x00\x12\x19\n\x15MISSION_GROUP_MISSION\x10\x01\x12\x1d\n\x19MISSION_GROUP_LOGIN_BONUS\x10\x02\x12\x1f\n\x1bMISSION_GROUP_DAILY_MISSION\x10\x03\x12/\n+MISSION_GROUP_FIXED_FIRST_DAY_DAILY_MISSION\x10\x04*\xa5\x01\n\x17MissionGroupExpiredType\x12!\n\x1dMISSION_GROUP_EXPIRED_UNLIMIT\x10\x00\x12\'\n#MISSION_GROUP_EXPIRED_REWARD_NUMBER\x10\x01\x12\x1e\n\x1aMISSION_GROUP_EXPIRED_DAYS\x10\x02\x12\x1e\n\x1aMISSION_GROUP_EXPIRED_DATE\x10\x03*\xc6\x07\n\x12MissionContentType\x12 \n\x1cMISSION_CONTENT_TYPE_DEFAULT\x10\x00\x12\x1d\n\x19MISSION_CONTENT_TYPE_HAND\x10\x01\x12\x1d\n\x19MISSION_CONTENT_TYPE_GAME\x10\x02\x12!\n\x1dMISSION_CONTENT_TYPE_ADD_CLUB\x10\x03\x12+\n\'MISSION_CONTENT_TYPE_SUBMIT_KYC_LEVEL_1\x10\x04\x12!\n\x1dMISSION_CONTENT_TYPE_COMPLETE\x10\x05\x12+\n\'MISSION_CONTENT_TYPE_SUBMIT_KYC_LEVEL_2\x10\x06\x12-\n)MISSION_CONTENT_TYPE_COMPLETE_KYC_LEVEL_2\x10\x07\x12\'\n#MISSION_CONTENT_TYPE_PROMOTION_LINK\x10\x08\x12-\n)MISSION_CONTENT_TYPE_COMPLETE_KYC_LEVEL_1\x10\t\x12#\n\x1fMISSION_CONTENT_TYPE_FREE_CLAIM\x10\n\x12)\n%MISSION_CONTENT_TYPE_GAME_AT_ONE_HAND\x10\x0b\x12&\n\"MISSION_CONTENT_TYPE_FIRST_DEPOSIT\x10\x0c\x12 \n\x1cMISSION_CONTENT_TYPE_DEPOSIT\x10\r\x12$\n MISSION_CONTENT_TYPE_LOGIN_BONUS\x10\x0e\x12!\n\x1dMISSION_CONTENT_TYPE_WIN_HAND\x10\x0f\x12\x30\n,MISSION_CONTENT_TYPE_PLAY_WITH_SPECIAL_HANDS\x10\x10\x12\x32\n.MISSION_CONTENT_TYPE_PLAY_HANDS_GO_TO_SHOWDOWN\x10\x11\x12-\n)MISSION_CONTENT_TYPE_WINNINGS_ACCUMULATED\x10\x12\x12*\n&MISSION_CONTENT_TYPE_SPINUP_MULTIPLIER\x10\x13\x12%\n!MISSION_CONTENT_TYPE_RAKEBACK_EXP\x10\x14\x12\x34\n0MISSION_CONTENT_TYPE_WINNINGS_ACCUMULATED_CASINO\x10\x15\x12(\n$MISSION_CONTENT_TYPE_BET_ACCUMULATED\x10\x16\x42\x07Z\x05../pb')
)

_MISSIONGAMETYPE = _descriptor.EnumDescriptor(
  name='MissionGameType',
  full_name='pb.MissionGameType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_UNLIMITED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_NLH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_6_PLUS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_PLO', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_OFC', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_FLASH', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_SPINUP', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_MTT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_AOF', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_FLASH_PLO', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_FLASH_NLH_6_PLUS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_FLASH_NLH_AOF', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_MTT_NLH', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_MTT_AOF', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_MTT_PLO', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_ALL_RING_GAME', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_ALL_TOURNAMENT', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_AOF_PLO', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GAME_TYPE_SK_FLIP', index=19, number=19,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=27,
  serialized_end=672,
)
_sym_db.RegisterEnumDescriptor(_MISSIONGAMETYPE)

MissionGameType = enum_type_wrapper.EnumTypeWrapper(_MISSIONGAMETYPE)
_MISSIONREWARDTYPE = _descriptor.EnumDescriptor(
  name='MissionRewardType',
  full_name='pb.MissionRewardType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_MONEY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_POINT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_ITEM', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_GIFT_BAG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_VIP', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_ITEM_SET', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_WHEEL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_BLIND_COIN', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_AVATAR_FRAME', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_REWARD_CASH_BACK', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=675,
  serialized_end=1001,
)
_sym_db.RegisterEnumDescriptor(_MISSIONREWARDTYPE)

MissionRewardType = enum_type_wrapper.EnumTypeWrapper(_MISSIONREWARDTYPE)
_MISSIONGROUPFETCHREWARDTYPE = _descriptor.EnumDescriptor(
  name='MissionGroupFetchRewardType',
  full_name='pb.MissionGroupFetchRewardType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_FETCH_REWARD_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_FETCH_REWARD_ORDER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_FETCH_REWARD_LIST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1004,
  serialized_end=1148,
)
_sym_db.RegisterEnumDescriptor(_MISSIONGROUPFETCHREWARDTYPE)

MissionGroupFetchRewardType = enum_type_wrapper.EnumTypeWrapper(_MISSIONGROUPFETCHREWARDTYPE)
_MISSIONGROUPTYPE = _descriptor.EnumDescriptor(
  name='MissionGroupType',
  full_name='pb.MissionGroupType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_MISSION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_LOGIN_BONUS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_DAILY_MISSION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_FIXED_FIRST_DAY_DAILY_MISSION', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1151,
  serialized_end=1336,
)
_sym_db.RegisterEnumDescriptor(_MISSIONGROUPTYPE)

MissionGroupType = enum_type_wrapper.EnumTypeWrapper(_MISSIONGROUPTYPE)
_MISSIONGROUPEXPIREDTYPE = _descriptor.EnumDescriptor(
  name='MissionGroupExpiredType',
  full_name='pb.MissionGroupExpiredType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_EXPIRED_UNLIMIT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_EXPIRED_REWARD_NUMBER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_EXPIRED_DAYS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_GROUP_EXPIRED_DATE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1339,
  serialized_end=1504,
)
_sym_db.RegisterEnumDescriptor(_MISSIONGROUPEXPIREDTYPE)

MissionGroupExpiredType = enum_type_wrapper.EnumTypeWrapper(_MISSIONGROUPEXPIREDTYPE)
_MISSIONCONTENTTYPE = _descriptor.EnumDescriptor(
  name='MissionContentType',
  full_name='pb.MissionContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_HAND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_GAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_ADD_CLUB', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_SUBMIT_KYC_LEVEL_1', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_COMPLETE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_SUBMIT_KYC_LEVEL_2', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_COMPLETE_KYC_LEVEL_2', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_PROMOTION_LINK', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_COMPLETE_KYC_LEVEL_1', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_FREE_CLAIM', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_GAME_AT_ONE_HAND', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_FIRST_DEPOSIT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_DEPOSIT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_LOGIN_BONUS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_WIN_HAND', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_PLAY_WITH_SPECIAL_HANDS', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_PLAY_HANDS_GO_TO_SHOWDOWN', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_WINNINGS_ACCUMULATED', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_SPINUP_MULTIPLIER', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_RAKEBACK_EXP', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_WINNINGS_ACCUMULATED_CASINO', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CONTENT_TYPE_BET_ACCUMULATED', index=22, number=22,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1507,
  serialized_end=2473,
)
_sym_db.RegisterEnumDescriptor(_MISSIONCONTENTTYPE)

MissionContentType = enum_type_wrapper.EnumTypeWrapper(_MISSIONCONTENTTYPE)
MISSION_GAME_TYPE_DEFAULT = 0
MISSION_GAME_TYPE_UNLIMITED = 1
MISSION_GAME_TYPE_NLH = 2
MISSION_GAME_TYPE_6_PLUS = 3
MISSION_GAME_TYPE_PLO = 4
MISSION_GAME_TYPE_OFC = 5
MISSION_GAME_TYPE_FLASH = 6
MISSION_GAME_TYPE_SPINUP = 7
MISSION_GAME_TYPE_MTT = 8
MISSION_GAME_TYPE_AOF = 9
MISSION_GAME_TYPE_FLASH_PLO = 10
MISSION_GAME_TYPE_FLASH_NLH_6_PLUS = 11
MISSION_GAME_TYPE_FLASH_NLH_AOF = 12
MISSION_GAME_TYPE_MTT_NLH = 13
MISSION_GAME_TYPE_MTT_AOF = 14
MISSION_GAME_TYPE_MTT_PLO = 15
MISSION_GAME_TYPE_ALL_RING_GAME = 16
MISSION_GAME_TYPE_ALL_TOURNAMENT = 17
MISSION_GAME_TYPE_AOF_PLO = 18
MISSION_GAME_TYPE_SK_FLIP = 19
MISSION_REWARD_DEFAULT = 0
MISSION_REWARD_MONEY = 1
MISSION_REWARD_POINT = 2
MISSION_REWARD_ITEM = 3
MISSION_REWARD_GIFT_BAG = 4
MISSION_REWARD_VIP = 5
MISSION_REWARD_ITEM_SET = 6
MISSION_REWARD_WHEEL = 7
MISSION_REWARD_BLIND_COIN = 8
MISSION_REWARD_AVATAR_FRAME = 9
MISSION_REWARD_CASH_BACK = 10
MISSION_GROUP_FETCH_REWARD_DEFAULT = 0
MISSION_GROUP_FETCH_REWARD_ORDER = 1
MISSION_GROUP_FETCH_REWARD_LIST = 2
MISSION_GROUP_DEFAULT = 0
MISSION_GROUP_MISSION = 1
MISSION_GROUP_LOGIN_BONUS = 2
MISSION_GROUP_DAILY_MISSION = 3
MISSION_GROUP_FIXED_FIRST_DAY_DAILY_MISSION = 4
MISSION_GROUP_EXPIRED_UNLIMIT = 0
MISSION_GROUP_EXPIRED_REWARD_NUMBER = 1
MISSION_GROUP_EXPIRED_DAYS = 2
MISSION_GROUP_EXPIRED_DATE = 3
MISSION_CONTENT_TYPE_DEFAULT = 0
MISSION_CONTENT_TYPE_HAND = 1
MISSION_CONTENT_TYPE_GAME = 2
MISSION_CONTENT_TYPE_ADD_CLUB = 3
MISSION_CONTENT_TYPE_SUBMIT_KYC_LEVEL_1 = 4
MISSION_CONTENT_TYPE_COMPLETE = 5
MISSION_CONTENT_TYPE_SUBMIT_KYC_LEVEL_2 = 6
MISSION_CONTENT_TYPE_COMPLETE_KYC_LEVEL_2 = 7
MISSION_CONTENT_TYPE_PROMOTION_LINK = 8
MISSION_CONTENT_TYPE_COMPLETE_KYC_LEVEL_1 = 9
MISSION_CONTENT_TYPE_FREE_CLAIM = 10
MISSION_CONTENT_TYPE_GAME_AT_ONE_HAND = 11
MISSION_CONTENT_TYPE_FIRST_DEPOSIT = 12
MISSION_CONTENT_TYPE_DEPOSIT = 13
MISSION_CONTENT_TYPE_LOGIN_BONUS = 14
MISSION_CONTENT_TYPE_WIN_HAND = 15
MISSION_CONTENT_TYPE_PLAY_WITH_SPECIAL_HANDS = 16
MISSION_CONTENT_TYPE_PLAY_HANDS_GO_TO_SHOWDOWN = 17
MISSION_CONTENT_TYPE_WINNINGS_ACCUMULATED = 18
MISSION_CONTENT_TYPE_SPINUP_MULTIPLIER = 19
MISSION_CONTENT_TYPE_RAKEBACK_EXP = 20
MISSION_CONTENT_TYPE_WINNINGS_ACCUMULATED_CASINO = 21
MISSION_CONTENT_TYPE_BET_ACCUMULATED = 22


DESCRIPTOR.enum_types_by_name['MissionGameType'] = _MISSIONGAMETYPE
DESCRIPTOR.enum_types_by_name['MissionRewardType'] = _MISSIONREWARDTYPE
DESCRIPTOR.enum_types_by_name['MissionGroupFetchRewardType'] = _MISSIONGROUPFETCHREWARDTYPE
DESCRIPTOR.enum_types_by_name['MissionGroupType'] = _MISSIONGROUPTYPE
DESCRIPTOR.enum_types_by_name['MissionGroupExpiredType'] = _MISSIONGROUPEXPIREDTYPE
DESCRIPTOR.enum_types_by_name['MissionContentType'] = _MISSIONCONTENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
