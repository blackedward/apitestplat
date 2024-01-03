# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rebate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rebate_base_pb2 as rebate__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rebate.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x0crebate.proto\x12\x02pb\x1a\x11rebate_base.proto\"3\n\x12GetUserRBStatusREQ\x12\x0b\n\x03uid\x18\x01 \x02(\x03\x12\x10\n\x08timezone\x18\x02 \x02(\x05\"\xce\x02\n\x12GetUserRBStatusRSP\x12 \n\x06status\x18\x01 \x02(\x0e\x32\x10.pb.RebateStatus\x12\x11\n\tmin_level\x18\x02 \x01(\x05\x12\x11\n\tmax_level\x18\x03 \x01(\x05\x12\x15\n\rcurrent_level\x18\x04 \x01(\x05\x12\x13\n\x0b\x63urrent_ggr\x18\x05 \x01(\x03\x12\x10\n\x08next_ggr\x18\x06 \x01(\x03\x12\x16\n\x0ekeep_level_ggr\x18\x07 \x01(\x03\x12\x17\n\x0freset_timestamp\x18\x08 \x01(\x03\x12\x16\n\x0erebate_percent\x18\t \x01(\x05\x12\x1a\n\x12\x63urrent_rebate_sum\x18\n \x01(\x03\x12 \n\x18rebate_percent_from_club\x18\x0b \x01(\x05\x12\x12\n\nclaim_pool\x18\x0c \x01(\x03\x12\x17\n\x0f\x61uto_claim_time\x18\r \x01(\x03\"R\n\x10UserRebateRecord\x12\r\n\x05setid\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0e\n\x06rebate\x18\x04 \x01(\x03\"q\n\x12GetUserRBRecordREQ\x12\x0b\n\x03uid\x18\x01 \x02(\x03\x12\x12\n\nstart_date\x18\x02 \x02(\x05\x12\x10\n\x08\x65nd_date\x18\x03 \x02(\x05\x12\x16\n\x0bstart_index\x18\x04 \x01(\x05:\x01\x31\x12\x10\n\x08timezone\x18\x05 \x02(\x05\"x\n\x12GetUserRBRecordRSP\x12$\n\x06record\x18\x01 \x03(\x0b\x32\x14.pb.UserRebateRecord\x12\x13\n\x0bstart_index\x18\x02 \x01(\x05\x12\x11\n\ttotal_num\x18\x03 \x01(\x05\x12\x14\n\x0ctotal_rebate\x18\x04 \x01(\x03\"H\n\x0c\x43laimPoolREQ\x12\x0f\n\x07\x63lub_id\x18\x01 \x01(\x03\x12\'\n\x0f\x63laim_pool_type\x18\x02 \x02(\x0e\x32\x0e.pb.RebateType\"0\n\x0c\x43laimPoolRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x12\n\nclaim_pool\x18\x02 \x01(\x03*2\n\x0cRebateStatus\x12\x16\n\tUNDEFINED\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\n\n\x06NORMAL\x10\x00\x42\x07Z\x05../pb')
  ,
  dependencies=[rebate__base__pb2.DESCRIPTOR,])

_REBATESTATUS = _descriptor.EnumDescriptor(
  name='RebateStatus',
  full_name='pb.RebateStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=-1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=874,
  serialized_end=924,
)
_sym_db.RegisterEnumDescriptor(_REBATESTATUS)

RebateStatus = enum_type_wrapper.EnumTypeWrapper(_REBATESTATUS)
UNDEFINED = -1
NORMAL = 0



_GETUSERRBSTATUSREQ = _descriptor.Descriptor(
  name='GetUserRBStatusREQ',
  full_name='pb.GetUserRBStatusREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pb.GetUserRBStatusREQ.uid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='pb.GetUserRBStatusREQ.timezone', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=39,
  serialized_end=90,
)


_GETUSERRBSTATUSRSP = _descriptor.Descriptor(
  name='GetUserRBStatusRSP',
  full_name='pb.GetUserRBStatusRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pb.GetUserRBStatusRSP.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_level', full_name='pb.GetUserRBStatusRSP.min_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_level', full_name='pb.GetUserRBStatusRSP.max_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_level', full_name='pb.GetUserRBStatusRSP.current_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_ggr', full_name='pb.GetUserRBStatusRSP.current_ggr', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_ggr', full_name='pb.GetUserRBStatusRSP.next_ggr', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keep_level_ggr', full_name='pb.GetUserRBStatusRSP.keep_level_ggr', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_timestamp', full_name='pb.GetUserRBStatusRSP.reset_timestamp', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate_percent', full_name='pb.GetUserRBStatusRSP.rebate_percent', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_rebate_sum', full_name='pb.GetUserRBStatusRSP.current_rebate_sum', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate_percent_from_club', full_name='pb.GetUserRBStatusRSP.rebate_percent_from_club', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claim_pool', full_name='pb.GetUserRBStatusRSP.claim_pool', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_claim_time', full_name='pb.GetUserRBStatusRSP.auto_claim_time', index=12,
      number=13, type=3, cpp_type=2, label=1,
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
  serialized_start=93,
  serialized_end=427,
)


