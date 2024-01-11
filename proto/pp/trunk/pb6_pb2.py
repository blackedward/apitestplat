# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb6.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pre_base_pb2 as pre__base__pb2
import base_pb2 as base__pb2
try:
  pre__base__pb2 = base__pb2.pre__base__pb2
except AttributeError:
  pre__base__pb2 = base__pb2.pre_base_pb2
try:
  pre__base1__pb2 = base__pb2.pre__base1__pb2
except AttributeError:
  pre__base1__pb2 = base__pb2.pre_base1_pb2
import pine_pb2 as pine__pb2
try:
  pine1__pb2 = pine__pb2.pine1__pb2
except AttributeError:
  pine1__pb2 = pine__pb2.pine1_pb2
import calltime_pb2 as calltime__pb2
import pre_base1_pb2 as pre__base1__pb2
import sng_pb2 as sng__pb2
import pb1_pb2 as pb1__pb2
import pb4_pb2 as pb4__pb2
import pusoy_pb2 as pusoy__pb2
import tp_pb2 as tp__pb2
import lucky_draw_pb2 as lucky__draw__pb2
import colorgame_pb2 as colorgame__pb2
import tongits_pb2 as tongits__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb6.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\004./pb'),
  serialized_pb=_b('\n\tpb6.proto\x12\x02pb\x1a\x0epre_base.proto\x1a\nbase.proto\x1a\npine.proto\x1a\x0e\x63\x61lltime.proto\x1a\x0fpre_base1.proto\x1a\tsng.proto\x1a\tpb1.proto\x1a\tpb4.proto\x1a\x0bpusoy.proto\x1a\x08tp.proto\x1a\x10lucky_draw.proto\x1a\x0f\x63olorgame.proto\x1a\rtongits.proto\"|\n\x0eShowCaptchaRSP\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x17\n\x0fslide_parameter\x18\x02 \x01(\x05\x12\x16\n\x0eicon_parameter\x18\x03 \x03(\x05\x12\x15\n\rnum_parameter\x18\x04 \x03(\x05\x12\x14\n\tleft_time\x18\x05 \x01(\x05:\x01\x30\"\x1d\n\rEndCaptchaRSP\x12\x0c\n\x04type\x18\x01 \x01(\x05\"b\n\nCaptchaREQ\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x17\n\x0fslide_parameter\x18\x02 \x01(\x05\x12\x16\n\x0eicon_parameter\x18\x03 \x03(\x05\x12\x15\n\rnum_parameter\x18\x04 \x01(\x05\"\x1a\n\nCaptchaRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\"v\n\x13\x43\x61ptchaFailLeaveRSP\x12\x0e\n\x06roomid\x18\x01 \x01(\x05\x12\x1f\n\troom_type\x18\x02 \x01(\x0e\x32\x0c.pb.RoomType\x12\x1f\n\tgame_mode\x18\x03 \x01(\x0e\x32\x0c.pb.GameMode\x12\r\n\x05\x62lind\x18\x04 \x01(\x05\"\x97\n\n\x0c\x45nterRoomRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12%\n\x0ctable_status\x18\x03 \x01(\x0b\x32\x0f.pb.TableStatus\x12#\n\x0broom_status\x18\x04 \x01(\x0b\x32\x0e.pb.RoomStatus\x12)\n\x0eplaying_status\x18\x05 \x01(\x0b\x32\x11.pb.PlayingStatus\x12\x1f\n\troom_info\x18\x06 \x01(\x0b\x32\x0c.pb.RoomInfo\x12\x1f\n\troom_type\x18\x07 \x01(\x0e\x32\x0c.pb.RoomType\x12%\n\x0csngroom_info\x18\x08 \x01(\x0b\x32\x0f.pb.SngRoomInfo\x12%\n\x0cmttroom_info\x18\t \x01(\x0b\x32\x0f.pb.MttRoomInfo\x12\x0e\n\x06roomid\x18\n \x01(\x05\x12/\n\troom_mode\x18\x0b \x01(\x0e\x32\x0c.pb.RoomMode:\x0eROOM_MODE_NONE\x12\'\n\rpineroom_info\x18\x0c \x01(\x0b\x32\x10.pb.PineRoomInfo\x12,\n\x10pine_room_status\x18\r \x01(\x0b\x32\x12.pb.PineRoomStatus\x12,\n\troom_list\x18\x0e \x03(\x0b\x32\x19.pb.MultipleTableRoomInfo\x12\x0c\n\x04type\x18\x0f \x01(\x05\x12.\n\x0bspinup_info\x18\x10 \x01(\x0b\x32\x19.pb.SpinUpDrawLotteryInfo\x12-\n\x0fguess_hand_info\x18\x11 \x01(\x0b\x32\x14.pb.GuessHandSubInfo\x12(\n\nstorm_info\x18\x12 \x01(\x0b\x32\x14.pb.PPchipsStormInfo\x12\x39\n\x17waiting_game_start_info\x18\x13 \x01(\x0b\x32\x18.pb.WaitingGameStartInfo\x12\'\n\rcallgame_info\x18\x14 \x01(\x0b\x32\x10.pb.CallGameInfo\x12\x1f\n\tuser_vpip\x18\x15 \x01(\x0b\x32\x0c.pb.UserVpip\x12(\n\x0c\x63\x61ptcha_info\x18\x16 \x01(\x0b\x32\x12.pb.ShowCaptchaRSP\x12\x18\n\ruser_leagueid\x18\x17 \x01(\x05:\x01\x30\x12\x1e\n\x13user_super_leagueid\x18\x18 \x01(\x05:\x01\x30\x12*\n\x0fpusoy_room_info\x18\x19 \x01(\x0b\x32\x11.pb.PusoyRoomInfo\x12.\n\x11pusoy_room_status\x18\x1a \x01(\x0b\x32\x13.pb.PusoyRoomStatus\x12$\n\x0ctp_room_info\x18\x1b \x01(\x0b\x32\x0e.pb.TpRoomInfo\x12*\n\x0ftp_table_status\x18\x1c \x01(\x0b\x32\x11.pb.TpTableStatus\x12.\n\x11lucky_draw_config\x18\x1d \x01(\x0b\x32\x13.pb.LuckyDrawConfig\x12*\n\x0f\x63olor_room_info\x18\x1e \x01(\x0b\x32\x11.pb.ColorRoomInfo\x12.\n\x11\x63olor_room_status\x18\x1f \x01(\x0b\x32\x13.pb.ColorRoomStatus\x12.\n\x11tongits_room_info\x18  \x01(\x0b\x32\x13.pb.TongitsRoomInfo\x12\x32\n\x13tongits_room_status\x18! \x01(\x0b\x32\x15.pb.TongitsRoomStatus\"&\n\x0e\x44iscardCardREQ\x12\x14\n\x0c\x64iscard_card\x18\x01 \x01(\x05\"4\n\x0e\x44iscardCardRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x14\n\x0c\x64iscard_card\x18\x02 \x01(\x05\" \n\x0e\x44iscardCardBRC\x12\x0e\n\x06seatid\x18\x01 \x03(\x05\"#\n\x0eShowDiscardBRC\x12\x11\n\tleft_time\x18\x01 \x01(\x05\"\x0f\n\rEndDiscardBRCB\x06Z\x04./pb')
  ,
  dependencies=[pre__base__pb2.DESCRIPTOR,base__pb2.DESCRIPTOR,pine__pb2.DESCRIPTOR,calltime__pb2.DESCRIPTOR,pre__base1__pb2.DESCRIPTOR,sng__pb2.DESCRIPTOR,pb1__pb2.DESCRIPTOR,pb4__pb2.DESCRIPTOR,pusoy__pb2.DESCRIPTOR,tp__pb2.DESCRIPTOR,lucky__draw__pb2.DESCRIPTOR,colorgame__pb2.DESCRIPTOR,tongits__pb2.DESCRIPTOR,])




