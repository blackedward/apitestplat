# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pine1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_pb2 as base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pine1.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x0bpine1.proto\x12\x02pb\x1a\nbase.proto\" \n\x0ePineStandUpBRC\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\"@\n\rPineLookerRSP\x12\x1b\n\x04user\x18\x01 \x03(\x0b\x32\r.pb.UserBrief\x12\x12\n\nlooker_num\x18\x02 \x01(\x05\"\x1c\n\rPineLookerREQ\x12\x0b\n\x03tid\x18\x01 \x01(\x05\"\x13\n\x11PineProfitListREQ\"\x10\n\x0ePineStandUpREQ\"7\n\x12PineRebuyNotifyRSP\x12\x11\n\tleft_time\x18\x01 \x01(\x05\x12\x0e\n\x06seatid\x18\x02 \x01(\x05\"%\n\x14PineExchangeChipsREQ\x12\r\n\x05\x63hips\x18\x01 \x01(\x03\"\x16\n\x14PineAddActionTimeREQ\"5\n\x14PineExchangeChipsBRC\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\x12\r\n\x05\x63hips\x18\x02 \x01(\x03\"\'\n\x19LeaveRoomAfterThisHandREQ\x12\n\n\x02on\x18\x01 \x01(\x08\"5\n\x19LeaveRoomAfterThisHandRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\n\n\x02on\x18\x02 \x01(\x08\x42\x07Z\x05../pb')
  ,
  dependencies=[base__pb2.DESCRIPTOR,])




_PINESTANDUPBRC = _descriptor.Descriptor(
  name='PineStandUpBRC',
  full_name='pb.PineStandUpBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.PineStandUpBRC.seatid', index=0,
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
  serialized_start=31,
  serialized_end=63,
)


_PINELOOKERRSP = _descriptor.Descriptor(
  name='PineLookerRSP',
  full_name='pb.PineLookerRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='pb.PineLookerRSP.user', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='looker_num', full_name='pb.PineLookerRSP.looker_num', index=1,
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
  serialized_start=65,
  serialized_end=129,
)


_PINELOOKERREQ = _descriptor.Descriptor(
  name='PineLookerREQ',
  full_name='pb.PineLookerREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='pb.PineLookerREQ.tid', index=0,
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
  serialized_start=131,
  serialized_end=159,
)


_PINEPROFITLISTREQ = _descriptor.Descriptor(
  name='PineProfitListREQ',
  full_name='pb.PineProfitListREQ',
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
  serialized_start=161,
  serialized_end=180,
)


_PINESTANDUPREQ = _descriptor.Descriptor(
  name='PineStandUpREQ',
  full_name='pb.PineStandUpREQ',
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
  serialized_start=182,
  serialized_end=198,
)


_PINEREBUYNOTIFYRSP = _descriptor.Descriptor(
  name='PineRebuyNotifyRSP',
  full_name='pb.PineRebuyNotifyRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_time', full_name='pb.PineRebuyNotifyRSP.left_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.PineRebuyNotifyRSP.seatid', index=1,
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
  serialized_start=200,
  serialized_end=255,
)


_PINEEXCHANGECHIPSREQ = _descriptor.Descriptor(
  name='PineExchangeChipsREQ',
  full_name='pb.PineExchangeChipsREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chips', full_name='pb.PineExchangeChipsREQ.chips', index=0,
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
  serialized_start=257,
  serialized_end=294,
)


_PINEADDACTIONTIMEREQ = _descriptor.Descriptor(
  name='PineAddActionTimeREQ',
  full_name='pb.PineAddActionTimeREQ',
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
  serialized_start=296,
  serialized_end=318,
)


_PINEEXCHANGECHIPSBRC = _descriptor.Descriptor(
  name='PineExchangeChipsBRC',
  full_name='pb.PineExchangeChipsBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.PineExchangeChipsBRC.seatid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chips', full_name='pb.PineExchangeChipsBRC.chips', index=1,
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
  serialized_start=320,
  serialized_end=373,
)


_LEAVEROOMAFTERTHISHANDREQ = _descriptor.Descriptor(
  name='LeaveRoomAfterThisHandREQ',
  full_name='pb.LeaveRoomAfterThisHandREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='on', full_name='pb.LeaveRoomAfterThisHandREQ.on', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=375,
  serialized_end=414,
)


_LEAVEROOMAFTERTHISHANDRSP = _descriptor.Descriptor(
  name='LeaveRoomAfterThisHandRSP',
  full_name='pb.LeaveRoomAfterThisHandRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.LeaveRoomAfterThisHandRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='on', full_name='pb.LeaveRoomAfterThisHandRSP.on', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=416,
  serialized_end=469,
)

