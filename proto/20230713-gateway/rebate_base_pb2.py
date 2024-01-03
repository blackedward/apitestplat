# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rebate_base.proto

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
  name='rebate_base.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x11rebate_base.proto\x12\x02pb*+\n\nRebateType\x12\x08\n\x04USER\x10\x01\x12\x08\n\x04HOST\x10\x02\x12\t\n\x05\x41GENT\x10\x03*{\n\tClaimType\x12\n\n\x06MANUAL\x10\x00\x12\x11\n\rEXPIRED_CLAIM\x10\x01\x12\x0f\n\x0b\x43HANGE_ROLE\x10\x02\x12\x14\n\x10REMOVE_FROM_CLUB\x10\x03\x12\x0f\n\x0b\x43HANGE_CLUB\x10\x04\x12\x17\n\x13INDEFINITELY_BANNED\x10\x05\x42\x07Z\x05../pb')
)

_REBATETYPE = _descriptor.EnumDescriptor(
  name='RebateType',
  full_name='pb.RebateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=25,
  serialized_end=68,
)
_sym_db.RegisterEnumDescriptor(_REBATETYPE)

RebateType = enum_type_wrapper.EnumTypeWrapper(_REBATETYPE)
_CLAIMTYPE = _descriptor.EnumDescriptor(
  name='ClaimType',
  full_name='pb.ClaimType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED_CLAIM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_ROLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_FROM_CLUB', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_CLUB', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEFINITELY_BANNED', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=70,
  serialized_end=193,
)
_sym_db.RegisterEnumDescriptor(_CLAIMTYPE)

ClaimType = enum_type_wrapper.EnumTypeWrapper(_CLAIMTYPE)
USER = 1
HOST = 2
AGENT = 3
MANUAL = 0
EXPIRED_CLAIM = 1
CHANGE_ROLE = 2
REMOVE_FROM_CLUB = 3
CHANGE_CLUB = 4
INDEFINITELY_BANNED = 5


DESCRIPTOR.enum_types_by_name['RebateType'] = _REBATETYPE
DESCRIPTOR.enum_types_by_name['ClaimType'] = _CLAIMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
