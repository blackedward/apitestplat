# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pre_base.proto

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
  name='pre_base.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x0epre_base.proto\x12\x02pb\"z\n\x13RewardConfigureItem\x12\x0f\n\x07ranking\x18\x01 \x01(\x05\x12\x18\n\x0cranking_nums\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x10\n\x04name\x18\x03 \x01(\tB\x02\x18\x01\x12\r\n\x05value\x18\x04 \x01(\x05\x12\x17\n\x0b\x65xpire_time\x18\x05 \x01(\x03\x42\x02\x18\x01*\xf2\x02\n\nActionType\x12\x0f\n\x0b\x41\x43TION_NONE\x10\x00\x12\x0f\n\x0b\x41\x43TION_FOLD\x10\x01\x12\x10\n\x0c\x41\x43TION_CHECK\x10\x02\x12\x0f\n\x0b\x41\x43TION_CALL\x10\x03\x12\x10\n\x0c\x41\x43TION_RAISE\x10\x04\x12\x0f\n\x0b\x41\x43TION_WAIT\x10\x05\x12\x10\n\x0c\x41\x43TION_SITED\x10\x06\x12\x0e\n\nACTION_BET\x10\x07\x12\r\n\tACTION_SB\x10\x08\x12\r\n\tACTION_BB\x10\t\x12\x0f\n\x0b\x41\x43TION_ANTE\x10\n\x12\x13\n\x0f\x41\x43TION_FORCE_BB\x10\x0b\x12\x16\n\x12\x41\x43TION_SYSTEM_FOLD\x10\x0c\x12\x17\n\x13\x41\x43TION_SYSTEM_CHECK\x10\r\x12\x13\n\x0f\x41\x43TION_STRADDLE\x10\x0e\x12\x0e\n\nACTION_POT\x10\x0f\x12\x14\n\x10\x41\x43TION_FAST_FOLD\x10\x10\x12\x13\n\x0f\x41\x43TION_STAND_UP\x10\x12\x12\x15\n\x11\x41\x43TION_BOMBPOT_BB\x10\x13*\x9c\x01\n\rPreActionType\x12\x13\n\x0fPRE_ACTION_NONE\x10\x00\x12\x1c\n\x18PRE_ACTION_CHECK_OR_FOLD\x10\x01\x12\x14\n\x10PRE_ACTION_CHECK\x10\x02\x12\x13\n\x0fPRE_ACTION_CALL\x10\x03\x12\x17\n\x13PRE_ACTION_CALL_ANY\x10\x04\x12\x14\n\x10PRE_ACTION_ALLIN\x10\x05*\xbd\x01\n\x08RoomType\x12\r\n\tTEST_ROOM\x10\x00\x12\x10\n\x0cNLH_MTT_ROOM\x10\x02\x12\x10\n\x0cNLH_SNG_ROOM\x10\x03\x12\x0c\n\x08NLH_ROOM\x10\x05\x12\x0e\n\nOMAHA_ROOM\x10\x08\x12\r\n\tPINE_ROOM\x10\t\x12\x12\n\x0eOMAHA_SNG_ROOM\x10\n\x12\x12\n\x0eOMAHA_MTT_ROOM\x10\x0b\x12\x0f\n\x0bSPINUP_ROOM\x10\r\x12\x18\n\x14SHARK_KING_FLIP_ROOM\x10\x0e*2\n\x08RoomMode\x12\x12\n\x0eROOM_MODE_NONE\x10\x00\x12\x12\n\x0eROOM_MODE_CLUB\x10\x03*\xde\x06\n\x08GameMode\x12\x15\n\x11GAME_MODE_REGULAR\x10\x00\x12\x12\n\x0eGAME_MODE_ZOOM\x10\x0b\x12\x1d\n\x19GAME_MODE_ZOOM_NLH_6_PLUS\x10\x11\x12\x1e\n\x1aGAME_MODE_ZOOM_PLO_5_CARDS\x10\x12\x12\x1d\n\x19GAME_MODE_ZOOM_ALLIN_FOLD\x10\x13\x12\x18\n\x14GAME_MODE_NLH_6_PLUS\x10\x0c\x12\x19\n\x15GAME_MODE_PLO_5_CARDS\x10\n\x12#\n\x1eGAME_MODE_PLO_5_CARDS_CALLTIME\x10\xd2\x01\x12 \n\x1cGAME_MODE_PLO_5_CARDS_HUNTER\x10\x17\x12)\n%GAME_MODE_PLO_5_CARDS_SNOWBALL_HUNTER\x10\x18\x12\'\n#GAME_MODE_PLO_5_CARDS_MTT_SATELLITE\x10\x19\x12$\n GAME_MODE_PLO_5_CARDS_ALLIN_FOLD\x10\x1a\x12$\n GAME_MODE_PLO_4_CARDS_ALLIN_FOLD\x10\x1b\x12\x18\n\x14GAME_MODE_ALLIN_FOLD\x10\r\x12\x1f\n\x1bGAME_MODE_ALLIN_FOLD_HUNTER\x10\x14\x12(\n$GAME_MODE_ALLIN_FOLD_SNOWBALL_HUNTER\x10\x15\x12&\n\"GAME_MODE_ALLIN_FOLD_MTT_SATELLITE\x10\x16\x12\x1f\n\x1aGAME_MODE_REGULAR_CALLTIME\x10\xc8\x01\x12\x14\n\x10GAME_MODE_HUNTER\x10\x0e\x12\x1d\n\x19GAME_MODE_SNOWBALL_HUNTER\x10\x0f\x12\x1b\n\x17GAME_MODE_MTT_SATELLITE\x10\x10\x12\x1d\n\x19GAME_MODE_OFC_PROGRESSIVE\x10\x01\x12\x1a\n\x16GAME_MODE_OFC_ULTIMATE\x10\x02\x12#\n\x1fGAME_MODE_OFC_WILD_CARD_REGULAR\x10\x64\x12\'\n#GAME_MODE_OFC_WILD_CARD_PROGRESSIVE\x10\x65\x12$\n GAME_MODE_OFC_WILD_CARD_ULTIMATE\x10\x66*u\n\nRoundStage\x12\x0e\n\nROUND_NONE\x10\x00\x12\x12\n\x0eROUND_PRE_FLOP\x10\x01\x12\x0e\n\nROUND_FLOP\x10\x02\x12\x0e\n\nROUND_TURN\x10\x03\x12\x0f\n\x0bROUND_RIVER\x10\x04\x12\x12\n\x0eROUND_COMPLETE\x10\x05*)\n\tValueType\x12\x0c\n\x08INVAILID\x10\x00\x12\x0e\n\nUSER_MONEY\x10\x01*8\n\nPPCurrency\x12\x14\n\x10PP_CURRENCY_NONE\x10\x00\x12\x14\n\x10PP_CURRENCY_GOLD\x10\x01*\xc7\x01\n\x0eUserRoomAction\x12\x19\n\x15USER_ROOM_ACTION_NONE\x10\x00\x12\x1b\n\x17USER_ROOM_ACTION_SIGNUP\x10\x01\x12\"\n\x1eUSER_ROOM_ACTION_CANCEL_SIGNUP\x10\x02\x12\x1c\n\x18USER_ROOM_ACTION_SITDOWN\x10\x03\x12\x1c\n\x18USER_ROOM_ACTION_STANDUP\x10\x04\x12\x1d\n\x19USER_ROOM_ACTION_WITHDRAW\x10\x05*\x9d\x03\n\nBankerType\x12\x14\n\x10\x42\x41NKER_TYPE_NONE\x10\x00\x12\x15\n\x11\x42\x41NKER_TYPE_BUYIN\x10\x01\x12\x1b\n\x17\x42\x41NKER_TYPE_DELAY_BUYIN\x10\x02\x12\x15\n\x11\x42\x41NKER_TYPE_REBUY\x10\x03\x12\x15\n\x11\x42\x41NKER_TYPE_TOPUP\x10\x04\x12\x15\n\x11\x42\x41NKER_TYPE_ADDON\x10\x05\x12\x1b\n\x17\x42\x41NKER_TYPE_GAME_REWARD\x10\x06\x12\x1d\n\x19\x42\x41NKER_TYPE_HUNTER_REWARD\x10\x07\x12\x16\n\x12\x42\x41NKER_TYPE_REFUND\x10\x64\x12\x1e\n\x1a\x42\x41NKER_TYPE_JACKPOT_REWARD\x10\x08\x12\x17\n\x13\x42\x41NKER_TYPE_CASHOUT\x10\x65\x12\x1c\n\x18\x42\x41NKER_TYPE_CHANGE_TABLE\x10\x66\x12\x1e\n\x1a\x42\x41NKER_TYPE_WITHDRAW_CHIPS\x10g\x12\x16\n\x12\x42\x41NKER_TYPE_SIGNUP\x10h\x12\x1d\n\x19\x42\x41NKER_TYPE_CANCEL_SIGNUP\x10i*\x80\x02\n\x14MttRewardPercentType\x12\x13\n\x0fMTT_TEN_PERCENT\x10\x00\x12\x17\n\x13MTT_FIFTEEN_PERCENT\x10\x01\x12\x16\n\x12MTT_TWENTY_PERCENT\x10\x02\x12\x17\n\x13MTT_NEW_TEN_PERCENT\x10\x03\x12\x1b\n\x17MTT_NEW_FIFTEEN_PERCENT\x10\x04\x12\x1a\n\x16MTT_NEW_TWENTY_PERCENT\x10\x05\x12\x17\n\x13MTT_PKO_TEN_PERCENT\x10\x06\x12\x1b\n\x17MTT_PKO_FIFTEEN_PERCENT\x10\x07\x12\x1a\n\x16MTT_PKO_TWENTY_PERCENT\x10\x08*u\n\x11GameSetPlayStatus\x12\x1d\n\x19GAME_SET_PLAY_STATUS_NONE\x10\x00\x12 \n\x1cGAME_SET_PLAY_STATUS_PLAYING\x10\x01\x12\x1f\n\x1bGAME_SET_PLAY_STATUS_FINISH\x10\x64*\xe4\x01\n\x0eUserPlayStatus\x12\x1b\n\x17USER_PLAY_STATUS_NOT_IN\x10\x00\x12\x1b\n\x17USER_PLAY_STATUS_SIGNUP\x10\x01\x12\x1c\n\x18USER_PLAY_STATUS_PLAYING\x10\x02\x12\x1c\n\x18USER_PLAY_STATUS_STANDUP\x10\x03\x12\x1c\n\x18USER_PLAY_STATUS_SITTING\x10\x04\x12\x1b\n\x17USER_PLAY_STATUS_RETURN\x10\x05\x12!\n\x1dUSER_PLAY_STATUS_CHANGE_TABLE\x10\x06*\xc7\x01\n\tMttStatus\x12\x18\n\x14MTT_STATUS_NOT_START\x10\x01\x12\x19\n\x15MTT_STATUS_DELAY_JOIN\x10\x02\x12\x1e\n\x1aMTT_STATUS_STOP_DELAY_JOIN\x10\x03\x12\x17\n\x13MTT_STATUS_FINISHED\x10\x04\x12\x17\n\x13MTT_STATUS_HAS_DAY1\x10\x05\x12\x16\n\x12MTT_STATUS_NO_DAY1\x10\x06\x12\x1b\n\x17MTT_STATUS_ENDING_SCENE\x10\x07\x42\x07Z\x05../pb')
)

