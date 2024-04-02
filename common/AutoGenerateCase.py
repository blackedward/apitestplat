from common.log import logger

from allpairspy import AllPairs


def is_2d_array(data):
    if not isinstance(data, list):
        return False

    for item in data:
        if not isinstance(item, list):
            return False

    return True


def process_attributes(attributes):
    if is_2d_array(attributes):
        attributes = attributes[0]
    parameters = []
    for attribute in attributes:
        if attribute["is_repeated"]:
            if attribute["type"] == "TYPE_MESSAGE":
                y = []
                x = []
                if is_2d_array(attribute["fields"]):
                    attribute["fields"] = attribute["fields"][0]
                for field in attribute["fields"]:
                    if field["type"] == "TYPE_MESSAGE":
                        x.extend(process_attributes([field]))
                    else:
                        x.append(field["range"])
                for a in AllPairs(x):
                    y.append(a)
                parameters.append(y)
            else:
                y = []
                for j in range(len(attribute["range"])):
                    temp = [attribute["range"][j]]
                    y.append(temp)
                parameters.append(y)
        else:
            if attribute["type"] == "TYPE_BOOL":
                w = [True, False]
                parameters.append(w)
            elif attribute["type"] == "TYPE_MESSAGE":
                y = []
                x = []
                for field in attribute["fields"]:
                    if field["type"] == "TYPE_MESSAGE":
                        z = []
                        z.extend(process_attributes(field["fields"]))
                        m = []
                        for a in AllPairs(z):
                            m.append(a)
                        x.append(m)
                    elif field["type"] != "TYPE_MESSAGE" and field["is_repeated"]:
                        s = []
                        for j in range(len(field["range"])):
                            l = [field["range"][j]]
                            s.append(l)
                        x.append(s)
                    else:
                        x.append(field["range"])
                for a in AllPairs(x):
                    y.append(a)
                parameters.append(y)
            else:
                parameters.append(attribute["range"])
    return parameters


def generate_test_cases(attributes):
    testcases_params = []
    parameters = process_attributes(attributes)
    logger.info(f"Parameters: {parameters}")
    test_cases = AllPairs(parameters)

    for i, test_case in enumerate(test_cases):
        json_object = {}
        for x in range(len(attributes)):
            if attributes[x]["is_repeated"]:
                if attributes[x]["type"] == "TYPE_MESSAGE":
                    field_values = []
                    field_values.append(process_message_field_assign(attributes[x], test_case[x]))
                    # for field in attributes[x]["fields"]:
                    #     if field["type"] == "TYPE_MESSAGE":
                    #         field_values.append(process_message_field_assign(field, test_case[x]))
                    #     else:
                    #         field_values.append(test_case[x])
                elif attributes[x]["type"] != "TYPE_MESSAGE" and attributes[x]["is_repeated"]:
                    field_values = []
                    for j in range(len(test_case[x])):
                        field_values.append(test_case[x][j])
                else:
                    for j in range(len(test_case[x])):
                        field_values.append(test_case[x][j])
                json_object[attributes[x]['name']] = field_values
            else:
                caseval = test_case[x]
                if attributes[x]["type"] == "TYPE_MESSAGE":
                    json_object[attributes[x]['name']] = process_message_field_assign(attributes[x], caseval)
                else:
                    json_object[attributes[x]['name']] = caseval
        testcases_params.append(json_object)
    return testcases_params


def process_message_field_assign(field, caseval):
    if field["type"] == "TYPE_MESSAGE" and field["is_repeated"]:
        tmp_array = []
        tmp_object = {}
        if is_2d_array(field["fields"]):
            field["fields"] = field["fields"][0]
        for subfield, subcaseval in zip(field["fields"], caseval):
            tmp_object[subfield["name"]] = process_message_field_assign(subfield, subcaseval)
        tmp_array.append(tmp_object)
        return tmp_array
    elif field["type"] == "TYPE_MESSAGE":
        tmp_object = {}
        for subfield, subcaseval in zip(field["fields"], caseval):
            tmp_object[subfield["name"]] = process_message_field_assign(subfield, subcaseval)
        return tmp_object
    elif field["type"] != "TYPE_MESSAGE" and field["is_repeated"]:
        return [caseval]
    else:
        return caseval

