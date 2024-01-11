# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_club_room.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_club_room.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\004./pb'),
  serialized_pb=_b('\n\x16\x63reate_club_room.proto\x12\x02pb\x1a\x0epre_base.proto\x1a\nbase.proto\x1a\npine.proto\x1a\x0e\x63\x61lltime.proto\x1a\x0fpre_base1.proto\x1a\tsng.proto\"\xbf\x0e\n\x11\x43reateClubRoomREQ\x12\x11\n\troom_name\x18\x01 \x01(\t\x12\r\n\x05\x62lind\x18\x02 \x01(\x03\x12\x0c\n\x04\x61nte\x18\x03 \x01(\x03\x12\x11\n\tmin_buyin\x18\x04 \x01(\x03\x12\x11\n\tgame_time\x18\x05 \x01(\x05\x12\x13\n\x0b\x61\x63tion_time\x18\x06 \x01(\x05\x12\x12\n\x07\x66\x65\x65type\x18\x07 \x01(\x05:\x01\x31\x12\x13\n\x08\x66\x65\x65point\x18\x08 \x01(\x05:\x01\x35\x12\x19\n\nauth_limit\x18\t \x01(\x08:\x05\x66\x61lse\x12\x11\n\x06\x63lubid\x18\n \x01(\x05:\x01\x30\x12\x10\n\x08seat_num\x18\x0b \x01(\x05\x12\x0b\n\x03\x63\x61p\x18\x0c \x01(\x05\x12\x1a\n\x04type\x18\r \x01(\x0e\x32\x0c.pb.RoomType\x12\x11\n\tmax_buyin\x18\x0e \x01(\x03\x12\x13\n\x08timezone\x18\x0f \x01(\x05:\x01\x38\x12\x0e\n\x06roomid\x18\x10 \x01(\x05\x12\x15\n\rdefault_buyin\x18\x11 \x01(\x03\x12!\n\x12is_run_multi_times\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cis_insurance\x18\x13 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x08leagueid\x18\x14 \x01(\x05:\x01\x30\x12\x18\n\tgps_limit\x18\x15 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x08ip_limit\x18\x16 \x01(\x08:\x05\x66\x61lse\x12\x11\n\x06\x63ityid\x18\x17 \x01(\x05:\x01\x30\x12\x16\n\nauto_start\x18\x18 \x01(\x05:\x02-1\x12\x32\n\tgame_mode\x18\x19 \x01(\x0e\x32\x0c.pb.GameMode:\x11GAME_MODE_REGULAR\x12\x18\n\x10\x63\x61lltime_minutes\x18\x1a \x01(\x05\x12\x1d\n\x0ewithdraw_chips\x18\x1b \x01(\x08:\x05\x66\x61lse\x12&\n\x17is_auto_delay_room_over\x18\x1c \x01(\x08:\x05\x66\x61lse\x12&\n\x1a\x61uto_delay_room_over_times\x18\x1d \x01(\x05:\x02\x31\x32\x12!\n\x13is_auto_create_room\x18\x1e \x01(\x08:\x04true\x12\x1a\n\x0f\x63reator_user_id\x18\x1f \x01(\x03:\x01\x30\x12\x15\n\nvpip_limit\x18  \x01(\x05:\x01\x30\x12\x13\n\x08moduleid\x18! \x01(\x03:\x01\x30\x12\x12\n\nmulti_opid\x18\" \x01(\t\x12\x15\n\x07\x63\x61n_use\x18# \x01(\x08:\x04true\x12\x1d\n\x0e\x66orbidden_chat\x18$ \x01(\x08:\x05\x66\x61lse\x12\x18\n\tis_evchop\x18% \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x12vpip_limit_per_set\x18& \x01(\x05:\x01\x30\x12\x1c\n\x11min_hands_per_set\x18\' \x01(\x05:\x01\x30\x12\x1b\n\x0cpasswd_limit\x18( \x01(\x08:\x05\x66\x61lse\x12\x19\n\x0esuper_leagueid\x18) \x01(\x05:\x01\x30\x12\x1c\n\x11super_league_type\x18* \x01(\x05:\x01\x30\x12\x13\n\x0b\x61nte_up_vec\x18+ \x03(\x03\x12\x18\n\rderive_roomid\x18, \x01(\x05:\x01\x30\x12\x19\n\nis_captcha\x18- \x01(\x08:\x05\x66\x61lse\x12\x18\n\tis_ban_pc\x18. \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ris_check_mail\x18/ \x01(\x08:\x05\x66\x61lse\x12(\n\x1dseven_deuce_reward_multiplier\x18\x30 \x01(\x05:\x01\x30\x12\x1e\n\x13\x66orbidden_chat_mode\x18\x31 \x01(\x05:\x01\x30\x12\x1b\n\x0cis_vip_table\x18\x32 \x01(\x08:\x05\x66\x61lse\x12%\n\x1d\x65nter_room_chips_prerequisite\x18\x33 \x01(\x03\x12\x11\n\x06ppsrid\x18\x34 \x01(\x05:\x01\x30\x12\x12\n\nis_jackpot\x18\x35 \x01(\x08\x12\x1f\n\x10is_certification\x18\x36 \x01(\x08:\x05\x66\x61lse\x12\x18\n\rparent_roomid\x18\x37 \x01(\x05:\x01\x30\x12\x1d\n\x12parent_room_handle\x18\x38 \x01(\r:\x01\x30\x12\x17\n\x0c\x62ombpot_type\x18\x39 \x01(\x05:\x01\x30\x12\x1e\n\x13\x63ycle_bombpot_hands\x18: \x01(\x05:\x01\x30\x12 \n\x15\x63ycle_bombpot_seconds\x18; \x01(\x05:\x01\x30\x12\x19\n\x0emin_bomb_times\x18< \x01(\x05:\x01\x30\x12\x19\n\x0emax_bomb_times\x18= \x01(\x05:\x01\x30\x12#\n\x18\x62ombpot_additional_board\x18> \x01(\x05:\x01\x30\x12\x1b\n\x10\x61\x64\x64itional_board\x18? \x01(\x05:\x01\x30\x12\x10\n\x08\x62\x61n_club\x18@ \x03(\x05\x12\x13\n\x0b\x62\x61n_country\x18\x41 \x03(\t\x12&\n\x17is_sequential_view_card\x18\x42 \x01(\x08:\x05\x66\x61lse\x12(\n\x19is_bombpot_without_evchop\x18\x43 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rcustom_passwd\x18\x44 \x01(\t\x12\x18\n\rcalltime_type\x18\x45 \x01(\x05:\x01\x30\"R\n\x11\x43reateClubRoomRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x1f\n\troom_info\x18\x03 \x01(\x0b\x32\x0c.pb.RoomInfoB\x06Z\x04./pb')
  ,
  dependencies=[pre__base__pb2.DESCRIPTOR,base__pb2.DESCRIPTOR,pine__pb2.DESCRIPTOR,calltime__pb2.DESCRIPTOR,pre__base1__pb2.DESCRIPTOR,sng__pb2.DESCRIPTOR,])




