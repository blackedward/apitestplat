# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inner_counter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base2_pb2 as base2__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inner_counter.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x13inner_counter.proto\x12\x02pb\x1a\x0b\x62\x61se2.proto\"\xd4\x03\n\x1fiSetAdminCounterTransferFlowREQ\x12\x0e\n\x06to_uid\x18\x01 \x01(\x03\x12?\n\tflow_type\x18\x02 \x01(\x0e\x32,.pb.iSetAdminCounterTransferFlowREQ.FlowType\x12\r\n\x05money\x18\x03 \x01(\x03\x12\x15\n\ritem_class_id\x18\x04 \x01(\x03\x12\x17\n\x0fitem_class_name\x18\x05 \x01(\t\x12\x16\n\x0eitem_class_num\x18\x06 \x01(\x05\x12\x0c\n\x04time\x18\x07 \x01(\x03\x12\x1b\n\x13\x62lind_coin_class_id\x18\x08 \x01(\x03\x12\x1d\n\x15\x62lind_coin_class_name\x18\t \x01(\t\x12\x1b\n\x13\x62lind_balance_value\x18\n \x01(\x03\x12\r\n\x05point\x18\x0b \x01(\x03\x12\x17\n\x0f\x63\x61sh_back_quota\x18\x0c \x01(\x03\x12\x12\n\nfree_chips\x18\r \x01(\x03\"f\n\x08\x46lowType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\t\n\x05MONEY\x10\x01\x12\x08\n\x04ITEM\x10\x02\x12\x0e\n\nBLIND_COIN\x10\x03\x12\t\n\x05POINT\x10\x04\x12\r\n\tCASH_BACK\x10\x05\x12\x0e\n\nFREE_CHIPS\x10\x06\"?\n\x1fiSetAdminCounterTransferFlowRSP\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.pb.iErrorCode\"l\n\x16iAdminChangeValueV2REQ\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0e\n\x06\x63hange\x18\x02 \x01(\x03\x12\x0e\n\x06\x61ttach\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x13\n\x0bneed_frozen\x18\x05 \x01(\x08\"D\n\x16iAdminChangeValueV2RSP\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.pb.iErrorCode\x12\x0c\n\x04left\x18\x02 \x01(\x03\"[\n\x15iAdminClearValueV2REQ\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0e\n\x06\x61ttach\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x13\n\x0bneed_frozen\x18\x04 \x01(\x08\"E\n\x15iAdminClearValueV2RSP\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.pb.iErrorCode\x12\x0e\n\x06\x63hange\x18\x02 \x01(\x03\x42\x07Z\x05../pb')
  ,
  dependencies=[base2__pb2.DESCRIPTOR,])



_ISETADMINCOUNTERTRANSFERFLOWREQ_FLOWTYPE = _descriptor.EnumDescriptor(
  name='FlowType',
  full_name='pb.iSetAdminCounterTransferFlowREQ.FlowType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLIND_COIN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POINT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASH_BACK', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREE_CHIPS', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=407,
  serialized_end=509,
)
_sym_db.RegisterEnumDescriptor(_ISETADMINCOUNTERTRANSFERFLOWREQ_FLOWTYPE)


_ISETADMINCOUNTERTRANSFERFLOWREQ = _descriptor.Descriptor(
  name='iSetAdminCounterTransferFlowREQ',
  full_name='pb.iSetAdminCounterTransferFlowREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to_uid', full_name='pb.iSetAdminCounterTransferFlowREQ.to_uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flow_type', full_name='pb.iSetAdminCounterTransferFlowREQ.flow_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='pb.iSetAdminCounterTransferFlowREQ.money', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_class_id', full_name='pb.iSetAdminCounterTransferFlowREQ.item_class_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_class_name', full_name='pb.iSetAdminCounterTransferFlowREQ.item_class_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_class_num', full_name='pb.iSetAdminCounterTransferFlowREQ.item_class_num', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='pb.iSetAdminCounterTransferFlowREQ.time', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blind_coin_class_id', full_name='pb.iSetAdminCounterTransferFlowREQ.blind_coin_class_id', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blind_coin_class_name', full_name='pb.iSetAdminCounterTransferFlowREQ.blind_coin_class_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blind_balance_value', full_name='pb.iSetAdminCounterTransferFlowREQ.blind_balance_value', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point', full_name='pb.iSetAdminCounterTransferFlowREQ.point', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cash_back_quota', full_name='pb.iSetAdminCounterTransferFlowREQ.cash_back_quota', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_chips', full_name='pb.iSetAdminCounterTransferFlowREQ.free_chips', index=12,
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
    _ISETADMINCOUNTERTRANSFERFLOWREQ_FLOWTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=509,
)


_ISETADMINCOUNTERTRANSFERFLOWRSP = _descriptor.Descriptor(
  name='iSetAdminCounterTransferFlowRSP',
  full_name='pb.iSetAdminCounterTransferFlowRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.iSetAdminCounterTransferFlowRSP.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=511,
  serialized_end=574,
)


_IADMINCHANGEVALUEV2REQ = _descriptor.Descriptor(
  name='iAdminChangeValueV2REQ',
  full_name='pb.iAdminChangeValueV2REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pb.iAdminChangeValueV2REQ.uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change', full_name='pb.iAdminChangeValueV2REQ.change', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attach', full_name='pb.iAdminChangeValueV2REQ.attach', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='pb.iAdminChangeValueV2REQ.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_frozen', full_name='pb.iAdminChangeValueV2REQ.need_frozen', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=576,
  serialized_end=684,
)


