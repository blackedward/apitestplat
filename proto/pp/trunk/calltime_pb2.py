# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calltime.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pre_base_pb2 as pre__base__pb2
import pre_base1_pb2 as pre__base1__pb2
import base_pb2 as base__pb2
try:
  pre__base__pb2 = base__pb2.pre__base__pb2
except AttributeError:
  pre__base__pb2 = base__pb2.pre_base_pb2
try:
  pre__base1__pb2 = base__pb2.pre__base1__pb2
except AttributeError:
  pre__base1__pb2 = base__pb2.pre_base1_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='calltime.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\004./pb'),
  serialized_pb=_b('\n\x0e\x63\x61lltime.proto\x12\x02pb\x1a\x0epre_base.proto\x1a\x0fpre_base1.proto\x1a\nbase.proto\"\r\n\x0b\x43\x61llTimeREQ\"\xb5\x01\n\x0c\x43\x61llTimeInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12!\n\x19\x63onfirm_remaining_seconds\x18\x02 \x01(\x05\x12\x19\n\x11remaining_seconds\x18\x03 \x01(\x05\x12\'\n\rcalltime_code\x18\x04 \x01(\x0e\x32\x10.pb.CallTimeCode\x12-\n\x0c\x63onfirm_code\x18\x05 \x01(\x0e\x32\x17.pb.CallTimeConfirmCode\"6\n\x0b\x43\x61llTimeBRC\x12\'\n\rcalltime_info\x18\x01 \x01(\x0b\x32\x10.pb.CallTimeInfo\"a\n\x17\x43\x61llTimeEnterConfirmREQ\x12\x36\n\x0e\x63onfirm_status\x18\x01 \x01(\x0e\x32\x1e.pb.CallTimeEnterConfirmStatus\x12\x0e\n\x06seatid\x18\x02 \x01(\x05\"r\n\x17\x43\x61llTimeEnterConfirmRSP\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\x12\x1e\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x10.pb.BookSeatCode\x12\'\n\rcalltime_info\x18\x03 \x01(\x0b\x32\x10.pb.CallTimeInfo\"t\n\x1b\x43\x61llTimeEnterRoomConfirmBRC\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\x12\r\n\x05\x63hips\x18\x02 \x01(\x03\x12\x36\n\x0e\x63onfirm_status\x18\x03 \x01(\x0e\x32\x1e.pb.CallTimeEnterConfirmStatus\"\xb1\x01\n\x0b\x42ookSeatREQ\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\x12\x11\n\tis_booked\x18\x02 \x01(\x08\x12\r\n\x05\x63hips\x18\x03 \x01(\x03\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x1b\n\x07gps_lon\x18\x05 \x01(\x05:\n-360000000\x12\x1b\n\x07gps_lat\x18\x06 \x01(\x05:\n-360000000\x12\x14\n\x05is_pc\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x14\n\tbook_type\x18\x08 \x01(\x05:\x01\x30\"=\n\x0b\x42ookSeatRSP\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\x12\x1e\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x10.pb.BookSeatCode\"\xae\x01\n\x0b\x42ookSeatBRC\x12\x0e\n\x06seatid\x18\x01 \x01(\x05\x12\x1c\n\x05\x62rief\x18\x02 \x01(\x0b\x32\r.pb.UserBrief\x12\x11\n\tis_booked\x18\x03 \x01(\x08\x12!\n\x19\x63onfirm_remaining_seconds\x18\x04 \x01(\x05\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\x14\n\tvip_level\x18\x06 \x01(\r:\x01\x30\x12\x14\n\tbook_type\x18\x07 \x01(\x05:\x01\x30*U\n\x0c\x43\x61llTimeCode\x12\x1b\n\x17NOT_ENTER_CALLTIME_ROOM\x10\x00\x12\x13\n\x0f\x44URING_CALLTIME\x10\x01\x12\x13\n\x0f\x46INISH_CALLTIME\x10\x02*J\n\x13\x43\x61llTimeConfirmCode\x12\x1b\n\x17WAIT_CONFIRM_ENTER_ROOM\x10\x00\x12\x16\n\x12\x43ONFIRM_ENTER_ROOM\x10\x01*E\n\x1a\x43\x61llTimeEnterConfirmStatus\x12\x0e\n\nNO_OPERATE\x10\x00\x12\x0b\n\x07\x43ONFIRM\x10\x01\x12\n\n\x06\x43\x41NCEL\x10\x02*?\n\x0c\x42ookSeatType\x12\x15\n\x11\x42OOK_TYPE_DEFAULT\x10\x00\x12\x18\n\x14\x42OOK_TYPE_SQUID_GAME\x10\x01*\xb2\x03\n\x0c\x42ookSeatCode\x12\x0b\n\x07\x42OOK_OK\x10\x00\x12\x12\n\x0e\x42OOK_CANCEL_OK\x10\x01\x12\x1f\n\x12\x42OOK_ERR_WAIT_AUTH\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0f\x42OOK_ERR_SEATID\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x17\x42OOK_ERR_ALREADY_BOOKED\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12!\n\x14\x42OOK_ERR_ALREADY_SIT\x10\xfc\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x13\x42OOK_ERR_BEEN_SITED\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12!\n\x14\x42OOK_ERR_BEEN_BOOKED\x10\xfa\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\rBOOK_ERR_CLUB\x10\xf9\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x19\n\x0c\x42OOK_ERR_GPS\x10\xf8\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x18\n\x0b\x42OOK_ERR_IP\x10\xf7\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12!\n\x14\x42OOK_ERR_GPS_INVALID\x10\xf6\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12\x42OOK_ERR_ROOM_OVER\x10\xf5\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12\x42OOK_ERR_ROOM_FULL\x10\xf4\xff\xff\xff\xff\xff\xff\xff\xff\x01\x42\x06Z\x04./pb')
  ,
  dependencies=[pre__base__pb2.DESCRIPTOR,pre__base1__pb2.DESCRIPTOR,base__pb2.DESCRIPTOR,])