_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='pb.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_FOLD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_CHECK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_CALL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_RAISE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_WAIT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_SITED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_BET', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_SB', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_BB', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_ANTE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_FORCE_BB', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_SYSTEM_FOLD', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_SYSTEM_CHECK', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_STRADDLE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_POT', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_FAST_FOLD', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_STAND_UP', index=17, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_BOMBPOT_BB', index=18, number=19,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=147,
  serialized_end=517,
)
_sym_db.RegisterEnumDescriptor(_ACTIONTYPE)

ActionType = enum_type_wrapper.EnumTypeWrapper(_ACTIONTYPE)
_PREACTIONTYPE = _descriptor.EnumDescriptor(
  name='PreActionType',
  full_name='pb.PreActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRE_ACTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_ACTION_CHECK_OR_FOLD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_ACTION_CHECK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_ACTION_CALL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_ACTION_CALL_ANY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_ACTION_ALLIN', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=520,
  serialized_end=676,
)
_sym_db.RegisterEnumDescriptor(_PREACTIONTYPE)

PreActionType = enum_type_wrapper.EnumTypeWrapper(_PREACTIONTYPE)
_ROOMTYPE = _descriptor.EnumDescriptor(
  name='RoomType',
  full_name='pb.RoomType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEST_ROOM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NLH_MTT_ROOM', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NLH_SNG_ROOM', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NLH_ROOM', index=3, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OMAHA_ROOM', index=4, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PINE_ROOM', index=5, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OMAHA_SNG_ROOM', index=6, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OMAHA_MTT_ROOM', index=7, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPINUP_ROOM', index=8, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARK_KING_FLIP_ROOM', index=9, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=679,
  serialized_end=868,
)
_sym_db.RegisterEnumDescriptor(_ROOMTYPE)

