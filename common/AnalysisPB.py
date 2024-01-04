import os
from enum import Enum
import re
import importlib
import sys

from google.protobuf.descriptor_pool import DescriptorPool

from common import GenerateProto
from common.log import logger

script_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_directory, '..'))
proto_root = os.path.join(project_root, 'proto')


class DataType(Enum):
    TYPE_DOUBLE = 1
    TYPE_FLOAT = 2
    TYPE_INT64 = 3
    TYPE_UINT64 = 4
    TYPE_INT32 = 5
    TYPE_FIXED64 = 6
    TYPE_FIXED32 = 7
    TYPE_BOOL = 8
    TYPE_STRING = 9
    TYPE_GROUP = 10
    TYPE_MESSAGE = 11
    TYPE_BYTES = 12
    TYPE_UINT32 = 13
    TYPE_ENUM = 14
    TYPE_SFIXED32 = 15
    TYPE_SFIXED64 = 16
    TYPE_SINT32 = 17
    TYPE_SINT64 = 18
    MAX_TYPE = 19


class ProtoHandler(object):
    def __init__(self, proto_name):
        self.proto_name = proto_name

    def get_message_attributes(self, proto_name=None):
        if proto_name is None:
            proto_name = self.proto_name
        # 导入已生成的_pb2.py模块
        importlib.import_module(f"proto.{proto_name}")
        # 获取 FileDescriptor
        file_descriptor = getattr(sys.modules[f"proto.{proto_name}"], "DESCRIPTOR")
        # 获取消息和属性信息
        message_attributes = self._get_message_attributes(file_descriptor)
        logger.info(f"message_attributes: {message_attributes}")
        return message_attributes

    def get_all_message(self, proto_name=None, branch_name=None):
        if proto_name is None:
            proto_name = self.proto_name
        path = os.path.dirname(os.path.dirname(__file__)) + "/proto/" + branch_name
        logger.info(f"path: {path}")
        sys.path.append(path)
        module_name = f"proto.{branch_name}.{proto_name}_pb2"
        importlib.import_module(module_name)
        logger.info(f"module_name: {module_name}")
        # 获取 FileDescriptor
        file_descriptor = getattr(sys.modules[module_name], "DESCRIPTOR")
        logger.info(file_descriptor)
        # 获取消息和属性信息
        messages = self._get_message(file_descriptor)
        logger.info(f"messages: {file_descriptor.pool}")
        if module_name in sys.modules:
            del sys.modules[module_name]

        return messages

    def get_attributes_by_message(self, proto_name=None, message=None):
        if proto_name is None:
            proto_name = self.proto_name
        # 导入已生成的_pb2.py模块
        importlib.import_module(f"proto.{proto_name}")
        # 获取 FileDescriptor
        file_descriptor = getattr(sys.modules[f"proto.{proto_name}"], "DESCRIPTOR")
        # 获取消息和属性信息
        message_attributes = self._get_message_attributes(file_descriptor)
        attributes = message_attributes.get(message)
        ret = {'message': message, 'attributes': attributes}
        logger.info(f"ret: {ret}")
        return ret

    def _get_message(self, file_descriptor):
        messages = []
        for message_name, message_type in file_descriptor.message_types_by_name.items():
            messages.append(message_name)
        return messages

    def _get_message_attributes(self, file_descriptor):
        message_attributes = {}

        for message_name, message_type in file_descriptor.message_types_by_name.items():
            fields = []

            for field_descriptor in message_type.fields:
                field_name = field_descriptor.name
                field_number = field_descriptor.number
                field_data_type = field_descriptor.type

                if field_data_type == 14:
                    list = []
                    enum_descriptor = field_descriptor.enum_type
                    for enum_value in enum_descriptor.values_by_name.values():
                        list.append({enum_value.name: enum_value.number})
                    fields.append((field_name, DataType(field_data_type).name, field_number, list))
                elif field_data_type == 11:
                    list = []
                    for field in field_descriptor.message_type.fields:
                        list.append({field.name: DataType(field.type).name})
                    fields.append((field_name, DataType(field_data_type).name, field_number, list))
                else:
                    fields.append((field_name, field_number, DataType(field_data_type).name))

            message_attributes[message_name] = fields

        return message_attributes


class ProtoDir(object):
    def get_all_protoname(self, dir=None):
        logger.info(f"dir: {dir}")
        if dir is None:
            dir = proto_root
        proto_names = []
        if os.path.exists(dir):
            for file in os.listdir(dir):
                if re.match(r".*_pb2.py", file):
                    proto_name = file.split(".")[0]
                    proto_names.append(proto_name)
        # sys.path.append(dir)

        else:
            GenerateProto.download_and_compile_protos(os.path.basename(dir))
            for file in os.listdir(dir):
                if re.match(r".*_pb2.py", file):
                    proto_name = file.split(".")[0]
                    proto_names.append(proto_name)
        return proto_names

    def get_branch_protoname(self, branches=None):
        if branches is None:
            branches = 'master'
        dir = os.path.join(proto_root, branches)
        return self.get_all_protoname(dir=dir)
