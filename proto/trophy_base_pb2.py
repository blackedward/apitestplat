# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trophy_base.proto

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
  name='trophy_base.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\x11trophy_base.proto\x12\x02pb*\x85\x01\n\x0eTrophyTierType\x12\x1c\n\x18TROPHY_TIER_TYPE_DEFAULT\x10\x00\x12\x1b\n\x17TROPHY_TIER_TYPE_BRONZE\x10\x01\x12\x1b\n\x17TROPHY_TIER_TYPE_SILVER\x10\x02\x12\x1b\n\x17TROPHY_TIER_TYPE_GOLDEN\x10\x03*s\n\x0fTrophyClassType\x12!\n\x1dTROPHY_CLASS_TYPE_ACHIEVEMENT\x10\x00\x12 \n\x1cTROPHY_CLASS_TYPE_TOURNAMENT\x10\x01\x12\x1b\n\x17TROPHY_CLASS_TYPE_EVENT\x10\x02\x42\x07Z\x05../pb')
)

_TROPHYTIERTYPE = _descriptor.EnumDescriptor(
  name='TrophyTierType',
  full_name='pb.TrophyTierType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TROPHY_TIER_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TROPHY_TIER_TYPE_BRONZE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TROPHY_TIER_TYPE_SILVER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TROPHY_TIER_TYPE_GOLDEN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=26,
  serialized_end=159,
)
_sym_db.RegisterEnumDescriptor(_TROPHYTIERTYPE)

TrophyTierType = enum_type_wrapper.EnumTypeWrapper(_TROPHYTIERTYPE)
_TROPHYCLASSTYPE = _descriptor.EnumDescriptor(
  name='TrophyClassType',
  full_name='pb.TrophyClassType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TROPHY_CLASS_TYPE_ACHIEVEMENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TROPHY_CLASS_TYPE_TOURNAMENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TROPHY_CLASS_TYPE_EVENT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_TROPHYCLASSTYPE)

TrophyClassType = enum_type_wrapper.EnumTypeWrapper(_TROPHYCLASSTYPE)
TROPHY_TIER_TYPE_DEFAULT = 0
TROPHY_TIER_TYPE_BRONZE = 1
TROPHY_TIER_TYPE_SILVER = 2
TROPHY_TIER_TYPE_GOLDEN = 3
TROPHY_CLASS_TYPE_ACHIEVEMENT = 0
TROPHY_CLASS_TYPE_TOURNAMENT = 1
TROPHY_CLASS_TYPE_EVENT = 2


DESCRIPTOR.enum_types_by_name['TrophyTierType'] = _TROPHYTIERTYPE
DESCRIPTOR.enum_types_by_name['TrophyClassType'] = _TROPHYCLASSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