RoomType = enum_type_wrapper.EnumTypeWrapper(_ROOMTYPE)
_ROOMMODE = _descriptor.EnumDescriptor(
  name='RoomMode',
  full_name='pb.RoomMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROOM_MODE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_MODE_CLUB', index=1, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=870,
  serialized_end=920,
)
_sym_db.RegisterEnumDescriptor(_ROOMMODE)

RoomMode = enum_type_wrapper.EnumTypeWrapper(_ROOMMODE)
_GAMEMODE = _descriptor.EnumDescriptor(
  name='GameMode',
  full_name='pb.GameMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_REGULAR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ZOOM', index=1, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ZOOM_NLH_6_PLUS', index=2, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ZOOM_PLO_5_CARDS', index=3, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ZOOM_ALLIN_FOLD', index=4, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_NLH_6_PLUS', index=5, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_5_CARDS', index=6, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_5_CARDS_CALLTIME', index=7, number=210,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_5_CARDS_HUNTER', index=8, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_5_CARDS_SNOWBALL_HUNTER', index=9, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_5_CARDS_MTT_SATELLITE', index=10, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_5_CARDS_ALLIN_FOLD', index=11, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_PLO_4_CARDS_ALLIN_FOLD', index=12, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ALLIN_FOLD', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ALLIN_FOLD_HUNTER', index=14, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ALLIN_FOLD_SNOWBALL_HUNTER', index=15, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_ALLIN_FOLD_MTT_SATELLITE', index=16, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_REGULAR_CALLTIME', index=17, number=200,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_HUNTER', index=18, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_SNOWBALL_HUNTER', index=19, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_MTT_SATELLITE', index=20, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_OFC_PROGRESSIVE', index=21, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_OFC_ULTIMATE', index=22, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_OFC_WILD_CARD_REGULAR', index=23, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_OFC_WILD_CARD_PROGRESSIVE', index=24, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_MODE_OFC_WILD_CARD_ULTIMATE', index=25, number=102,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=923,
  serialized_end=1785,
)
_sym_db.RegisterEnumDescriptor(_GAMEMODE)

