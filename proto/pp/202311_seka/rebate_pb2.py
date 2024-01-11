# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rebate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rebate.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\004./pb'),
  serialized_pb=_b('\n\x0crebate.proto\x12\x02pb\"\x0b\n\tRebateREQ\"\x1b\n\tRebateRSP\x12\x0e\n\x06rebate\x18\x01 \x01(\x03\"\x0f\n\rRebateShopREQ\"\xa4\x01\n\x0eRebateShopItem\x12\x0e\n\x06tempid\x18\x01 \x01(\t\x12\x11\n\titem_type\x18\x02 \x01(\x05\x12\x11\n\titem_name\x18\x03 \x01(\t\x12\x10\n\x08item_qty\x18\x04 \x01(\x05\x12\x12\n\nitem_price\x18\x05 \x01(\x03\x12\x11\n\titem_sort\x18\x06 \x01(\x05\x12\x11\n\tlimit_num\x18\x07 \x01(\x05\x12\x10\n\x08left_num\x18\x08 \x01(\x05\"G\n\rRebateShopRSP\x12 \n\x04item\x18\x01 \x03(\x0b\x32\x12.pb.RebateShopItem\x12\x14\n\x0crefresh_time\x18\x02 \x01(\x03\"&\n\x14\x42uyRebateShopItemREQ\x12\x0e\n\x06tempid\x18\x01 \x01(\t\"4\n\x14\x42uyRebateShopItemRSP\x12\x0e\n\x06tempid\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"\x19\n\x17\x45xchangeRebateRecordREQ\"l\n\x14\x45xchangeRebateRecord\x12\x0e\n\x06rebate\x18\x01 \x01(\x03\x12\x11\n\titem_type\x18\x02 \x01(\x05\x12\x11\n\titem_name\x18\x03 \x01(\t\x12\x10\n\x08item_qty\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x03\"C\n\x17\x45xchangeRebateRecordRSP\x12(\n\x06record\x18\x01 \x03(\x0b\x32\x18.pb.ExchangeRebateRecord\"\x15\n\x13\x46lowRebateRecordREQ\"\x90\x01\n\x13\x46lowRebateRecordRSP\x12\x14\n\x0clobby_rebate\x18\x01 \x01(\x03\x12\x17\n\x0fofficial_rebate\x18\x02 \x01(\x03\x12\x13\n\x0b\x63lub_rebate\x18\x03 \x01(\x03\x12\x1f\n\x17lottery_prize_gl_rebate\x18\x04 \x01(\x03\x12\x14\n\x0clevel_rebate\x18\x05 \x01(\x03\"\x1d\n\x1b\x46lowRebateLastWeekRecordREQ\"a\n\x1b\x46lowRebateLastWeekRecordRSP\x12\x14\n\x0clobby_rebate\x18\x01 \x01(\x03\x12\x17\n\x0fofficial_rebate\x18\x02 \x01(\x03\x12\x13\n\x0b\x63lub_rebate\x18\x03 \x01(\x03\"\x13\n\x11RoomRebateInfoREQ\"*\n\nRebateInfo\x12\x0e\n\x06rebate\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x03\"\xb9\x01\n\x11RoomRebateInfoRSP\x12\x14\n\thands_num\x18\x01 \x01(\x05:\x01\x30\x12\x11\n\x06rebate\x18\x02 \x01(\x05:\x01\x30\x12\x19\n\x0eneed_hands_num\x18\x03 \x01(\x05:\x01\x30\x12\x17\n\x0crebate_point\x18\x04 \x01(\x05:\x01\x30\x12\x1a\n\x0fget_rebate_type\x18\x05 \x01(\x05:\x01\x31\x12+\n\x13history_rebate_list\x18\x06 \x03(\x0b\x32\x0e.pb.RebateInfo\"\xb9\x01\n\x11RoomRebateInfoBRC\x12\x14\n\thands_num\x18\x01 \x01(\x05:\x01\x30\x12\x11\n\x06rebate\x18\x02 \x01(\x05:\x01\x30\x12\x19\n\x0eneed_hands_num\x18\x03 \x01(\x05:\x01\x30\x12\x17\n\x0crebate_point\x18\x04 \x01(\x05:\x01\x30\x12\x1a\n\x0fget_rebate_type\x18\x05 \x01(\x05:\x01\x31\x12+\n\x13history_rebate_list\x18\x06 \x03(\x0b\x32\x0e.pb.RebateInfo\"\x18\n\x16\x46\x65tchClubRakeRebateREQ\"9\n\x16\x46\x65tchClubRakeRebateRSP\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x11\n\x06rebate\x18\x02 \x01(\x05:\x01\x30\x42\x06Z\x04./pb')
)