_CALLTIMECODE = _descriptor.EnumDescriptor(
  name='CallTimeCode',
  full_name='pb.CallTimeCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_ENTER_CALLTIME_ROOM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DURING_CALLTIME', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISH_CALLTIME', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1075,
  serialized_end=1160,
)
_sym_db.RegisterEnumDescriptor(_CALLTIMECODE)

CallTimeCode = enum_type_wrapper.EnumTypeWrapper(_CALLTIMECODE)
_CALLTIMECONFIRMCODE = _descriptor.EnumDescriptor(
  name='CallTimeConfirmCode',
  full_name='pb.CallTimeConfirmCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAIT_CONFIRM_ENTER_ROOM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ENTER_ROOM', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1162,
  serialized_end=1236,
)
_sym_db.RegisterEnumDescriptor(_CALLTIMECONFIRMCODE)

CallTimeConfirmCode = enum_type_wrapper.EnumTypeWrapper(_CALLTIMECONFIRMCODE)
_CALLTIMEENTERCONFIRMSTATUS = _descriptor.EnumDescriptor(
  name='CallTimeEnterConfirmStatus',
  full_name='pb.CallTimeEnterConfirmStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_OPERATE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1238,
  serialized_end=1307,
)
_sym_db.RegisterEnumDescriptor(_CALLTIMEENTERCONFIRMSTATUS)

CallTimeEnterConfirmStatus = enum_type_wrapper.EnumTypeWrapper(_CALLTIMEENTERCONFIRMSTATUS)
_BOOKSEATTYPE = _descriptor.EnumDescriptor(
  name='BookSeatType',
  full_name='pb.BookSeatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOK_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_TYPE_SQUID_GAME', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1309,
  serialized_end=1372,
)
_sym_db.RegisterEnumDescriptor(_BOOKSEATTYPE)