_SHOWCAPTCHARSP = _descriptor.Descriptor(
  name='ShowCaptchaRSP',
  full_name='pb.ShowCaptchaRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.ShowCaptchaRSP.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slide_parameter', full_name='pb.ShowCaptchaRSP.slide_parameter', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_parameter', full_name='pb.ShowCaptchaRSP.icon_parameter', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_parameter', full_name='pb.ShowCaptchaRSP.num_parameter', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_time', full_name='pb.ShowCaptchaRSP.left_time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=196,
  serialized_end=320,
)


_ENDCAPTCHARSP = _descriptor.Descriptor(
  name='EndCaptchaRSP',
  full_name='pb.EndCaptchaRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.EndCaptchaRSP.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=322,
  serialized_end=351,
)


_CAPTCHAREQ = _descriptor.Descriptor(
  name='CaptchaREQ',
  full_name='pb.CaptchaREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.CaptchaREQ.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slide_parameter', full_name='pb.CaptchaREQ.slide_parameter', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_parameter', full_name='pb.CaptchaREQ.icon_parameter', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_parameter', full_name='pb.CaptchaREQ.num_parameter', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=353,
  serialized_end=451,
)


_CAPTCHARSP = _descriptor.Descriptor(
  name='CaptchaRSP',
  full_name='pb.CaptchaRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.CaptchaRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=453,
  serialized_end=479,
)


