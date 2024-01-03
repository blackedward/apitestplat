# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: club_base.proto

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
  name='club_base.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x0f\x63lub_base.proto\x12\x02pb\"X\n\x0bLeagueBrief\x12\x10\n\x08room_num\x18\x01 \x01(\x05\x12\x10\n\x08leagueid\x18\x02 \x01(\x05\x12\x13\n\x0broom_num_h5\x18\x03 \x01(\x05\x12\x10\n\x08official\x18\x04 \x01(\x05\"\xb4\x01\n\tClubBrief\x12\x0e\n\x06\x63lubid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\x05\x12\x10\n\x08room_num\x18\x05 \x01(\x05\x12$\n\x0bleague_list\x18\x06 \x03(\x0b\x32\x0f.pb.LeagueBrief\x12\x13\n\x0broom_num_h5\x18\x07 \x01(\x05\x12\x0e\n\x03num\x18\x08 \x01(\x05:\x01\x30\x12\x10\n\x08platform\x18\t \x01(\t\"?\n\nClubConfig\x12\x16\n\x0brebate_rate\x18\x01 \x01(\x05:\x01\x30\x12\x19\n\x11\x61gent_rebate_rate\x18\x02 \x01(\x05*g\n\x0c\x43lubRoleType\x12\x15\n\x11\x43LUB_ROLE_FOUNDER\x10\x01\x12\x15\n\x11\x43LUB_ROLE_MANAGER\x10\x02\x12\x13\n\x0f\x43LUB_ROLE_AGENT\x10\x05\x12\x14\n\x10\x43LUB_ROLE_MEMBER\x10\n*\xf5\x03\n\x12\x43lubMemberSortType\x12\x17\n\x13\x43LUB_MEMBER_DEFAULT\x10\x00\x12\x17\n\x13\x43LUB_MEMBER_FEE_DES\x10\x01\x12\x17\n\x13\x43LUB_MEMBER_FEE_AES\x10\x02\x12\x17\n\x13\x43LUB_MEMBER_WIN_DES\x10\x03\x12\x17\n\x13\x43LUB_MEMBER_WIN_AES\x10\x04\x12\x18\n\x14\x43LUB_MEMBER_HAND_DES\x10\x05\x12\x18\n\x14\x43LUB_MEMBER_HAND_AES\x10\x06\x12\x1e\n\x1a\x43LUB_MEMBER_LAST_LOGIN_DES\x10\x07\x12\x1e\n\x1a\x43LUB_MEMBER_LAST_LOGIN_AES\x10\x08\x12\x1d\n\x19\x43LUB_MEMBER_JOIN_TIME_DES\x10\t\x12\x1d\n\x19\x43LUB_MEMBER_JOIN_TIME_AES\x10\n\x12\x1c\n\x18\x43LUB_MEMBER_RAKEBACK_DES\x10\x0b\x12\x1c\n\x18\x43LUB_MEMBER_RAKEBACK_AES\x10\x0c\x12\x18\n\x14\x43LUB_MEMBER_ROLE_DES\x10\r\x12\x18\n\x14\x43LUB_MEMBER_ROLE_AES\x10\x0e\x12\x1f\n\x1b\x43LUB_MEMBER_INACTIVEDAY_DES\x10\x0f\x12\x1f\n\x1b\x43LUB_MEMBER_INACTIVEDAY_AES\x10\x10\x42\x07Z\x05../pb')
)

_CLUBROLETYPE = _descriptor.EnumDescriptor(
  name='ClubRoleType',
  full_name='pb.ClubRoleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLUB_ROLE_FOUNDER', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_ROLE_MANAGER', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_ROLE_AGENT', index=2, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_ROLE_MEMBER', index=3, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=361,
  serialized_end=464,
)
_sym_db.RegisterEnumDescriptor(_CLUBROLETYPE)

ClubRoleType = enum_type_wrapper.EnumTypeWrapper(_CLUBROLETYPE)
_CLUBMEMBERSORTTYPE = _descriptor.EnumDescriptor(
  name='ClubMemberSortType',
  full_name='pb.ClubMemberSortType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_FEE_DES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_FEE_AES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_WIN_DES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_WIN_AES', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_HAND_DES', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_HAND_AES', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_LAST_LOGIN_DES', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_LAST_LOGIN_AES', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_JOIN_TIME_DES', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_JOIN_TIME_AES', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_RAKEBACK_DES', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_RAKEBACK_AES', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_ROLE_DES', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_ROLE_AES', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_INACTIVEDAY_DES', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUB_MEMBER_INACTIVEDAY_AES', index=16, number=16,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=467,
  serialized_end=968,
)
_sym_db.RegisterEnumDescriptor(_CLUBMEMBERSORTTYPE)

