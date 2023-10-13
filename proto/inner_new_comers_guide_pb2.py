# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inner_new_comers_guide.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base2_pb2 as base2__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inner_new_comers_guide.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x1cinner_new_comers_guide.proto\x12\x02pb\x1a\x0b\x62\x61se2.proto\"\x88\x01\n\x1eNewComersGuideMissionGroupInfo\x12\x10\n\x08group_id\x18\x01 \x01(\x03\x12\x10\n\x08identity\x18\x02 \x01(\t\x12,\n\x05infos\x18\x03 \x03(\x0b\x32\x1d.pb.NewComersGuideMissionInfo\x12\x14\n\x0c\x65xpired_time\x18\x04 \x01(\x03\"\xb3\x01\n\x19NewComersGuideMissionInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x63ontent_num\x18\x02 \x01(\x03\x12\x13\n\x0b\x63urrent_num\x18\x03 \x01(\x03\x12\x17\n\x0fis_fetch_reward\x18\x04 \x01(\x08\x12\x39\n\x0cmulti_reward\x18\x05 \x03(\x0b\x32#.pb.NewComersGuideMissionRewardItem\x12\x0c\n\x04lock\x18\x06 \x01(\x08\"z\n\x1fNewComersGuideMissionRewardItem\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.pb.NewComersGuideMissionRewardType\x12\x0b\n\x03num\x18\x02 \x01(\x03\x12\x17\n\x0fitem_class_name\x18\x03 \x01(\t\"0\n!iGetNewComersGuideMissionGroupREQ\x12\x0b\n\x03uid\x18\x01 \x01(\x03\"\x82\x01\n!iGetNewComersGuideMissionGroupRSP\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.pb.iErrorCode\x12\x30\n\x04info\x18\x02 \x01(\x0b\x32\".pb.NewComersGuideMissionGroupInfo\x12\r\n\x05phase\x18\x03 \x01(\x05*\xb6\x01\n\x1fNewComersGuideMissionRewardType\x12\x30\n,NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_DEFAULT\x10\x00\x12-\n)NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_ITEM\x10\x01\x12\x32\n.NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_CASH_BACK\x10\x02\x42\x07Z\x05../pb')
  ,
  dependencies=[base2__pb2.DESCRIPTOR,])

_NEWCOMERSGUIDEMISSIONREWARDTYPE = _descriptor.EnumDescriptor(
  name='NewComersGuideMissionRewardType',
  full_name='pb.NewComersGuideMissionRewardType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_ITEM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_CASH_BACK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=678,
  serialized_end=860,
)
_sym_db.RegisterEnumDescriptor(_NEWCOMERSGUIDEMISSIONREWARDTYPE)

NewComersGuideMissionRewardType = enum_type_wrapper.EnumTypeWrapper(_NEWCOMERSGUIDEMISSIONREWARDTYPE)
NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_DEFAULT = 0
NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_ITEM = 1
NEW_COMERS_GUIDE_MISSION_REWARD_TYPE_CASH_BACK = 2



_NEWCOMERSGUIDEMISSIONGROUPINFO = _descriptor.Descriptor(
  name='NewComersGuideMissionGroupInfo',
  full_name='pb.NewComersGuideMissionGroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='pb.NewComersGuideMissionGroupInfo.group_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity', full_name='pb.NewComersGuideMissionGroupInfo.identity', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infos', full_name='pb.NewComersGuideMissionGroupInfo.infos', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expired_time', full_name='pb.NewComersGuideMissionGroupInfo.expired_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=50,
  serialized_end=186,
)


_NEWCOMERSGUIDEMISSIONINFO = _descriptor.Descriptor(
  name='NewComersGuideMissionInfo',
  full_name='pb.NewComersGuideMissionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.NewComersGuideMissionInfo.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_num', full_name='pb.NewComersGuideMissionInfo.content_num', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_num', full_name='pb.NewComersGuideMissionInfo.current_num', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_fetch_reward', full_name='pb.NewComersGuideMissionInfo.is_fetch_reward', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_reward', full_name='pb.NewComersGuideMissionInfo.multi_reward', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lock', full_name='pb.NewComersGuideMissionInfo.lock', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=189,
  serialized_end=368,
)


_NEWCOMERSGUIDEMISSIONREWARDITEM = _descriptor.Descriptor(
  name='NewComersGuideMissionRewardItem',
  full_name='pb.NewComersGuideMissionRewardItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.NewComersGuideMissionRewardItem.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='pb.NewComersGuideMissionRewardItem.num', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_class_name', full_name='pb.NewComersGuideMissionRewardItem.item_class_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=370,
  serialized_end=492,
)


_IGETNEWCOMERSGUIDEMISSIONGROUPREQ = _descriptor.Descriptor(
  name='iGetNewComersGuideMissionGroupREQ',
  full_name='pb.iGetNewComersGuideMissionGroupREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pb.iGetNewComersGuideMissionGroupREQ.uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=494,
  serialized_end=542,
)