_CAPTCHAFAILLEAVERSP = _descriptor.Descriptor(
  name='CaptchaFailLeaveRSP',
  full_name='pb.CaptchaFailLeaveRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomid', full_name='pb.CaptchaFailLeaveRSP.roomid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_type', full_name='pb.CaptchaFailLeaveRSP.room_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_mode', full_name='pb.CaptchaFailLeaveRSP.game_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blind', full_name='pb.CaptchaFailLeaveRSP.blind', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=481,
  serialized_end=599,
)


_ENTERROOMRSP = _descriptor.Descriptor(
  name='EnterRoomRSP',
  full_name='pb.EnterRoomRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.EnterRoomRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='pb.EnterRoomRSP.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_status', full_name='pb.EnterRoomRSP.table_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_status', full_name='pb.EnterRoomRSP.room_status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playing_status', full_name='pb.EnterRoomRSP.playing_status', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_info', full_name='pb.EnterRoomRSP.room_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_type', full_name='pb.EnterRoomRSP.room_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sngroom_info', full_name='pb.EnterRoomRSP.sngroom_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mttroom_info', full_name='pb.EnterRoomRSP.mttroom_info', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='pb.EnterRoomRSP.roomid', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_mode', full_name='pb.EnterRoomRSP.room_mode', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pineroom_info', full_name='pb.EnterRoomRSP.pineroom_info', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pine_room_status', full_name='pb.EnterRoomRSP.pine_room_status', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_list', full_name='pb.EnterRoomRSP.room_list', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.EnterRoomRSP.type', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spinup_info', full_name='pb.EnterRoomRSP.spinup_info', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guess_hand_info', full_name='pb.EnterRoomRSP.guess_hand_info', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storm_info', full_name='pb.EnterRoomRSP.storm_info', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waiting_game_start_info', full_name='pb.EnterRoomRSP.waiting_game_start_info', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callgame_info', full_name='pb.EnterRoomRSP.callgame_info', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_vpip', full_name='pb.EnterRoomRSP.user_vpip', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='captcha_info', full_name='pb.EnterRoomRSP.captcha_info', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_leagueid', full_name='pb.EnterRoomRSP.user_leagueid', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_super_leagueid', full_name='pb.EnterRoomRSP.user_super_leagueid', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pusoy_room_info', full_name='pb.EnterRoomRSP.pusoy_room_info', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pusoy_room_status', full_name='pb.EnterRoomRSP.pusoy_room_status', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tp_room_info', full_name='pb.EnterRoomRSP.tp_room_info', index=26,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tp_table_status', full_name='pb.EnterRoomRSP.tp_table_status', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lucky_draw_config', full_name='pb.EnterRoomRSP.lucky_draw_config', index=28,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_room_info', full_name='pb.EnterRoomRSP.color_room_info', index=29,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_room_status', full_name='pb.EnterRoomRSP.color_room_status', index=30,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tongits_room_info', full_name='pb.EnterRoomRSP.tongits_room_info', index=31,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tongits_room_status', full_name='pb.EnterRoomRSP.tongits_room_status', index=32,
      number=33, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=602,
  serialized_end=1905,
)


_DISCARDCARDREQ = _descriptor.Descriptor(
  name='DiscardCardREQ',
  full_name='pb.DiscardCardREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discard_card', full_name='pb.DiscardCardREQ.discard_card', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1907,
  serialized_end=1945,
)


_DISCARDCARDRSP = _descriptor.Descriptor(
  name='DiscardCardRSP',
  full_name='pb.DiscardCardRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.DiscardCardRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discard_card', full_name='pb.DiscardCardRSP.discard_card', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1947,
  serialized_end=1999,
)


_DISCARDCARDBRC = _descriptor.Descriptor(
  name='DiscardCardBRC',
  full_name='pb.DiscardCardBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.DiscardCardBRC.seatid', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=2001,
  serialized_end=2033,
)