GameMode = enum_type_wrapper.EnumTypeWrapper(_GAMEMODE)
_ROUNDSTAGE = _descriptor.EnumDescriptor(
  name='RoundStage',
  full_name='pb.RoundStage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROUND_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_PRE_FLOP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_FLOP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_TURN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_RIVER', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUND_COMPLETE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1787,
  serialized_end=1904,
)
_sym_db.RegisterEnumDescriptor(_ROUNDSTAGE)

RoundStage = enum_type_wrapper.EnumTypeWrapper(_ROUNDSTAGE)
_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='pb.ValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVAILID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_MONEY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1906,
  serialized_end=1947,
)
_sym_db.RegisterEnumDescriptor(_VALUETYPE)

ValueType = enum_type_wrapper.EnumTypeWrapper(_VALUETYPE)
_PPCURRENCY = _descriptor.EnumDescriptor(
  name='PPCurrency',
  full_name='pb.PPCurrency',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PP_CURRENCY_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PP_CURRENCY_GOLD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1949,
  serialized_end=2005,
)
_sym_db.RegisterEnumDescriptor(_PPCURRENCY)

PPCurrency = enum_type_wrapper.EnumTypeWrapper(_PPCURRENCY)
_USERROOMACTION = _descriptor.EnumDescriptor(
  name='UserRoomAction',
  full_name='pb.UserRoomAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_ROOM_ACTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_ROOM_ACTION_SIGNUP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_ROOM_ACTION_CANCEL_SIGNUP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_ROOM_ACTION_SITDOWN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_ROOM_ACTION_STANDUP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_ROOM_ACTION_WITHDRAW', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2008,
  serialized_end=2207,
)
_sym_db.RegisterEnumDescriptor(_USERROOMACTION)

