# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pppoker.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import mystery_bounty_pb2 as mystery__bounty__pb2
import pre_base_pb2 as pre__base__pb2
import base_pb2 as base__pb2
import base2_pb2 as base2__pb2
import activity_pb2 as activity__pb2
import deposit_activity_pb2 as deposit__activity__pb2
import activity3_pb2 as activity3__pb2
import calltime_pb2 as calltime__pb2
import pb2_pb2 as pb2__pb2
import pine1_pb2 as pine1__pb2
import pine_pb2 as pine__pb2
import sng_pb2 as sng__pb2
import pb1_pb2 as pb1__pb2
import pb3_pb2 as pb3__pb2
import pb4_pb2 as pb4__pb2
import free_chips_pb2 as free__chips__pb2
import shark_king_flip_pb2 as shark__king__flip__pb2
import pb5_pb2 as pb5__pb2
import pb6_pb2 as pb6__pb2
import pb7_pb2 as pb7__pb2
import trophy_base_pb2 as trophy__base__pb2
import trophy_pb2 as trophy__pb2
import cash_back_pb2 as cash__back__pb2
import shop_pb2 as shop__pb2
import vip_pb2 as vip__pb2
import league_pb2 as league__pb2
import club_base_pb2 as club__base__pb2
import club1_pb2 as club1__pb2
import club2_pb2 as club2__pb2
import club3_pb2 as club3__pb2
import club4_pb2 as club4__pb2
import mtt2_pb2 as mtt2__pb2
import mtt1_pb2 as mtt1__pb2
import mtt_pb2 as mtt__pb2
import career_pb2 as career__pb2
import user_relation_pb2 as user__relation__pb2
import user_setting_pb2 as user__setting__pb2
import risk_management_pb2 as risk__management__pb2
import jackpot_pb2 as jackpot__pb2
import value_pb2 as value__pb2
import achievement_base_pb2 as achievement__base__pb2
import achievement_pb2 as achievement__pb2
import shop_item_list_pb2 as shop__item__list__pb2
import kyc_pb2 as kyc__pb2
import mission_base_pb2 as mission__base__pb2
import mission_pb2 as mission__pb2
import ticket_pb2 as ticket__pb2
import leaderboard_activity_base_pb2 as leaderboard__activity__base__pb2
import leaderboard_activity_pb2 as leaderboard__activity__pb2
import item_pb2 as item__pb2
import rebate_base_pb2 as rebate__base__pb2
import rebate_pb2 as rebate__pb2
import lucky_draw_base_pb2 as lucky__draw__base__pb2
import lucky_draw_pb2 as lucky__draw__pb2
import push_center_pb2 as push__center__pb2
import hands_review_pb2 as hands__review__pb2
import gift_code_pb2 as gift__code__pb2
import cheers_activity_pb2 as cheers__activity__pb2
import go_user_pb2 as go__user__pb2
import translation_pb2 as translation__pb2
import aof_treasure_pb2 as aof__treasure__pb2
import invite_pb2 as invite__pb2
import new_comers_guide_pb2 as new__comers__guide__pb2
import christmas_2023_pb2 as christmas__2023__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pppoker.proto',
  package='pb',
  syntax='proto2',
  serialized_options=_b('Z\005../pb'),
  serialized_pb=_b('\n\rpppoker.proto\x12\x02pb\x1a\x0c\x63ommon.proto\x1a\x14mystery_bounty.proto\x1a\x0epre_base.proto\x1a\nbase.proto\x1a\x0b\x62\x61se2.proto\x1a\x0e\x61\x63tivity.proto\x1a\x16\x64\x65posit_activity.proto\x1a\x0f\x61\x63tivity3.proto\x1a\x0e\x63\x61lltime.proto\x1a\tpb2.proto\x1a\x0bpine1.proto\x1a\npine.proto\x1a\tsng.proto\x1a\tpb1.proto\x1a\tpb3.proto\x1a\tpb4.proto\x1a\x10\x66ree_chips.proto\x1a\x15shark_king_flip.proto\x1a\tpb5.proto\x1a\tpb6.proto\x1a\tpb7.proto\x1a\x11trophy_base.proto\x1a\x0ctrophy.proto\x1a\x0f\x63\x61sh_back.proto\x1a\nshop.proto\x1a\tvip.proto\x1a\x0cleague.proto\x1a\x0f\x63lub_base.proto\x1a\x0b\x63lub1.proto\x1a\x0b\x63lub2.proto\x1a\x0b\x63lub3.proto\x1a\x0b\x63lub4.proto\x1a\nmtt2.proto\x1a\nmtt1.proto\x1a\tmtt.proto\x1a\x0c\x63\x61reer.proto\x1a\x13user_relation.proto\x1a\x12user_setting.proto\x1a\x15risk_management.proto\x1a\rjackpot.proto\x1a\x0bvalue.proto\x1a\x16\x61\x63hievement_base.proto\x1a\x11\x61\x63hievement.proto\x1a\x14shop_item_list.proto\x1a\tkyc.proto\x1a\x12mission_base.proto\x1a\rmission.proto\x1a\x0cticket.proto\x1a\x1fleaderboard_activity_base.proto\x1a\x1aleaderboard_activity.proto\x1a\nitem.proto\x1a\x11rebate_base.proto\x1a\x0crebate.proto\x1a\x15lucky_draw_base.proto\x1a\x10lucky_draw.proto\x1a\x11push_center.proto\x1a\x12hands_review.proto\x1a\x0fgift_code.proto\x1a\x15\x63heers_activity.proto\x1a\rgo_user.proto\x1a\x11translation.proto\x1a\x12\x61of_treasure.proto\x1a\x0cinvite.proto\x1a\x16new_comers_guide.proto\x1a\x14\x63hristmas_2023.protoB\x07Z\x05../pb')
  ,
  dependencies=[common__pb2.DESCRIPTOR,mystery__bounty__pb2.DESCRIPTOR,pre__base__pb2.DESCRIPTOR,base__pb2.DESCRIPTOR,base2__pb2.DESCRIPTOR,activity__pb2.DESCRIPTOR,deposit__activity__pb2.DESCRIPTOR,activity3__pb2.DESCRIPTOR,calltime__pb2.DESCRIPTOR,pb2__pb2.DESCRIPTOR,pine1__pb2.DESCRIPTOR,pine__pb2.DESCRIPTOR,sng__pb2.DESCRIPTOR,pb1__pb2.DESCRIPTOR,pb3__pb2.DESCRIPTOR,pb4__pb2.DESCRIPTOR,free__chips__pb2.DESCRIPTOR,shark__king__flip__pb2.DESCRIPTOR,pb5__pb2.DESCRIPTOR,pb6__pb2.DESCRIPTOR,pb7__pb2.DESCRIPTOR,trophy__base__pb2.DESCRIPTOR,trophy__pb2.DESCRIPTOR,cash__back__pb2.DESCRIPTOR,shop__pb2.DESCRIPTOR,vip__pb2.DESCRIPTOR,league__pb2.DESCRIPTOR,club__base__pb2.DESCRIPTOR,club1__pb2.DESCRIPTOR,club2__pb2.DESCRIPTOR,club3__pb2.DESCRIPTOR,club4__pb2.DESCRIPTOR,mtt2__pb2.DESCRIPTOR,mtt1__pb2.DESCRIPTOR,mtt__pb2.DESCRIPTOR,career__pb2.DESCRIPTOR,user__relation__pb2.DESCRIPTOR,user__setting__pb2.DESCRIPTOR,risk__management__pb2.DESCRIPTOR,jackpot__pb2.DESCRIPTOR,value__pb2.DESCRIPTOR,achievement__base__pb2.DESCRIPTOR,achievement__pb2.DESCRIPTOR,shop__item__list__pb2.DESCRIPTOR,kyc__pb2.DESCRIPTOR,mission__base__pb2.DESCRIPTOR,mission__pb2.DESCRIPTOR,ticket__pb2.DESCRIPTOR,leaderboard__activity__base__pb2.DESCRIPTOR,leaderboard__activity__pb2.DESCRIPTOR,item__pb2.DESCRIPTOR,rebate__base__pb2.DESCRIPTOR,rebate__pb2.DESCRIPTOR,lucky__draw__base__pb2.DESCRIPTOR,lucky__draw__pb2.DESCRIPTOR,push__center__pb2.DESCRIPTOR,hands__review__pb2.DESCRIPTOR,gift__code__pb2.DESCRIPTOR,cheers__activity__pb2.DESCRIPTOR,go__user__pb2.DESCRIPTOR,translation__pb2.DESCRIPTOR,aof__treasure__pb2.DESCRIPTOR,invite__pb2.DESCRIPTOR,new__comers__guide__pb2.DESCRIPTOR,christmas__2023__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