_SHOWDISCARDBRC = _descriptor.Descriptor(
  name='ShowDiscardBRC',
  full_name='pb.ShowDiscardBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_time', full_name='pb.ShowDiscardBRC.left_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=2035,
  serialized_end=2070,
)


_ENDDISCARDBRC = _descriptor.Descriptor(
  name='EndDiscardBRC',
  full_name='pb.EndDiscardBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=2072,
  serialized_end=2087,
)

_CAPTCHAFAILLEAVERSP.fields_by_name['room_type'].enum_type = pre__base__pb2._ROOMTYPE
_CAPTCHAFAILLEAVERSP.fields_by_name['game_mode'].enum_type = pre__base__pb2._GAMEMODE
_ENTERROOMRSP.fields_by_name['table_status'].message_type = pb1__pb2._TABLESTATUS
_ENTERROOMRSP.fields_by_name['room_status'].message_type = pb1__pb2._ROOMSTATUS
_ENTERROOMRSP.fields_by_name['playing_status'].message_type = pb1__pb2._PLAYINGSTATUS
_ENTERROOMRSP.fields_by_name['room_info'].message_type = base__pb2._ROOMINFO
_ENTERROOMRSP.fields_by_name['room_type'].enum_type = pre__base__pb2._ROOMTYPE
_ENTERROOMRSP.fields_by_name['sngroom_info'].message_type = base__pb2._SNGROOMINFO
_ENTERROOMRSP.fields_by_name['mttroom_info'].message_type = base__pb2._MTTROOMINFO
_ENTERROOMRSP.fields_by_name['room_mode'].enum_type = pre__base__pb2._ROOMMODE
_ENTERROOMRSP.fields_by_name['pineroom_info'].message_type = pine__pb2._PINEROOMINFO
_ENTERROOMRSP.fields_by_name['pine_room_status'].message_type = pine__pb2._PINEROOMSTATUS
_ENTERROOMRSP.fields_by_name['room_list'].message_type = pb1__pb2._MULTIPLETABLEROOMINFO
_ENTERROOMRSP.fields_by_name['spinup_info'].message_type = sng__pb2._SPINUPDRAWLOTTERYINFO
_ENTERROOMRSP.fields_by_name['guess_hand_info'].message_type = sng__pb2._GUESSHANDSUBINFO
_ENTERROOMRSP.fields_by_name['storm_info'].message_type = base__pb2._PPCHIPSSTORMINFO
_ENTERROOMRSP.fields_by_name['waiting_game_start_info'].message_type = sng__pb2._WAITINGGAMESTARTINFO
_ENTERROOMRSP.fields_by_name['callgame_info'].message_type = sng__pb2._CALLGAMEINFO
_ENTERROOMRSP.fields_by_name['user_vpip'].message_type = pb4__pb2._USERVPIP
_ENTERROOMRSP.fields_by_name['captcha_info'].message_type = _SHOWCAPTCHARSP
_ENTERROOMRSP.fields_by_name['pusoy_room_info'].message_type = pusoy__pb2._PUSOYROOMINFO
_ENTERROOMRSP.fields_by_name['pusoy_room_status'].message_type = pusoy__pb2._PUSOYROOMSTATUS
_ENTERROOMRSP.fields_by_name['tp_room_info'].message_type = tp__pb2._TPROOMINFO
_ENTERROOMRSP.fields_by_name['tp_table_status'].message_type = tp__pb2._TPTABLESTATUS
_ENTERROOMRSP.fields_by_name['lucky_draw_config'].message_type = lucky__draw__pb2._LUCKYDRAWCONFIG
_ENTERROOMRSP.fields_by_name['color_room_info'].message_type = colorgame__pb2._COLORROOMINFO
_ENTERROOMRSP.fields_by_name['color_room_status'].message_type = colorgame__pb2._COLORROOMSTATUS
_ENTERROOMRSP.fields_by_name['tongits_room_info'].message_type = tongits__pb2._TONGITSROOMINFO
_ENTERROOMRSP.fields_by_name['tongits_room_status'].message_type = tongits__pb2._TONGITSROOMSTATUS
DESCRIPTOR.message_types_by_name['ShowCaptchaRSP'] = _SHOWCAPTCHARSP
DESCRIPTOR.message_types_by_name['EndCaptchaRSP'] = _ENDCAPTCHARSP
DESCRIPTOR.message_types_by_name['CaptchaREQ'] = _CAPTCHAREQ
DESCRIPTOR.message_types_by_name['CaptchaRSP'] = _CAPTCHARSP
DESCRIPTOR.message_types_by_name['CaptchaFailLeaveRSP'] = _CAPTCHAFAILLEAVERSP
DESCRIPTOR.message_types_by_name['EnterRoomRSP'] = _ENTERROOMRSP
DESCRIPTOR.message_types_by_name['DiscardCardREQ'] = _DISCARDCARDREQ
DESCRIPTOR.message_types_by_name['DiscardCardRSP'] = _DISCARDCARDRSP
DESCRIPTOR.message_types_by_name['DiscardCardBRC'] = _DISCARDCARDBRC
DESCRIPTOR.message_types_by_name['ShowDiscardBRC'] = _SHOWDISCARDBRC
DESCRIPTOR.message_types_by_name['EndDiscardBRC'] = _ENDDISCARDBRC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShowCaptchaRSP = _reflection.GeneratedProtocolMessageType('ShowCaptchaRSP', (_message.Message,), dict(
  DESCRIPTOR = _SHOWCAPTCHARSP,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.ShowCaptchaRSP)
  ))
