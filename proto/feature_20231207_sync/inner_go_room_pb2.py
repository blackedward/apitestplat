# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inner_go_room.proto

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
  name='inner_go_room.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x13inner_go_room.proto\x12\x02pb\x1a\x0b\x62\x61se2.proto\"\xa7\x01\n\x13iSetGoRoomRecordREQ\x12\x31\n\x08set_type\x18\x01 \x01(\x0e\x32\x1f.pb.iSetGoRoomRecordREQ.SetType\x12\x0b\n\x03uid\x18\x02 \x01(\x03\"P\n\x07SetType\x12\x18\n\x14SK_RECORD_PLAYER_WIN\x10\x01\x12\x18\n\x14SK_RECORD_BANKER_WIN\x10\x02\x12\x11\n\rSK_RECORD_TIE\x10\x03\x42\x07Z\x05../pb')
  ,
  dependencies=[base2__pb2.DESCRIPTOR,])



_ISETGOROOMRECORDREQ_SETTYPE = _descriptor.EnumDescriptor(
  name='SetType',
  full_name='pb.iSetGoRoomRecordREQ.SetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SK_RECORD_PLAYER_WIN', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SK_RECORD_BANKER_WIN', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SK_RECORD_TIE', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=128,
  serialized_end=208,
)
_sym_db.RegisterEnumDescriptor(_ISETGOROOMRECORDREQ_SETTYPE)


_ISETGOROOMRECORDREQ = _descriptor.Descriptor(
  name='iSetGoRoomRecordREQ',
  full_name='pb.iSetGoRoomRecordREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='set_type', full_name='pb.iSetGoRoomRecordREQ.set_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='pb.iSetGoRoomRecordREQ.uid', index=1,
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
    _ISETGOROOMRECORDREQ_SETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=208,
)

_ISETGOROOMRECORDREQ.fields_by_name['set_type'].enum_type = _ISETGOROOMRECORDREQ_SETTYPE
_ISETGOROOMRECORDREQ_SETTYPE.containing_type = _ISETGOROOMRECORDREQ
DESCRIPTOR.message_types_by_name['iSetGoRoomRecordREQ'] = _ISETGOROOMRECORDREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

iSetGoRoomRecordREQ = _reflection.GeneratedProtocolMessageType('iSetGoRoomRecordREQ', (_message.Message,), dict(
  DESCRIPTOR = _ISETGOROOMRECORDREQ,
  __module__ = 'inner_go_room_pb2'
  # @@protoc_insertion_point(class_scope:pb.iSetGoRoomRecordREQ)
  ))
_sym_db.RegisterMessage(iSetGoRoomRecordREQ)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