_USERREBATERECORD = _descriptor.Descriptor(
  name='UserRebateRecord',
  full_name='pb.UserRebateRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setid', full_name='pb.UserRebateRecord.setid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pb.UserRebateRecord.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='pb.UserRebateRecord.desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.UserRebateRecord.rebate', index=3,
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
  serialized_start=429,
  serialized_end=511,
)


_GETUSERRBRECORDREQ = _descriptor.Descriptor(
  name='GetUserRBRecordREQ',
  full_name='pb.GetUserRBRecordREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pb.GetUserRBRecordREQ.uid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='pb.GetUserRBRecordREQ.start_date', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='pb.GetUserRBRecordREQ.end_date', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_index', full_name='pb.GetUserRBRecordREQ.start_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='pb.GetUserRBRecordREQ.timezone', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=513,
  serialized_end=626,
)


_GETUSERRBRECORDRSP = _descriptor.Descriptor(
  name='GetUserRBRecordRSP',
  full_name='pb.GetUserRBRecordRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='pb.GetUserRBRecordRSP.record', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_index', full_name='pb.GetUserRBRecordRSP.start_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_num', full_name='pb.GetUserRBRecordRSP.total_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_rebate', full_name='pb.GetUserRBRecordRSP.total_rebate', index=3,
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
  serialized_start=628,
  serialized_end=748,
)


_CLAIMPOOLREQ = _descriptor.Descriptor(
  name='ClaimPoolREQ',
  full_name='pb.ClaimPoolREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='club_id', full_name='pb.ClaimPoolREQ.club_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claim_pool_type', full_name='pb.ClaimPoolREQ.claim_pool_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=750,
  serialized_end=822,
)


_CLAIMPOOLRSP = _descriptor.Descriptor(
  name='ClaimPoolRSP',
  full_name='pb.ClaimPoolRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.ClaimPoolRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claim_pool', full_name='pb.ClaimPoolRSP.claim_pool', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=824,
  serialized_end=872,
)

_GETUSERRBSTATUSRSP.fields_by_name['status'].enum_type = _REBATESTATUS
_GETUSERRBRECORDRSP.fields_by_name['record'].message_type = _USERREBATERECORD
_CLAIMPOOLREQ.fields_by_name['claim_pool_type'].enum_type = rebate__base__pb2._REBATETYPE
DESCRIPTOR.message_types_by_name['GetUserRBStatusREQ'] = _GETUSERRBSTATUSREQ
DESCRIPTOR.message_types_by_name['GetUserRBStatusRSP'] = _GETUSERRBSTATUSRSP
DESCRIPTOR.message_types_by_name['UserRebateRecord'] = _USERREBATERECORD
DESCRIPTOR.message_types_by_name['GetUserRBRecordREQ'] = _GETUSERRBRECORDREQ
DESCRIPTOR.message_types_by_name['GetUserRBRecordRSP'] = _GETUSERRBRECORDRSP
DESCRIPTOR.message_types_by_name['ClaimPoolREQ'] = _CLAIMPOOLREQ
DESCRIPTOR.message_types_by_name['ClaimPoolRSP'] = _CLAIMPOOLRSP
DESCRIPTOR.enum_types_by_name['RebateStatus'] = _REBATESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserRBStatusREQ = _reflection.GeneratedProtocolMessageType('GetUserRBStatusREQ', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERRBSTATUSREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetUserRBStatusREQ)
  ))
_sym_db.RegisterMessage(GetUserRBStatusREQ)

GetUserRBStatusRSP = _reflection.GeneratedProtocolMessageType('GetUserRBStatusRSP', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERRBSTATUSRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetUserRBStatusRSP)
  ))
_sym_db.RegisterMessage(GetUserRBStatusRSP)

UserRebateRecord = _reflection.GeneratedProtocolMessageType('UserRebateRecord', (_message.Message,), dict(
  DESCRIPTOR = _USERREBATERECORD,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.UserRebateRecord)
  ))
_sym_db.RegisterMessage(UserRebateRecord)

GetUserRBRecordREQ = _reflection.GeneratedProtocolMessageType('GetUserRBRecordREQ', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERRBRECORDREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetUserRBRecordREQ)
  ))
_sym_db.RegisterMessage(GetUserRBRecordREQ)

GetUserRBRecordRSP = _reflection.GeneratedProtocolMessageType('GetUserRBRecordRSP', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERRBRECORDRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.GetUserRBRecordRSP)
  ))
_sym_db.RegisterMessage(GetUserRBRecordRSP)

ClaimPoolREQ = _reflection.GeneratedProtocolMessageType('ClaimPoolREQ', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMPOOLREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClaimPoolREQ)
  ))
_sym_db.RegisterMessage(ClaimPoolREQ)

ClaimPoolRSP = _reflection.GeneratedProtocolMessageType('ClaimPoolRSP', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMPOOLRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClaimPoolRSP)
  ))
_sym_db.RegisterMessage(ClaimPoolRSP)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