_sym_db.RegisterMessage(ShowCaptchaRSP)

EndCaptchaRSP = _reflection.GeneratedProtocolMessageType('EndCaptchaRSP', (_message.Message,), dict(
  DESCRIPTOR = _ENDCAPTCHARSP,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.EndCaptchaRSP)
  ))
_sym_db.RegisterMessage(EndCaptchaRSP)

CaptchaREQ = _reflection.GeneratedProtocolMessageType('CaptchaREQ', (_message.Message,), dict(
  DESCRIPTOR = _CAPTCHAREQ,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.CaptchaREQ)
  ))
_sym_db.RegisterMessage(CaptchaREQ)

CaptchaRSP = _reflection.GeneratedProtocolMessageType('CaptchaRSP', (_message.Message,), dict(
  DESCRIPTOR = _CAPTCHARSP,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.CaptchaRSP)
  ))
_sym_db.RegisterMessage(CaptchaRSP)

CaptchaFailLeaveRSP = _reflection.GeneratedProtocolMessageType('CaptchaFailLeaveRSP', (_message.Message,), dict(
  DESCRIPTOR = _CAPTCHAFAILLEAVERSP,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.CaptchaFailLeaveRSP)
  ))
_sym_db.RegisterMessage(CaptchaFailLeaveRSP)

EnterRoomRSP = _reflection.GeneratedProtocolMessageType('EnterRoomRSP', (_message.Message,), dict(
  DESCRIPTOR = _ENTERROOMRSP,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.EnterRoomRSP)
  ))
_sym_db.RegisterMessage(EnterRoomRSP)

DiscardCardREQ = _reflection.GeneratedProtocolMessageType('DiscardCardREQ', (_message.Message,), dict(
  DESCRIPTOR = _DISCARDCARDREQ,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.DiscardCardREQ)
  ))
_sym_db.RegisterMessage(DiscardCardREQ)

DiscardCardRSP = _reflection.GeneratedProtocolMessageType('DiscardCardRSP', (_message.Message,), dict(
  DESCRIPTOR = _DISCARDCARDRSP,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.DiscardCardRSP)
  ))
_sym_db.RegisterMessage(DiscardCardRSP)

DiscardCardBRC = _reflection.GeneratedProtocolMessageType('DiscardCardBRC', (_message.Message,), dict(
  DESCRIPTOR = _DISCARDCARDBRC,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.DiscardCardBRC)
  ))
_sym_db.RegisterMessage(DiscardCardBRC)

ShowDiscardBRC = _reflection.GeneratedProtocolMessageType('ShowDiscardBRC', (_message.Message,), dict(
  DESCRIPTOR = _SHOWDISCARDBRC,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.ShowDiscardBRC)
  ))
_sym_db.RegisterMessage(ShowDiscardBRC)

EndDiscardBRC = _reflection.GeneratedProtocolMessageType('EndDiscardBRC', (_message.Message,), dict(
  DESCRIPTOR = _ENDDISCARDBRC,
  __module__ = 'pb6_pb2'
  # @@protoc_insertion_point(class_scope:pb.EndDiscardBRC)
  ))
_sym_db.RegisterMessage(EndDiscardBRC)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