_REBATEREQ = _descriptor.Descriptor(
  name='RebateREQ',
  full_name='pb.RebateREQ',
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
  serialized_start=20,
  serialized_end=31,
)


_REBATERSP = _descriptor.Descriptor(
  name='RebateRSP',
  full_name='pb.RebateRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.RebateRSP.rebate', index=0,
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
  serialized_start=33,
  serialized_end=60,
)


_REBATESHOPREQ = _descriptor.Descriptor(
  name='RebateShopREQ',
  full_name='pb.RebateShopREQ',
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
  serialized_start=62,
  serialized_end=77,
)


_REBATESHOPITEM = _descriptor.Descriptor(
  name='RebateShopItem',
  full_name='pb.RebateShopItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tempid', full_name='pb.RebateShopItem.tempid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_type', full_name='pb.RebateShopItem.item_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_name', full_name='pb.RebateShopItem.item_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_qty', full_name='pb.RebateShopItem.item_qty', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_price', full_name='pb.RebateShopItem.item_price', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_sort', full_name='pb.RebateShopItem.item_sort', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit_num', full_name='pb.RebateShopItem.limit_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_num', full_name='pb.RebateShopItem.left_num', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=80,
  serialized_end=244,
)


_REBATESHOPRSP = _descriptor.Descriptor(
  name='RebateShopRSP',
  full_name='pb.RebateShopRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pb.RebateShopRSP.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh_time', full_name='pb.RebateShopRSP.refresh_time', index=1,
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
  serialized_start=246,
  serialized_end=317,
)


_BUYREBATESHOPITEMREQ = _descriptor.Descriptor(
  name='BuyRebateShopItemREQ',
  full_name='pb.BuyRebateShopItemREQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tempid', full_name='pb.BuyRebateShopItemREQ.tempid', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=319,
  serialized_end=357,
)


_BUYREBATESHOPITEMRSP = _descriptor.Descriptor(
  name='BuyRebateShopItemRSP',
  full_name='pb.BuyRebateShopItemRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tempid', full_name='pb.BuyRebateShopItemRSP.tempid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.BuyRebateShopItemRSP.code', index=1,
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
  serialized_start=359,
  serialized_end=411,
)


_EXCHANGEREBATERECORDREQ = _descriptor.Descriptor(
  name='ExchangeRebateRecordREQ',
  full_name='pb.ExchangeRebateRecordREQ',
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
  serialized_start=413,
  serialized_end=438,
)


_EXCHANGEREBATERECORD = _descriptor.Descriptor(
  name='ExchangeRebateRecord',
  full_name='pb.ExchangeRebateRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.ExchangeRebateRecord.rebate', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_type', full_name='pb.ExchangeRebateRecord.item_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_name', full_name='pb.ExchangeRebateRecord.item_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_qty', full_name='pb.ExchangeRebateRecord.item_qty', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='pb.ExchangeRebateRecord.time', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=440,
  serialized_end=548,
)


_EXCHANGEREBATERECORDRSP = _descriptor.Descriptor(
  name='ExchangeRebateRecordRSP',
  full_name='pb.ExchangeRebateRecordRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='pb.ExchangeRebateRecordRSP.record', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=550,
  serialized_end=617,
)


_FLOWREBATERECORDREQ = _descriptor.Descriptor(
  name='FlowRebateRecordREQ',
  full_name='pb.FlowRebateRecordREQ',
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
  serialized_start=619,
  serialized_end=640,
)


_FLOWREBATERECORDRSP = _descriptor.Descriptor(
  name='FlowRebateRecordRSP',
  full_name='pb.FlowRebateRecordRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lobby_rebate', full_name='pb.FlowRebateRecordRSP.lobby_rebate', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='official_rebate', full_name='pb.FlowRebateRecordRSP.official_rebate', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='club_rebate', full_name='pb.FlowRebateRecordRSP.club_rebate', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lottery_prize_gl_rebate', full_name='pb.FlowRebateRecordRSP.lottery_prize_gl_rebate', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level_rebate', full_name='pb.FlowRebateRecordRSP.level_rebate', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=643,
  serialized_end=787,
)