ClubMemberSortType = enum_type_wrapper.EnumTypeWrapper(_CLUBMEMBERSORTTYPE)
CLUB_ROLE_FOUNDER = 1
CLUB_ROLE_MANAGER = 2
CLUB_ROLE_AGENT = 5
CLUB_ROLE_MEMBER = 10
CLUB_MEMBER_DEFAULT = 0
CLUB_MEMBER_FEE_DES = 1
CLUB_MEMBER_FEE_AES = 2
CLUB_MEMBER_WIN_DES = 3
CLUB_MEMBER_WIN_AES = 4
CLUB_MEMBER_HAND_DES = 5
CLUB_MEMBER_HAND_AES = 6
CLUB_MEMBER_LAST_LOGIN_DES = 7
CLUB_MEMBER_LAST_LOGIN_AES = 8
CLUB_MEMBER_JOIN_TIME_DES = 9
CLUB_MEMBER_JOIN_TIME_AES = 10
CLUB_MEMBER_RAKEBACK_DES = 11
CLUB_MEMBER_RAKEBACK_AES = 12
CLUB_MEMBER_ROLE_DES = 13
CLUB_MEMBER_ROLE_AES = 14
CLUB_MEMBER_INACTIVEDAY_DES = 15
CLUB_MEMBER_INACTIVEDAY_AES = 16



_LEAGUEBRIEF = _descriptor.Descriptor(
  name='LeagueBrief',
  full_name='pb.LeagueBrief',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_num', full_name='pb.LeagueBrief.room_num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leagueid', full_name='pb.LeagueBrief.leagueid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_num_h5', full_name='pb.LeagueBrief.room_num_h5', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='official', full_name='pb.LeagueBrief.official', index=3,
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
  serialized_start=23,
  serialized_end=111,
)


_CLUBBRIEF = _descriptor.Descriptor(
  name='ClubBrief',
  full_name='pb.ClubBrief',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clubid', full_name='pb.ClubBrief.clubid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pb.ClubBrief.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='pb.ClubBrief.icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='pb.ClubBrief.role', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_num', full_name='pb.ClubBrief.room_num', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='league_list', full_name='pb.ClubBrief.league_list', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_num_h5', full_name='pb.ClubBrief.room_num_h5', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='pb.ClubBrief.num', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='pb.ClubBrief.platform', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=114,
  serialized_end=294,
)


_CLUBCONFIG = _descriptor.Descriptor(
  name='ClubConfig',
  full_name='pb.ClubConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rebate_rate', full_name='pb.ClubConfig.rebate_rate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_rebate_rate', full_name='pb.ClubConfig.agent_rebate_rate', index=1,
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
  serialized_start=296,
  serialized_end=359,
)

_CLUBBRIEF.fields_by_name['league_list'].message_type = _LEAGUEBRIEF
DESCRIPTOR.message_types_by_name['LeagueBrief'] = _LEAGUEBRIEF
DESCRIPTOR.message_types_by_name['ClubBrief'] = _CLUBBRIEF
DESCRIPTOR.message_types_by_name['ClubConfig'] = _CLUBCONFIG
DESCRIPTOR.enum_types_by_name['ClubRoleType'] = _CLUBROLETYPE
DESCRIPTOR.enum_types_by_name['ClubMemberSortType'] = _CLUBMEMBERSORTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LeagueBrief = _reflection.GeneratedProtocolMessageType('LeagueBrief', (_message.Message,), dict(
  DESCRIPTOR = _LEAGUEBRIEF,
  __module__ = 'club_base_pb2'
  # @@protoc_insertion_point(class_scope:pb.LeagueBrief)
  ))
_sym_db.RegisterMessage(LeagueBrief)

ClubBrief = _reflection.GeneratedProtocolMessageType('ClubBrief', (_message.Message,), dict(
  DESCRIPTOR = _CLUBBRIEF,
  __module__ = 'club_base_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClubBrief)
  ))
_sym_db.RegisterMessage(ClubBrief)

ClubConfig = _reflection.GeneratedProtocolMessageType('ClubConfig', (_message.Message,), dict(
  DESCRIPTOR = _CLUBCONFIG,
  __module__ = 'club_base_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClubConfig)
  ))
_sym_db.RegisterMessage(ClubConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