BookSeatType = enum_type_wrapper.EnumTypeWrapper(_BOOKSEATTYPE)
_BOOKSEATCODE = _descriptor.EnumDescriptor(
  name='BookSeatCode',
  full_name='pb.BookSeatCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOK_OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_CANCEL_OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_WAIT_AUTH', index=2, number=-1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_SEATID', index=3, number=-2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_ALREADY_BOOKED', index=4, number=-3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_ALREADY_SIT', index=5, number=-4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_BEEN_SITED', index=6, number=-5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_BEEN_BOOKED', index=7, number=-6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_CLUB', index=8, number=-7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_GPS', index=9, number=-8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_IP', index=10, number=-9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_GPS_INVALID', index=11, number=-10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_ROOM_OVER', index=12, number=-11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOK_ERR_ROOM_FULL', index=13, number=-12,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1375,
  serialized_end=1809,
)
_sym_db.RegisterEnumDescriptor(_BOOKSEATCODE)

BookSeatCode = enum_type_wrapper.EnumTypeWrapper(_BOOKSEATCODE)
NOT_ENTER_CALLTIME_ROOM = 0
DURING_CALLTIME = 1
FINISH_CALLTIME = 2
WAIT_CONFIRM_ENTER_ROOM = 0
CONFIRM_ENTER_ROOM = 1
NO_OPERATE = 0
CONFIRM = 1
CANCEL = 2
BOOK_TYPE_DEFAULT = 0
BOOK_TYPE_SQUID_GAME = 1
BOOK_OK = 0
BOOK_CANCEL_OK = 1
BOOK_ERR_WAIT_AUTH = -1
BOOK_ERR_SEATID = -2
BOOK_ERR_ALREADY_BOOKED = -3
BOOK_ERR_ALREADY_SIT = -4
BOOK_ERR_BEEN_SITED = -5
BOOK_ERR_BEEN_BOOKED = -6
BOOK_ERR_CLUB = -7
BOOK_ERR_GPS = -8
BOOK_ERR_IP = -9
BOOK_ERR_GPS_INVALID = -10
BOOK_ERR_ROOM_OVER = -11
BOOK_ERR_ROOM_FULL = -12



_CALLTIMEREQ = _descriptor.Descriptor(
  name='CallTimeREQ',
  full_name='pb.CallTimeREQ',
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
  serialized_start=67,
  serialized_end=80,
)


_CALLTIMEINFO = _descriptor.Descriptor(
  name='CallTimeInfo',
  full_name='pb.CallTimeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='pb.CallTimeInfo.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm_remaining_seconds', full_name='pb.CallTimeInfo.confirm_remaining_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remaining_seconds', full_name='pb.CallTimeInfo.remaining_seconds', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calltime_code', full_name='pb.CallTimeInfo.calltime_code', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm_code', full_name='pb.CallTimeInfo.confirm_code', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=83,
  serialized_end=264,
)


_CALLTIMEBRC = _descriptor.Descriptor(
  name='CallTimeBRC',
  full_name='pb.CallTimeBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='calltime_info', full_name='pb.CallTimeBRC.calltime_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=266,
  serialized_end=320,
)


_CALLTIMEENTERCONFIRMREQ = _descriptor.Descriptor(
  name='CallTimeEnterConfirmREQ',
  full_name='pb.CallTimeEnterConfirmREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='confirm_status', full_name='pb.CallTimeEnterConfirmREQ.confirm_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.CallTimeEnterConfirmREQ.seatid', index=1,
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
  serialized_start=322,
  serialized_end=419,
)


_CALLTIMEENTERCONFIRMRSP = _descriptor.Descriptor(
  name='CallTimeEnterConfirmRSP',
  full_name='pb.CallTimeEnterConfirmRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.CallTimeEnterConfirmRSP.seatid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.CallTimeEnterConfirmRSP.code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calltime_info', full_name='pb.CallTimeEnterConfirmRSP.calltime_info', index=2,
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
  serialized_start=421,
  serialized_end=535,
)