_FLOWREBATELASTWEEKRECORDREQ = _descriptor.Descriptor(
  name='FlowRebateLastWeekRecordREQ',
  full_name='pb.FlowRebateLastWeekRecordREQ',
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
  serialized_start=789,
  serialized_end=818,
)


_FLOWREBATELASTWEEKRECORDRSP = _descriptor.Descriptor(
  name='FlowRebateLastWeekRecordRSP',
  full_name='pb.FlowRebateLastWeekRecordRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lobby_rebate', full_name='pb.FlowRebateLastWeekRecordRSP.lobby_rebate', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='official_rebate', full_name='pb.FlowRebateLastWeekRecordRSP.official_rebate', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='club_rebate', full_name='pb.FlowRebateLastWeekRecordRSP.club_rebate', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=820,
  serialized_end=917,
)


_ROOMREBATEINFOREQ = _descriptor.Descriptor(
  name='RoomRebateInfoREQ',
  full_name='pb.RoomRebateInfoREQ',
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
  serialized_start=919,
  serialized_end=938,
)


_REBATEINFO = _descriptor.Descriptor(
  name='RebateInfo',
  full_name='pb.RebateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.RebateInfo.rebate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='pb.RebateInfo.time', index=1,
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
  serialized_start=940,
  serialized_end=982,
)


_ROOMREBATEINFORSP = _descriptor.Descriptor(
  name='RoomRebateInfoRSP',
  full_name='pb.RoomRebateInfoRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hands_num', full_name='pb.RoomRebateInfoRSP.hands_num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.RoomRebateInfoRSP.rebate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_hands_num', full_name='pb.RoomRebateInfoRSP.need_hands_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate_point', full_name='pb.RoomRebateInfoRSP.rebate_point', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_rebate_type', full_name='pb.RoomRebateInfoRSP.get_rebate_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='history_rebate_list', full_name='pb.RoomRebateInfoRSP.history_rebate_list', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=985,
  serialized_end=1170,
)


_ROOMREBATEINFOBRC = _descriptor.Descriptor(
  name='RoomRebateInfoBRC',
  full_name='pb.RoomRebateInfoBRC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hands_num', full_name='pb.RoomRebateInfoBRC.hands_num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.RoomRebateInfoBRC.rebate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_hands_num', full_name='pb.RoomRebateInfoBRC.need_hands_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate_point', full_name='pb.RoomRebateInfoBRC.rebate_point', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_rebate_type', full_name='pb.RoomRebateInfoBRC.get_rebate_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='history_rebate_list', full_name='pb.RoomRebateInfoBRC.history_rebate_list', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1173,
  serialized_end=1358,
)


_FETCHCLUBRAKEREBATEREQ = _descriptor.Descriptor(
  name='FetchClubRakeRebateREQ',
  full_name='pb.FetchClubRakeRebateREQ',
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
  serialized_start=1360,
  serialized_end=1384,
)


_FETCHCLUBRAKEREBATERSP = _descriptor.Descriptor(
  name='FetchClubRakeRebateRSP',
  full_name='pb.FetchClubRakeRebateRSP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.FetchClubRakeRebateRSP.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rebate', full_name='pb.FetchClubRakeRebateRSP.rebate', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1386,
  serialized_end=1443,
)