UserRoomAction = enum_type_wrapper.EnumTypeWrapper(_USERROOMACTION)
_BANKERTYPE = _descriptor.EnumDescriptor(
  name='BankerType',
  full_name='pb.BankerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_BUYIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_DELAY_BUYIN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_REBUY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_TOPUP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_ADDON', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_GAME_REWARD', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_HUNTER_REWARD', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_REFUND', index=8, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_JACKPOT_REWARD', index=9, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_CASHOUT', index=10, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_CHANGE_TABLE', index=11, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_WITHDRAW_CHIPS', index=12, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_SIGNUP', index=13, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANKER_TYPE_CANCEL_SIGNUP', index=14, number=105,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2210,
  serialized_end=2623,
)
_sym_db.RegisterEnumDescriptor(_BANKERTYPE)

BankerType = enum_type_wrapper.EnumTypeWrapper(_BANKERTYPE)
_MTTREWARDPERCENTTYPE = _descriptor.EnumDescriptor(
  name='MttRewardPercentType',
  full_name='pb.MttRewardPercentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MTT_TEN_PERCENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_FIFTEEN_PERCENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_TWENTY_PERCENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_NEW_TEN_PERCENT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_NEW_FIFTEEN_PERCENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_NEW_TWENTY_PERCENT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_PKO_TEN_PERCENT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_PKO_FIFTEEN_PERCENT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_PKO_TWENTY_PERCENT', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2626,
  serialized_end=2882,
)
_sym_db.RegisterEnumDescriptor(_MTTREWARDPERCENTTYPE)

MttRewardPercentType = enum_type_wrapper.EnumTypeWrapper(_MTTREWARDPERCENTTYPE)
_GAMESETPLAYSTATUS = _descriptor.EnumDescriptor(
  name='GameSetPlayStatus',
  full_name='pb.GameSetPlayStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAME_SET_PLAY_STATUS_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_SET_PLAY_STATUS_PLAYING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_SET_PLAY_STATUS_FINISH', index=2, number=100,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2884,
  serialized_end=3001,
)
_sym_db.RegisterEnumDescriptor(_GAMESETPLAYSTATUS)

GameSetPlayStatus = enum_type_wrapper.EnumTypeWrapper(_GAMESETPLAYSTATUS)
_USERPLAYSTATUS = _descriptor.EnumDescriptor(
  name='UserPlayStatus',
  full_name='pb.UserPlayStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_NOT_IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_SIGNUP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_PLAYING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_STANDUP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_SITTING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_RETURN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_PLAY_STATUS_CHANGE_TABLE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3004,
  serialized_end=3232,
)
_sym_db.RegisterEnumDescriptor(_USERPLAYSTATUS)

UserPlayStatus = enum_type_wrapper.EnumTypeWrapper(_USERPLAYSTATUS)
_MTTSTATUS = _descriptor.EnumDescriptor(
  name='MttStatus',
  full_name='pb.MttStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_NOT_START', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_DELAY_JOIN', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_STOP_DELAY_JOIN', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_FINISHED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_HAS_DAY1', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_NO_DAY1', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MTT_STATUS_ENDING_SCENE', index=6, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3235,
  serialized_end=3434,
)
_sym_db.RegisterEnumDescriptor(_MTTSTATUS)

