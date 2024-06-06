import google.protobuf.descriptor_pb2 as descriptor


def get_messages_and_enums(proto_file_path):
    with open(proto_file_path, 'rb') as f:
        file_descriptor_set = descriptor.FileDescriptorSet.FromString(f.read())

    messages = []
    enums = []
    for file_descriptor_proto in file_descriptor_set.file:
        for message_type in file_descriptor_proto.message_type:
            messages.append(message_type.name)
        for enum_type in file_descriptor_proto.enum_type:
            enums.append(enum_type.name)

    return messages, enums


if __name__ == '__main__':
    proto_file_path = 'D:\work\protoScripts\proto\pb\achievement.proto'
    messages, enums = get_messages_and_enums(proto_file_path)
    print(messages)
    print(enums)