_REBATESHOPRSP.fields_by_name['item'].message_type = _REBATESHOPITEM
_EXCHANGEREBATERECORDRSP.fields_by_name['record'].message_type = _EXCHANGEREBATERECORD
_ROOMREBATEINFORSP.fields_by_name['history_rebate_list'].message_type = _REBATEINFO
_ROOMREBATEINFOBRC.fields_by_name['history_rebate_list'].message_type = _REBATEINFO
DESCRIPTOR.message_types_by_name['RebateREQ'] = _REBATEREQ
DESCRIPTOR.message_types_by_name['RebateRSP'] = _REBATERSP
DESCRIPTOR.message_types_by_name['RebateShopREQ'] = _REBATESHOPREQ
DESCRIPTOR.message_types_by_name['RebateShopItem'] = _REBATESHOPITEM
DESCRIPTOR.message_types_by_name['RebateShopRSP'] = _REBATESHOPRSP
DESCRIPTOR.message_types_by_name['BuyRebateShopItemREQ'] = _BUYREBATESHOPITEMREQ
DESCRIPTOR.message_types_by_name['BuyRebateShopItemRSP'] = _BUYREBATESHOPITEMRSP
DESCRIPTOR.message_types_by_name['ExchangeRebateRecordREQ'] = _EXCHANGEREBATERECORDREQ
DESCRIPTOR.message_types_by_name['ExchangeRebateRecord'] = _EXCHANGEREBATERECORD
DESCRIPTOR.message_types_by_name['ExchangeRebateRecordRSP'] = _EXCHANGEREBATERECORDRSP
DESCRIPTOR.message_types_by_name['FlowRebateRecordREQ'] = _FLOWREBATERECORDREQ
DESCRIPTOR.message_types_by_name['FlowRebateRecordRSP'] = _FLOWREBATERECORDRSP
DESCRIPTOR.message_types_by_name['FlowRebateLastWeekRecordREQ'] = _FLOWREBATELASTWEEKRECORDREQ
DESCRIPTOR.message_types_by_name['FlowRebateLastWeekRecordRSP'] = _FLOWREBATELASTWEEKRECORDRSP
DESCRIPTOR.message_types_by_name['RoomRebateInfoREQ'] = _ROOMREBATEINFOREQ
DESCRIPTOR.message_types_by_name['RebateInfo'] = _REBATEINFO
DESCRIPTOR.message_types_by_name['RoomRebateInfoRSP'] = _ROOMREBATEINFORSP
DESCRIPTOR.message_types_by_name['RoomRebateInfoBRC'] = _ROOMREBATEINFOBRC
DESCRIPTOR.message_types_by_name['FetchClubRakeRebateREQ'] = _FETCHCLUBRAKEREBATEREQ
DESCRIPTOR.message_types_by_name['FetchClubRakeRebateRSP'] = _FETCHCLUBRAKEREBATERSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RebateREQ = _reflection.GeneratedProtocolMessageType('RebateREQ', (_message.Message,), dict(
  DESCRIPTOR = _REBATEREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RebateREQ)
  ))
_sym_db.RegisterMessage(RebateREQ)

RebateRSP = _reflection.GeneratedProtocolMessageType('RebateRSP', (_message.Message,), dict(
  DESCRIPTOR = _REBATERSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RebateRSP)
  ))
_sym_db.RegisterMessage(RebateRSP)

RebateShopREQ = _reflection.GeneratedProtocolMessageType('RebateShopREQ', (_message.Message,), dict(
  DESCRIPTOR = _REBATESHOPREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RebateShopREQ)
  ))
_sym_db.RegisterMessage(RebateShopREQ)

RebateShopItem = _reflection.GeneratedProtocolMessageType('RebateShopItem', (_message.Message,), dict(
  DESCRIPTOR = _REBATESHOPITEM,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RebateShopItem)
  ))
_sym_db.RegisterMessage(RebateShopItem)

RebateShopRSP = _reflection.GeneratedProtocolMessageType('RebateShopRSP', (_message.Message,), dict(
  DESCRIPTOR = _REBATESHOPRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RebateShopRSP)
  ))
_sym_db.RegisterMessage(RebateShopRSP)

BuyRebateShopItemREQ = _reflection.GeneratedProtocolMessageType('BuyRebateShopItemREQ', (_message.Message,), dict(
  DESCRIPTOR = _BUYREBATESHOPITEMREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.BuyRebateShopItemREQ)
  ))
_sym_db.RegisterMessage(BuyRebateShopItemREQ)

BuyRebateShopItemRSP = _reflection.GeneratedProtocolMessageType('BuyRebateShopItemRSP', (_message.Message,), dict(
  DESCRIPTOR = _BUYREBATESHOPITEMRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.BuyRebateShopItemRSP)
  ))
_sym_db.RegisterMessage(BuyRebateShopItemRSP)