_CALLTIMEENTERROOMCONFIRMBRC = _descriptor.Descriptor(
  name='CallTimeEnterRoomConfirmBRC',
  full_name='pb.CallTimeEnterRoomConfirmBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.CallTimeEnterRoomConfirmBRC.seatid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chips', full_name='pb.CallTimeEnterRoomConfirmBRC.chips', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm_status', full_name='pb.CallTimeEnterRoomConfirmBRC.confirm_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=537,
  serialized_end=653,
)


_BOOKSEATREQ = _descriptor.Descriptor(
  name='BookSeatREQ',
  full_name='pb.BookSeatREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.BookSeatREQ.seatid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_booked', full_name='pb.BookSeatREQ.is_booked', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chips', full_name='pb.BookSeatREQ.chips', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='pb.BookSeatREQ.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gps_lon', full_name='pb.BookSeatREQ.gps_lon', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-360000000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gps_lat', full_name='pb.BookSeatREQ.gps_lat', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-360000000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_pc', full_name='pb.BookSeatREQ.is_pc', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_type', full_name='pb.BookSeatREQ.book_type', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=656,
  serialized_end=833,
)


_BOOKSEATRSP = _descriptor.Descriptor(
  name='BookSeatRSP',
  full_name='pb.BookSeatRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.BookSeatRSP.seatid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.BookSeatRSP.code', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=835,
  serialized_end=896,
)


_BOOKSEATBRC = _descriptor.Descriptor(
  name='BookSeatBRC',
  full_name='pb.BookSeatBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seatid', full_name='pb.BookSeatBRC.seatid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brief', full_name='pb.BookSeatBRC.brief', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_booked', full_name='pb.BookSeatBRC.is_booked', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm_remaining_seconds', full_name='pb.BookSeatBRC.confirm_remaining_seconds', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='pb.BookSeatBRC.country', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='pb.BookSeatBRC.vip_level', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_type', full_name='pb.BookSeatBRC.book_type', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=899,
  serialized_end=1073,
)

_CALLTIMEINFO.fields_by_name['calltime_code'].enum_type = _CALLTIMECODE
_CALLTIMEINFO.fields_by_name['confirm_code'].enum_type = _CALLTIMECONFIRMCODE
_CALLTIMEBRC.fields_by_name['calltime_info'].message_type = _CALLTIMEINFO
_CALLTIMEENTERCONFIRMREQ.fields_by_name['confirm_status'].enum_type = _CALLTIMEENTERCONFIRMSTATUS
_CALLTIMEENTERCONFIRMRSP.fields_by_name['code'].enum_type = _BOOKSEATCODE
_CALLTIMEENTERCONFIRMRSP.fields_by_name['calltime_info'].message_type = _CALLTIMEINFO
_CALLTIMEENTERROOMCONFIRMBRC.fields_by_name['confirm_status'].enum_type = _CALLTIMEENTERCONFIRMSTATUS
_BOOKSEATRSP.fields_by_name['code'].enum_type = _BOOKSEATCODE
_BOOKSEATBRC.fields_by_name['brief'].message_type = pre__base__pb2._USERBRIEF
DESCRIPTOR.message_types_by_name['CallTimeREQ'] = _CALLTIMEREQ
DESCRIPTOR.message_types_by_name['CallTimeInfo'] = _CALLTIMEINFO
DESCRIPTOR.message_types_by_name['CallTimeBRC'] = _CALLTIMEBRC
DESCRIPTOR.message_types_by_name['CallTimeEnterConfirmREQ'] = _CALLTIMEENTERCONFIRMREQ
DESCRIPTOR.message_types_by_name['CallTimeEnterConfirmRSP'] = _CALLTIMEENTERCONFIRMRSP
DESCRIPTOR.message_types_by_name['CallTimeEnterRoomConfirmBRC'] = _CALLTIMEENTERROOMCONFIRMBRC
DESCRIPTOR.message_types_by_name['BookSeatREQ'] = _BOOKSEATREQ
DESCRIPTOR.message_types_by_name['BookSeatRSP'] = _BOOKSEATRSP
DESCRIPTOR.message_types_by_name['BookSeatBRC'] = _BOOKSEATBRC
DESCRIPTOR.enum_types_by_name['CallTimeCode'] = _CALLTIMECODE
DESCRIPTOR.enum_types_by_name['CallTimeConfirmCode'] = _CALLTIMECONFIRMCODE
DESCRIPTOR.enum_types_by_name['CallTimeEnterConfirmStatus'] = _CALLTIMEENTERCONFIRMSTATUS
DESCRIPTOR.enum_types_by_name['BookSeatType'] = _BOOKSEATTYPE
DESCRIPTOR.enum_types_by_name['BookSeatCode'] = _BOOKSEATCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CallTimeREQ = _reflection.GeneratedProtocolMessageType('CallTimeREQ', (_message.Message,), dict(
  DESCRIPTOR = _CALLTIMEREQ,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.CallTimeREQ)
  ))