_IADMINCHANGEVALUEV2RSP = _descriptor.Descriptor(
  name='iAdminChangeValueV2RSP',
  full_name='pb.iAdminChangeValueV2RSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.iAdminChangeValueV2RSP.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='pb.iAdminChangeValueV2RSP.left', index=1,
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
  serialized_start=686,
  serialized_end=754,
)


_IADMINCLEARVALUEV2REQ = _descriptor.Descriptor(
  name='iAdminClearValueV2REQ',
  full_name='pb.iAdminClearValueV2REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='pb.iAdminClearValueV2REQ.uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attach', full_name='pb.iAdminClearValueV2REQ.attach', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='pb.iAdminClearValueV2REQ.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_frozen', full_name='pb.iAdminClearValueV2REQ.need_frozen', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=756,
  serialized_end=847,
)


_IADMINCLEARVALUEV2RSP = _descriptor.Descriptor(
  name='iAdminClearValueV2RSP',
  full_name='pb.iAdminClearValueV2RSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.iAdminClearValueV2RSP.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change', full_name='pb.iAdminClearValueV2RSP.change', index=1,
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
  serialized_start=849,
  serialized_end=918,
)

_ISETADMINCOUNTERTRANSFERFLOWREQ.fields_by_name['flow_type'].enum_type = _ISETADMINCOUNTERTRANSFERFLOWREQ_FLOWTYPE
_ISETADMINCOUNTERTRANSFERFLOWREQ_FLOWTYPE.containing_type = _ISETADMINCOUNTERTRANSFERFLOWREQ
_ISETADMINCOUNTERTRANSFERFLOWRSP.fields_by_name['code'].enum_type = base2__pb2._IERRORCODE
_IADMINCHANGEVALUEV2RSP.fields_by_name['code'].enum_type = base2__pb2._IERRORCODE
_IADMINCLEARVALUEV2RSP.fields_by_name['code'].enum_type = base2__pb2._IERRORCODE
DESCRIPTOR.message_types_by_name['iSetAdminCounterTransferFlowREQ'] = _ISETADMINCOUNTERTRANSFERFLOWREQ
DESCRIPTOR.message_types_by_name['iSetAdminCounterTransferFlowRSP'] = _ISETADMINCOUNTERTRANSFERFLOWRSP
DESCRIPTOR.message_types_by_name['iAdminChangeValueV2REQ'] = _IADMINCHANGEVALUEV2REQ
DESCRIPTOR.message_types_by_name['iAdminChangeValueV2RSP'] = _IADMINCHANGEVALUEV2RSP
DESCRIPTOR.message_types_by_name['iAdminClearValueV2REQ'] = _IADMINCLEARVALUEV2REQ
DESCRIPTOR.message_types_by_name['iAdminClearValueV2RSP'] = _IADMINCLEARVALUEV2RSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

iSetAdminCounterTransferFlowREQ = _reflection.GeneratedProtocolMessageType('iSetAdminCounterTransferFlowREQ', (_message.Message,), dict(
  DESCRIPTOR = _ISETADMINCOUNTERTRANSFERFLOWREQ,
  __module__ = 'inner_counter_pb2'
  # @@protoc_insertion_point(class_scope:pb.iSetAdminCounterTransferFlowREQ)
  ))
_sym_db.RegisterMessage(iSetAdminCounterTransferFlowREQ)

iSetAdminCounterTransferFlowRSP = _reflection.GeneratedProtocolMessageType('iSetAdminCounterTransferFlowRSP', (_message.Message,), dict(
  DESCRIPTOR = _ISETADMINCOUNTERTRANSFERFLOWRSP,
  __module__ = 'inner_counter_pb2'
  # @@protoc_insertion_point(class_scope:pb.iSetAdminCounterTransferFlowRSP)
  ))
_sym_db.RegisterMessage(iSetAdminCounterTransferFlowRSP)

iAdminChangeValueV2REQ = _reflection.GeneratedProtocolMessageType('iAdminChangeValueV2REQ', (_message.Message,), dict(
  DESCRIPTOR = _IADMINCHANGEVALUEV2REQ,
  __module__ = 'inner_counter_pb2'
  # @@protoc_insertion_point(class_scope:pb.iAdminChangeValueV2REQ)
  ))
_sym_db.RegisterMessage(iAdminChangeValueV2REQ)

iAdminChangeValueV2RSP = _reflection.GeneratedProtocolMessageType('iAdminChangeValueV2RSP', (_message.Message,), dict(
  DESCRIPTOR = _IADMINCHANGEVALUEV2RSP,
  __module__ = 'inner_counter_pb2'
  # @@protoc_insertion_point(class_scope:pb.iAdminChangeValueV2RSP)
  ))
_sym_db.RegisterMessage(iAdminChangeValueV2RSP)

iAdminClearValueV2REQ = _reflection.GeneratedProtocolMessageType('iAdminClearValueV2REQ', (_message.Message,), dict(
  DESCRIPTOR = _IADMINCLEARVALUEV2REQ,
  __module__ = 'inner_counter_pb2'
  # @@protoc_insertion_point(class_scope:pb.iAdminClearValueV2REQ)
  ))
_sym_db.RegisterMessage(iAdminClearValueV2REQ)

iAdminClearValueV2RSP = _reflection.GeneratedProtocolMessageType('iAdminClearValueV2RSP', (_message.Message,), dict(
  DESCRIPTOR = _IADMINCLEARVALUEV2RSP,
  __module__ = 'inner_counter_pb2'
  # @@protoc_insertion_point(class_scope:pb.iAdminClearValueV2RSP)
  ))
_sym_db.RegisterMessage(iAdminClearValueV2RSP)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