ExchangeRebateRecordREQ = _reflection.GeneratedProtocolMessageType('ExchangeRebateRecordREQ', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEREBATERECORDREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.ExchangeRebateRecordREQ)
  ))
_sym_db.RegisterMessage(ExchangeRebateRecordREQ)

ExchangeRebateRecord = _reflection.GeneratedProtocolMessageType('ExchangeRebateRecord', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEREBATERECORD,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.ExchangeRebateRecord)
  ))
_sym_db.RegisterMessage(ExchangeRebateRecord)

ExchangeRebateRecordRSP = _reflection.GeneratedProtocolMessageType('ExchangeRebateRecordRSP', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEREBATERECORDRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.ExchangeRebateRecordRSP)
  ))
_sym_db.RegisterMessage(ExchangeRebateRecordRSP)

FlowRebateRecordREQ = _reflection.GeneratedProtocolMessageType('FlowRebateRecordREQ', (_message.Message,), dict(
  DESCRIPTOR = _FLOWREBATERECORDREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.FlowRebateRecordREQ)
  ))
_sym_db.RegisterMessage(FlowRebateRecordREQ)

FlowRebateRecordRSP = _reflection.GeneratedProtocolMessageType('FlowRebateRecordRSP', (_message.Message,), dict(
  DESCRIPTOR = _FLOWREBATERECORDRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.FlowRebateRecordRSP)
  ))
_sym_db.RegisterMessage(FlowRebateRecordRSP)

FlowRebateLastWeekRecordREQ = _reflection.GeneratedProtocolMessageType('FlowRebateLastWeekRecordREQ', (_message.Message,), dict(
  DESCRIPTOR = _FLOWREBATELASTWEEKRECORDREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.FlowRebateLastWeekRecordREQ)
  ))
_sym_db.RegisterMessage(FlowRebateLastWeekRecordREQ)

FlowRebateLastWeekRecordRSP = _reflection.GeneratedProtocolMessageType('FlowRebateLastWeekRecordRSP', (_message.Message,), dict(
  DESCRIPTOR = _FLOWREBATELASTWEEKRECORDRSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.FlowRebateLastWeekRecordRSP)
  ))
_sym_db.RegisterMessage(FlowRebateLastWeekRecordRSP)

RoomRebateInfoREQ = _reflection.GeneratedProtocolMessageType('RoomRebateInfoREQ', (_message.Message,), dict(
  DESCRIPTOR = _ROOMREBATEINFOREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RoomRebateInfoREQ)
  ))
_sym_db.RegisterMessage(RoomRebateInfoREQ)

RebateInfo = _reflection.GeneratedProtocolMessageType('RebateInfo', (_message.Message,), dict(
  DESCRIPTOR = _REBATEINFO,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RebateInfo)
  ))
_sym_db.RegisterMessage(RebateInfo)

RoomRebateInfoRSP = _reflection.GeneratedProtocolMessageType('RoomRebateInfoRSP', (_message.Message,), dict(
  DESCRIPTOR = _ROOMREBATEINFORSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RoomRebateInfoRSP)
  ))
_sym_db.RegisterMessage(RoomRebateInfoRSP)

RoomRebateInfoBRC = _reflection.GeneratedProtocolMessageType('RoomRebateInfoBRC', (_message.Message,), dict(
  DESCRIPTOR = _ROOMREBATEINFOBRC,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.RoomRebateInfoBRC)
  ))
_sym_db.RegisterMessage(RoomRebateInfoBRC)

FetchClubRakeRebateREQ = _reflection.GeneratedProtocolMessageType('FetchClubRakeRebateREQ', (_message.Message,), dict(
  DESCRIPTOR = _FETCHCLUBRAKEREBATEREQ,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.FetchClubRakeRebateREQ)
  ))
_sym_db.RegisterMessage(FetchClubRakeRebateREQ)

FetchClubRakeRebateRSP = _reflection.GeneratedProtocolMessageType('FetchClubRakeRebateRSP', (_message.Message,), dict(
  DESCRIPTOR = _FETCHCLUBRAKEREBATERSP,
  __module__ = 'rebate_pb2'
  # @@protoc_insertion_point(class_scope:pb.FetchClubRakeRebateRSP)
  ))
_sym_db.RegisterMessage(FetchClubRakeRebateRSP)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