MttStatus = enum_type_wrapper.EnumTypeWrapper(_MTTSTATUS)
ACTION_NONE = 0
ACTION_FOLD = 1
ACTION_CHECK = 2
ACTION_CALL = 3
ACTION_RAISE = 4
ACTION_WAIT = 5
ACTION_SITED = 6
ACTION_BET = 7
ACTION_SB = 8
ACTION_BB = 9
ACTION_ANTE = 10
ACTION_FORCE_BB = 11
ACTION_SYSTEM_FOLD = 12
ACTION_SYSTEM_CHECK = 13
ACTION_STRADDLE = 14
ACTION_POT = 15
ACTION_FAST_FOLD = 16
ACTION_STAND_UP = 18
ACTION_BOMBPOT_BB = 19
PRE_ACTION_NONE = 0
PRE_ACTION_CHECK_OR_FOLD = 1
PRE_ACTION_CHECK = 2
PRE_ACTION_CALL = 3
PRE_ACTION_CALL_ANY = 4
PRE_ACTION_ALLIN = 5
TEST_ROOM = 0
NLH_MTT_ROOM = 2
NLH_SNG_ROOM = 3
NLH_ROOM = 5
OMAHA_ROOM = 8
PINE_ROOM = 9
OMAHA_SNG_ROOM = 10
OMAHA_MTT_ROOM = 11
SPINUP_ROOM = 13
SHARK_KING_FLIP_ROOM = 14
ROOM_MODE_NONE = 0
ROOM_MODE_CLUB = 3
GAME_MODE_REGULAR = 0
GAME_MODE_ZOOM = 11
GAME_MODE_ZOOM_NLH_6_PLUS = 17
GAME_MODE_ZOOM_PLO_5_CARDS = 18
GAME_MODE_ZOOM_ALLIN_FOLD = 19
GAME_MODE_NLH_6_PLUS = 12
GAME_MODE_PLO_5_CARDS = 10
GAME_MODE_PLO_5_CARDS_CALLTIME = 210
GAME_MODE_PLO_5_CARDS_HUNTER = 23
GAME_MODE_PLO_5_CARDS_SNOWBALL_HUNTER = 24
GAME_MODE_PLO_5_CARDS_MTT_SATELLITE = 25
GAME_MODE_PLO_5_CARDS_ALLIN_FOLD = 26
GAME_MODE_PLO_4_CARDS_ALLIN_FOLD = 27
GAME_MODE_ALLIN_FOLD = 13
GAME_MODE_ALLIN_FOLD_HUNTER = 20
GAME_MODE_ALLIN_FOLD_SNOWBALL_HUNTER = 21
GAME_MODE_ALLIN_FOLD_MTT_SATELLITE = 22
GAME_MODE_REGULAR_CALLTIME = 200
GAME_MODE_HUNTER = 14
GAME_MODE_SNOWBALL_HUNTER = 15
GAME_MODE_MTT_SATELLITE = 16
GAME_MODE_OFC_PROGRESSIVE = 1
GAME_MODE_OFC_ULTIMATE = 2
GAME_MODE_OFC_WILD_CARD_REGULAR = 100
GAME_MODE_OFC_WILD_CARD_PROGRESSIVE = 101
GAME_MODE_OFC_WILD_CARD_ULTIMATE = 102
ROUND_NONE = 0
ROUND_PRE_FLOP = 1
ROUND_FLOP = 2
ROUND_TURN = 3
ROUND_RIVER = 4
ROUND_COMPLETE = 5
INVAILID = 0
USER_MONEY = 1
PP_CURRENCY_NONE = 0
PP_CURRENCY_GOLD = 1
USER_ROOM_ACTION_NONE = 0
USER_ROOM_ACTION_SIGNUP = 1
USER_ROOM_ACTION_CANCEL_SIGNUP = 2
USER_ROOM_ACTION_SITDOWN = 3
USER_ROOM_ACTION_STANDUP = 4
USER_ROOM_ACTION_WITHDRAW = 5
BANKER_TYPE_NONE = 0
BANKER_TYPE_BUYIN = 1
BANKER_TYPE_DELAY_BUYIN = 2
BANKER_TYPE_REBUY = 3
BANKER_TYPE_TOPUP = 4
BANKER_TYPE_ADDON = 5
BANKER_TYPE_GAME_REWARD = 6
BANKER_TYPE_HUNTER_REWARD = 7
BANKER_TYPE_REFUND = 100
BANKER_TYPE_JACKPOT_REWARD = 8
BANKER_TYPE_CASHOUT = 101
BANKER_TYPE_CHANGE_TABLE = 102
BANKER_TYPE_WITHDRAW_CHIPS = 103
BANKER_TYPE_SIGNUP = 104
BANKER_TYPE_CANCEL_SIGNUP = 105
MTT_TEN_PERCENT = 0
MTT_FIFTEEN_PERCENT = 1
MTT_TWENTY_PERCENT = 2
MTT_NEW_TEN_PERCENT = 3
MTT_NEW_FIFTEEN_PERCENT = 4
MTT_NEW_TWENTY_PERCENT = 5
MTT_PKO_TEN_PERCENT = 6
MTT_PKO_FIFTEEN_PERCENT = 7
MTT_PKO_TWENTY_PERCENT = 8
GAME_SET_PLAY_STATUS_NONE = 0
GAME_SET_PLAY_STATUS_PLAYING = 1
GAME_SET_PLAY_STATUS_FINISH = 100
USER_PLAY_STATUS_NOT_IN = 0
USER_PLAY_STATUS_SIGNUP = 1
USER_PLAY_STATUS_PLAYING = 2
USER_PLAY_STATUS_STANDUP = 3
USER_PLAY_STATUS_SITTING = 4
USER_PLAY_STATUS_RETURN = 5
USER_PLAY_STATUS_CHANGE_TABLE = 6
MTT_STATUS_NOT_START = 1
MTT_STATUS_DELAY_JOIN = 2
MTT_STATUS_STOP_DELAY_JOIN = 3
MTT_STATUS_FINISHED = 4
MTT_STATUS_HAS_DAY1 = 5
MTT_STATUS_NO_DAY1 = 6
MTT_STATUS_ENDING_SCENE = 7