_PINELOOKERRSP.fields_by_name['user'].message_type = base__pb2._USERBRIEF
DESCRIPTOR.message_types_by_name['PineStandUpBRC'] = _PINESTANDUPBRC
DESCRIPTOR.message_types_by_name['PineLookerRSP'] = _PINELOOKERRSP
DESCRIPTOR.message_types_by_name['PineLookerREQ'] = _PINELOOKERREQ
DESCRIPTOR.message_types_by_name['PineProfitListREQ'] = _PINEPROFITLISTREQ
DESCRIPTOR.message_types_by_name['PineStandUpREQ'] = _PINESTANDUPREQ
DESCRIPTOR.message_types_by_name['PineRebuyNotifyRSP'] = _PINEREBUYNOTIFYRSP
DESCRIPTOR.message_types_by_name['PineExchangeChipsREQ'] = _PINEEXCHANGECHIPSREQ
DESCRIPTOR.message_types_by_name['PineAddActionTimeREQ'] = _PINEADDACTIONTIMEREQ
DESCRIPTOR.message_types_by_name['PineExchangeChipsBRC'] = _PINEEXCHANGECHIPSBRC
DESCRIPTOR.message_types_by_name['LeaveRoomAfterThisHandREQ'] = _LEAVEROOMAFTERTHISHANDREQ
DESCRIPTOR.message_types_by_name['LeaveRoomAfterThisHandRSP'] = _LEAVEROOMAFTERTHISHANDRSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PineStandUpBRC = _reflection.GeneratedProtocolMessageType('PineStandUpBRC', (_message.Message,), dict(
  DESCRIPTOR = _PINESTANDUPBRC,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineStandUpBRC)
  ))
_sym_db.RegisterMessage(PineStandUpBRC)

PineLookerRSP = _reflection.GeneratedProtocolMessageType('PineLookerRSP', (_message.Message,), dict(
  DESCRIPTOR = _PINELOOKERRSP,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineLookerRSP)
  ))
_sym_db.RegisterMessage(PineLookerRSP)

PineLookerREQ = _reflection.GeneratedProtocolMessageType('PineLookerREQ', (_message.Message,), dict(
  DESCRIPTOR = _PINELOOKERREQ,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineLookerREQ)
  ))
_sym_db.RegisterMessage(PineLookerREQ)

PineProfitListREQ = _reflection.GeneratedProtocolMessageType('PineProfitListREQ', (_message.Message,), dict(
  DESCRIPTOR = _PINEPROFITLISTREQ,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineProfitListREQ)
  ))
_sym_db.RegisterMessage(PineProfitListREQ)

PineStandUpREQ = _reflection.GeneratedProtocolMessageType('PineStandUpREQ', (_message.Message,), dict(
  DESCRIPTOR = _PINESTANDUPREQ,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineStandUpREQ)
  ))
_sym_db.RegisterMessage(PineStandUpREQ)

PineRebuyNotifyRSP = _reflection.GeneratedProtocolMessageType('PineRebuyNotifyRSP', (_message.Message,), dict(
  DESCRIPTOR = _PINEREBUYNOTIFYRSP,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineRebuyNotifyRSP)
  ))
_sym_db.RegisterMessage(PineRebuyNotifyRSP)

PineExchangeChipsREQ = _reflection.GeneratedProtocolMessageType('PineExchangeChipsREQ', (_message.Message,), dict(
  DESCRIPTOR = _PINEEXCHANGECHIPSREQ,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineExchangeChipsREQ)
  ))
_sym_db.RegisterMessage(PineExchangeChipsREQ)

PineAddActionTimeREQ = _reflection.GeneratedProtocolMessageType('PineAddActionTimeREQ', (_message.Message,), dict(
  DESCRIPTOR = _PINEADDACTIONTIMEREQ,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineAddActionTimeREQ)
  ))
_sym_db.RegisterMessage(PineAddActionTimeREQ)

PineExchangeChipsBRC = _reflection.GeneratedProtocolMessageType('PineExchangeChipsBRC', (_message.Message,), dict(
  DESCRIPTOR = _PINEEXCHANGECHIPSBRC,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.PineExchangeChipsBRC)
  ))
_sym_db.RegisterMessage(PineExchangeChipsBRC)

LeaveRoomAfterThisHandREQ = _reflection.GeneratedProtocolMessageType('LeaveRoomAfterThisHandREQ', (_message.Message,), dict(
  DESCRIPTOR = _LEAVEROOMAFTERTHISHANDREQ,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.LeaveRoomAfterThisHandREQ)
  ))
_sym_db.RegisterMessage(LeaveRoomAfterThisHandREQ)

LeaveRoomAfterThisHandRSP = _reflection.GeneratedProtocolMessageType('LeaveRoomAfterThisHandRSP', (_message.Message,), dict(
  DESCRIPTOR = _LEAVEROOMAFTERTHISHANDRSP,
  __module__ = 'pine1_pb2'
  # @@protoc_insertion_point(class_scope:pb.LeaveRoomAfterThisHandRSP)
  ))
_sym_db.RegisterMessage(LeaveRoomAfterThisHandRSP)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