_CREATECLUBROOMREQ = _descriptor.Descriptor(
  name='CreateClubRoomREQ',
  full_name='pb.CreateClubRoomREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_name', full_name='pb.CreateClubRoomREQ.room_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blind', full_name='pb.CreateClubRoomREQ.blind', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ante', full_name='pb.CreateClubRoomREQ.ante', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_buyin', full_name='pb.CreateClubRoomREQ.min_buyin', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_time', full_name='pb.CreateClubRoomREQ.game_time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_time', full_name='pb.CreateClubRoomREQ.action_time', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feetype', full_name='pb.CreateClubRoomREQ.feetype', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feepoint', full_name='pb.CreateClubRoomREQ.feepoint', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_limit', full_name='pb.CreateClubRoomREQ.auth_limit', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clubid', full_name='pb.CreateClubRoomREQ.clubid', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seat_num', full_name='pb.CreateClubRoomREQ.seat_num', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cap', full_name='pb.CreateClubRoomREQ.cap', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.CreateClubRoomREQ.type', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_buyin', full_name='pb.CreateClubRoomREQ.max_buyin', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='pb.CreateClubRoomREQ.timezone', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='pb.CreateClubRoomREQ.roomid', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_buyin', full_name='pb.CreateClubRoomREQ.default_buyin', index=16,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_run_multi_times', full_name='pb.CreateClubRoomREQ.is_run_multi_times', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_insurance', full_name='pb.CreateClubRoomREQ.is_insurance', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leagueid', full_name='pb.CreateClubRoomREQ.leagueid', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gps_limit', full_name='pb.CreateClubRoomREQ.gps_limit', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_limit', full_name='pb.CreateClubRoomREQ.ip_limit', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cityid', full_name='pb.CreateClubRoomREQ.cityid', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_start', full_name='pb.CreateClubRoomREQ.auto_start', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_mode', full_name='pb.CreateClubRoomREQ.game_mode', index=24,
      number=25, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calltime_minutes', full_name='pb.CreateClubRoomREQ.calltime_minutes', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdraw_chips', full_name='pb.CreateClubRoomREQ.withdraw_chips', index=26,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_auto_delay_room_over', full_name='pb.CreateClubRoomREQ.is_auto_delay_room_over', index=27,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_delay_room_over_times', full_name='pb.CreateClubRoomREQ.auto_delay_room_over_times', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=12,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_auto_create_room', full_name='pb.CreateClubRoomREQ.is_auto_create_room', index=29,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator_user_id', full_name='pb.CreateClubRoomREQ.creator_user_id', index=30,
      number=31, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vpip_limit', full_name='pb.CreateClubRoomREQ.vpip_limit', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleid', full_name='pb.CreateClubRoomREQ.moduleid', index=32,
      number=33, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_opid', full_name='pb.CreateClubRoomREQ.multi_opid', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_use', full_name='pb.CreateClubRoomREQ.can_use', index=34,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forbidden_chat', full_name='pb.CreateClubRoomREQ.forbidden_chat', index=35,
      number=36, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_evchop', full_name='pb.CreateClubRoomREQ.is_evchop', index=36,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vpip_limit_per_set', full_name='pb.CreateClubRoomREQ.vpip_limit_per_set', index=37,
      number=38, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_hands_per_set', full_name='pb.CreateClubRoomREQ.min_hands_per_set', index=38,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passwd_limit', full_name='pb.CreateClubRoomREQ.passwd_limit', index=39,
      number=40, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='super_leagueid', full_name='pb.CreateClubRoomREQ.super_leagueid', index=40,
      number=41, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='super_league_type', full_name='pb.CreateClubRoomREQ.super_league_type', index=41,
      number=42, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ante_up_vec', full_name='pb.CreateClubRoomREQ.ante_up_vec', index=42,
      number=43, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derive_roomid', full_name='pb.CreateClubRoomREQ.derive_roomid', index=43,
      number=44, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_captcha', full_name='pb.CreateClubRoomREQ.is_captcha', index=44,
      number=45, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_ban_pc', full_name='pb.CreateClubRoomREQ.is_ban_pc', index=45,
      number=46, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_check_mail', full_name='pb.CreateClubRoomREQ.is_check_mail', index=46,
      number=47, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seven_deuce_reward_multiplier', full_name='pb.CreateClubRoomREQ.seven_deuce_reward_multiplier', index=47,
      number=48, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forbidden_chat_mode', full_name='pb.CreateClubRoomREQ.forbidden_chat_mode', index=48,
      number=49, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_vip_table', full_name='pb.CreateClubRoomREQ.is_vip_table', index=49,
      number=50, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enter_room_chips_prerequisite', full_name='pb.CreateClubRoomREQ.enter_room_chips_prerequisite', index=50,
      number=51, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ppsrid', full_name='pb.CreateClubRoomREQ.ppsrid', index=51,
      number=52, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_jackpot', full_name='pb.CreateClubRoomREQ.is_jackpot', index=52,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_certification', full_name='pb.CreateClubRoomREQ.is_certification', index=53,
      number=54, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_roomid', full_name='pb.CreateClubRoomREQ.parent_roomid', index=54,
      number=55, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_room_handle', full_name='pb.CreateClubRoomREQ.parent_room_handle', index=55,
      number=56, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bombpot_type', full_name='pb.CreateClubRoomREQ.bombpot_type', index=56,
      number=57, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cycle_bombpot_hands', full_name='pb.CreateClubRoomREQ.cycle_bombpot_hands', index=57,
      number=58, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cycle_bombpot_seconds', full_name='pb.CreateClubRoomREQ.cycle_bombpot_seconds', index=58,
      number=59, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_bomb_times', full_name='pb.CreateClubRoomREQ.min_bomb_times', index=59,
      number=60, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bomb_times', full_name='pb.CreateClubRoomREQ.max_bomb_times', index=60,
      number=61, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bombpot_additional_board', full_name='pb.CreateClubRoomREQ.bombpot_additional_board', index=61,
      number=62, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additional_board', full_name='pb.CreateClubRoomREQ.additional_board', index=62,
      number=63, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ban_club', full_name='pb.CreateClubRoomREQ.ban_club', index=63,
      number=64, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ban_country', full_name='pb.CreateClubRoomREQ.ban_country', index=64,
      number=65, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_sequential_view_card', full_name='pb.CreateClubRoomREQ.is_sequential_view_card', index=65,
      number=66, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_bombpot_without_evchop', full_name='pb.CreateClubRoomREQ.is_bombpot_without_evchop', index=66,
      number=67, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_passwd', full_name='pb.CreateClubRoomREQ.custom_passwd', index=67,
      number=68, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calltime_type', full_name='pb.CreateClubRoomREQ.calltime_type', index=68,
      number=69, type=5, cpp_type=1, label=1,
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
  serialized_start=115,
  serialized_end=1970,
)