_sym_db.RegisterMessage(CallTimeREQ)

CallTimeInfo = _reflection.GeneratedProtocolMessageType('CallTimeInfo', (_message.Message,), dict(
  DESCRIPTOR = _CALLTIMEINFO,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.CallTimeInfo)
  ))
_sym_db.RegisterMessage(CallTimeInfo)

CallTimeBRC = _reflection.GeneratedProtocolMessageType('CallTimeBRC', (_message.Message,), dict(
  DESCRIPTOR = _CALLTIMEBRC,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.CallTimeBRC)
  ))
_sym_db.RegisterMessage(CallTimeBRC)

CallTimeEnterConfirmREQ = _reflection.GeneratedProtocolMessageType('CallTimeEnterConfirmREQ', (_message.Message,), dict(
  DESCRIPTOR = _CALLTIMEENTERCONFIRMREQ,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.CallTimeEnterConfirmREQ)
  ))
_sym_db.RegisterMessage(CallTimeEnterConfirmREQ)

CallTimeEnterConfirmRSP = _reflection.GeneratedProtocolMessageType('CallTimeEnterConfirmRSP', (_message.Message,), dict(
  DESCRIPTOR = _CALLTIMEENTERCONFIRMRSP,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.CallTimeEnterConfirmRSP)
  ))
_sym_db.RegisterMessage(CallTimeEnterConfirmRSP)

CallTimeEnterRoomConfirmBRC = _reflection.GeneratedProtocolMessageType('CallTimeEnterRoomConfirmBRC', (_message.Message,), dict(
  DESCRIPTOR = _CALLTIMEENTERROOMCONFIRMBRC,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.CallTimeEnterRoomConfirmBRC)
  ))
_sym_db.RegisterMessage(CallTimeEnterRoomConfirmBRC)

BookSeatREQ = _reflection.GeneratedProtocolMessageType('BookSeatREQ', (_message.Message,), dict(
  DESCRIPTOR = _BOOKSEATREQ,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.BookSeatREQ)
  ))
_sym_db.RegisterMessage(BookSeatREQ)

BookSeatRSP = _reflection.GeneratedProtocolMessageType('BookSeatRSP', (_message.Message,), dict(
  DESCRIPTOR = _BOOKSEATRSP,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.BookSeatRSP)
  ))
_sym_db.RegisterMessage(BookSeatRSP)

BookSeatBRC = _reflection.GeneratedProtocolMessageType('BookSeatBRC', (_message.Message,), dict(
  DESCRIPTOR = _BOOKSEATBRC,
  __module__ = 'calltime_pb2'
  # @@protoc_insertion_point(class_scope:pb.BookSeatBRC)
  ))
_sym_db.RegisterMessage(BookSeatBRC)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