_IGETNEWCOMERSGUIDEMISSIONGROUPRSP = _descriptor.Descriptor(
  name='iGetNewComersGuideMissionGroupRSP',
  full_name='pb.iGetNewComersGuideMissionGroupRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.iGetNewComersGuideMissionGroupRSP.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='pb.iGetNewComersGuideMissionGroupRSP.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='pb.iGetNewComersGuideMissionGroupRSP.phase', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=545,
  serialized_end=675,
)

_NEWCOMERSGUIDEMISSIONGROUPINFO.fields_by_name['infos'].message_type = _NEWCOMERSGUIDEMISSIONINFO
_NEWCOMERSGUIDEMISSIONINFO.fields_by_name['multi_reward'].message_type = _NEWCOMERSGUIDEMISSIONREWARDITEM
_NEWCOMERSGUIDEMISSIONREWARDITEM.fields_by_name['type'].enum_type = _NEWCOMERSGUIDEMISSIONREWARDTYPE
_IGETNEWCOMERSGUIDEMISSIONGROUPRSP.fields_by_name['code'].enum_type = base2__pb2._IERRORCODE
_IGETNEWCOMERSGUIDEMISSIONGROUPRSP.fields_by_name['info'].message_type = _NEWCOMERSGUIDEMISSIONGROUPINFO
DESCRIPTOR.message_types_by_name['NewComersGuideMissionGroupInfo'] = _NEWCOMERSGUIDEMISSIONGROUPINFO
DESCRIPTOR.message_types_by_name['NewComersGuideMissionInfo'] = _NEWCOMERSGUIDEMISSIONINFO
DESCRIPTOR.message_types_by_name['NewComersGuideMissionRewardItem'] = _NEWCOMERSGUIDEMISSIONREWARDITEM
DESCRIPTOR.message_types_by_name['iGetNewComersGuideMissionGroupREQ'] = _IGETNEWCOMERSGUIDEMISSIONGROUPREQ
DESCRIPTOR.message_types_by_name['iGetNewComersGuideMissionGroupRSP'] = _IGETNEWCOMERSGUIDEMISSIONGROUPRSP
DESCRIPTOR.enum_types_by_name['NewComersGuideMissionRewardType'] = _NEWCOMERSGUIDEMISSIONREWARDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewComersGuideMissionGroupInfo = _reflection.GeneratedProtocolMessageType('NewComersGuideMissionGroupInfo', (_message.Message,), dict(
  DESCRIPTOR = _NEWCOMERSGUIDEMISSIONGROUPINFO,
  __module__ = 'inner_new_comers_guide_pb2'
  # @@protoc_insertion_point(class_scope:pb.NewComersGuideMissionGroupInfo)
  ))
_sym_db.RegisterMessage(NewComersGuideMissionGroupInfo)

NewComersGuideMissionInfo = _reflection.GeneratedProtocolMessageType('NewComersGuideMissionInfo', (_message.Message,), dict(
  DESCRIPTOR = _NEWCOMERSGUIDEMISSIONINFO,
  __module__ = 'inner_new_comers_guide_pb2'
  # @@protoc_insertion_point(class_scope:pb.NewComersGuideMissionInfo)
  ))
_sym_db.RegisterMessage(NewComersGuideMissionInfo)

NewComersGuideMissionRewardItem = _reflection.GeneratedProtocolMessageType('NewComersGuideMissionRewardItem', (_message.Message,), dict(
  DESCRIPTOR = _NEWCOMERSGUIDEMISSIONREWARDITEM,
  __module__ = 'inner_new_comers_guide_pb2'
  # @@protoc_insertion_point(class_scope:pb.NewComersGuideMissionRewardItem)
  ))
_sym_db.RegisterMessage(NewComersGuideMissionRewardItem)

iGetNewComersGuideMissionGroupREQ = _reflection.GeneratedProtocolMessageType('iGetNewComersGuideMissionGroupREQ', (_message.Message,), dict(
  DESCRIPTOR = _IGETNEWCOMERSGUIDEMISSIONGROUPREQ,
  __module__ = 'inner_new_comers_guide_pb2'
  # @@protoc_insertion_point(class_scope:pb.iGetNewComersGuideMissionGroupREQ)
  ))
_sym_db.RegisterMessage(iGetNewComersGuideMissionGroupREQ)

iGetNewComersGuideMissionGroupRSP = _reflection.GeneratedProtocolMessageType('iGetNewComersGuideMissionGroupRSP', (_message.Message,), dict(
  DESCRIPTOR = _IGETNEWCOMERSGUIDEMISSIONGROUPRSP,
  __module__ = 'inner_new_comers_guide_pb2'
  # @@protoc_insertion_point(class_scope:pb.iGetNewComersGuideMissionGroupRSP)
  ))
_sym_db.RegisterMessage(iGetNewComersGuideMissionGroupRSP)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