_CREATECLUBROOMRSP = _descriptor.Descriptor(
  name='CreateClubRoomRSP',
  full_name='pb.CreateClubRoomRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.CreateClubRoomRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='pb.CreateClubRoomRSP.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_info', full_name='pb.CreateClubRoomRSP.room_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1972,
  serialized_end=2054,
)

_CREATECLUBROOMREQ.fields_by_name['type'].enum_type = pre__base__pb2._ROOMTYPE
_CREATECLUBROOMREQ.fields_by_name['game_mode'].enum_type = pre__base__pb2._GAMEMODE
_CREATECLUBROOMRSP.fields_by_name['room_info'].message_type = base__pb2._ROOMINFO
DESCRIPTOR.message_types_by_name['CreateClubRoomREQ'] = _CREATECLUBROOMREQ
DESCRIPTOR.message_types_by_name['CreateClubRoomRSP'] = _CREATECLUBROOMRSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateClubRoomREQ = _reflection.GeneratedProtocolMessageType('CreateClubRoomREQ', (_message.Message,), dict(
  DESCRIPTOR = _CREATECLUBROOMREQ,
  __module__ = 'create_club_room_pb2'
  # @@protoc_insertion_point(class_scope:pb.CreateClubRoomREQ)
  ))
_sym_db.RegisterMessage(CreateClubRoomREQ)

CreateClubRoomRSP = _reflection.GeneratedProtocolMessageType('CreateClubRoomRSP', (_message.Message,), dict(
  DESCRIPTOR = _CREATECLUBROOMRSP,
  __module__ = 'create_club_room_pb2'
  # @@protoc_insertion_point(class_scope:pb.CreateClubRoomRSP)
  ))
_sym_db.RegisterMessage(CreateClubRoomRSP)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