# def generate_test_cases(attributes):
#     testcases_params = []
#     parameters = []
#
#     n = len(attributes)
#
#     for i in range(n):
#         if attributes[i]["is_repeated"]:
#             if attributes[i]["type"] == "TYPE_MESSAGE":
#                 y = []
#                 x = []
#                 for j in range(len(attributes[i]["fields"])):
#                     x.append(attributes[i]["fields"][j]["range"])
#                 for a in AllPairs(x):
#                     y.append(a)
#                 parameters.append(y)
#             else:
#                 y = []
#                 for j in range(len(attributes[i]["range"])):
#                     temp = [attributes[i]["range"][j]]
#                     y.append(temp)
#                 sub_array = random.sample(attributes[i]["range"], random.randint(1, len(attributes[i]["range"])))
#
#                 y.append(sub_array)
#                 parameters.append(y)
#         else:
#             if attributes[i]["type"] == "TYPE_BOOL":
#                 w = [True, False]
#                 parameters.append(w)
#             else:
#                 parameters.append(attributes[i]["range"])
#     test_cases = AllPairs(parameters)
#
#     for i, test_case in enumerate(test_cases):
#
#         json_object = {}
#         for x in range(len(attributes)):
#             if attributes[x]["is_repeated"]:
#                 tmp_object = {}
#                 tmp_array = []
#                 field_values = []
#                 if attributes[x]["type"] == "TYPE_MESSAGE":
#                     for j in range(len(attributes[x]["fields"])):
#                         field_values.append(test_case[x][j])
#                         tmp_object[attributes[x]['fields'][j]['name']] = field_values[j]
#                     tmp_array.append(tmp_object)
#                     json_object[attributes[x]['name']] = tmp_array
#                 else:
#                     for j in range(len(test_case[x])):
#                         field_values.append(test_case[x][j])
#                     json_object[attributes[x]['name']] = field_values
#             else:
#                 json_object[attributes[x]['name']] = test_case[x]
#         testcases_params.append(json_object)
#     return testcases_params

# if __name__ == "__main__":
#     expression = "code.road1.road2"
#     temp = json.loads(
#         '{"code": {"SKFlipRoadInfoGoRoomRSPCode_ERROR": -1, "SKFlipRoadInfoGoRoomRSPCode_SUCCESS": 0, "road1": {"road2":3}}}')
#
#     if '.' in expression:
#         for i in expression.split('.'):
#             temp = temp[i]
#     print(temp)
#     attributes = [
#         {
#             "enum_values": [
#                 {
#                     "SKFlipRoadInfoGoRoomRSPCode_ERROR": -1
#                 },
#                 {
#                     "SKFlipRoadInfoGoRoomRSPCode_SUCCESS": 0
#                 }
#             ],
#             "is_repeated": False,
#             "name": "code",
#             "number": 1,
#             "type": "TYPE_ENUM"
#         },
#         {
#             "is_repeated": True,
#             "name": "road1",
#             "number": 2,
#             "range": [
#                 1, 2, 3
#             ],
#             "type": "TYPE_INT64"
#         },
#         {
#             "is_repeated": True,
#             "name": "road2",
#             "number": 3,
#             "range": [
#                 10, 22, 44, 100
#             ],
#             "type": "TYPE_INT64"
#         }
#     ]
#     parameters = []
#
#     n = len(attributes)
#
#     for i in range(n):
#         if attributes[i]["is_repeated"]:
#             if attributes[i]["type"] == "TYPE_MESSAGE":
#                 y = []
#                 x = []
#                 for j in range(len(attributes[i]["fields"])):
#                     x.append(attributes[i]["fields"][j]["range"])
#                 for a in AllPairs(x):
#                     y.append(a)
#                 parameters.append(y)
#             else:
#                 y = []
#                 for j in range(len(attributes[i]["range"])):
#                     temp = [attributes[i]["range"][j]]
#                     y.append(temp)
#                 sub_array = random.sample(attributes[i]["range"], random.randint(1, len(attributes[i]["range"])))
#
#                 y.append(sub_array)
#                 parameters.append(y)
#         else:
#             if attributes[i]["type"] == "TYPE_ENUM":
#                 w = []
#                 for j in range(len(attributes[i]["enum_values"])):
#                     w.append(next(iter(attributes[i]["enum_values"][j].values())))
#                 parameters.append(w)
#             else:
#                 parameters.append(attributes[i]["range"])
#     print(parameters)
#     test_cases = AllPairs(parameters)
#
#     for i, test_case in enumerate(test_cases):
#
#         json_object = {}
#         for x in range(len(attributes)):
#             if attributes[x]["is_repeated"]:
#                 tmp_object = {}
#                 tmp_array = []
#                 field_values = []
#                 if attributes[x]["type"] == "TYPE_MESSAGE":
#                     for j in range(len(attributes[x]["fields"])):
#                         field_values.append(test_case[x][j])
#                         tmp_object[attributes[x]['fields'][j]['name']] = field_values[j]
#                     tmp_array.append(tmp_object)
#                     json_object[attributes[x]['name']] = tmp_array
#                 else:
#                     for j in range(len(test_case[x])):
#                         field_values.append(test_case[x][j])
#                     json_object[attributes[x]['name']] = field_values
#             else:
#                 json_object[attributes[x]['name']] = test_case[x]
#         print(i, json.dumps(json_object))