_REWARDCONFIGUREITEM = _descriptor.Descriptor(
  name='RewardConfigureItem',
  full_name='pb.RewardConfigureItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ranking', full_name='pb.RewardConfigureItem.ranking', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranking_nums', full_name='pb.RewardConfigureItem.ranking_nums', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pb.RewardConfigureItem.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pb.RewardConfigureItem.value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='pb.RewardConfigureItem.expire_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['RewardConfigureItem'] = _REWARDCONFIGUREITEM
DESCRIPTOR.enum_types_by_name['ActionType'] = _ACTIONTYPE
DESCRIPTOR.enum_types_by_name['PreActionType'] = _PREACTIONTYPE
DESCRIPTOR.enum_types_by_name['RoomType'] = _ROOMTYPE
DESCRIPTOR.enum_types_by_name['RoomMode'] = _ROOMMODE
DESCRIPTOR.enum_types_by_name['GameMode'] = _GAMEMODE
DESCRIPTOR.enum_types_by_name['RoundStage'] = _ROUNDSTAGE
DESCRIPTOR.enum_types_by_name['ValueType'] = _VALUETYPE
DESCRIPTOR.enum_types_by_name['PPCurrency'] = _PPCURRENCY
DESCRIPTOR.enum_types_by_name['UserRoomAction'] = _USERROOMACTION
DESCRIPTOR.enum_types_by_name['BankerType'] = _BANKERTYPE
DESCRIPTOR.enum_types_by_name['MttRewardPercentType'] = _MTTREWARDPERCENTTYPE
DESCRIPTOR.enum_types_by_name['GameSetPlayStatus'] = _GAMESETPLAYSTATUS
DESCRIPTOR.enum_types_by_name['UserPlayStatus'] = _USERPLAYSTATUS
DESCRIPTOR.enum_types_by_name['MttStatus'] = _MTTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RewardConfigureItem = _reflection.GeneratedProtocolMessageType('RewardConfigureItem', (_message.Message,), dict(
  DESCRIPTOR = _REWARDCONFIGUREITEM,
  __module__ = 'pre_base_pb2'
  # @@protoc_insertion_point(class_scope:pb.RewardConfigureItem)
  ))
_sym_db.RegisterMessage(RewardConfigureItem)


DESCRIPTOR._options = None
_REWARDCONFIGUREITEM.fields_by_name['ranking_nums']._options = None
_REWARDCONFIGUREITEM.fields_by_name['name']._options = None
_REWARDCONFIGUREITEM.fields_by_name['expire_time']._options = None
# @@protoc_insertion_point(module_scope)
