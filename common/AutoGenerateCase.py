import json
import random
from common.log import logger

from allpairspy import AllPairs


def generate_test_cases(attributes):
    testcases_params = []
    parameters = []
    n = len(attributes)

    for i in range(n):
        if attributes[i]["is_repeated"]:
            if attributes[i]["type"] == "TYPE_MESSAGE":
                y = []
                x = []
                for j in range(len(attributes[i]["fields"])):
                    x.append(attributes[i]["fields"][j]["range"])
                for a in AllPairs(x):
                    y.append(a)
                parameters.append(y)
            else:
                y = []
                for j in range(len(attributes[i]["range"])):
                    temp = [attributes[i]["range"][j]]
                    y.append(temp)
                sub_array = random.sample(attributes[i]["range"], random.randint(1, len(attributes[i]["range"])))

                y.append(sub_array)
                parameters.append(y)
        else:
            # if attributes[i]["type"] == "TYPE_ENUM":
            #     w = []
            #     for j in range(len(attributes[i]["enum_values"])):
            #         w.append(next(iter(attributes[i]["enum_values"][j].values())))
            #     parameters.append(w)
            # else:
            parameters.append(attributes[i]["range"])
    test_cases = AllPairs(parameters)

    for i, test_case in enumerate(test_cases):

        json_object = {}
        for x in range(len(attributes)):
            if attributes[x]["is_repeated"]:
                tmp_object = {}
                tmp_array = []
                field_values = []
                if attributes[x]["type"] == "TYPE_MESSAGE":
                    for j in range(len(attributes[x]["fields"])):
                        field_values.append(test_case[x][j])
                        tmp_object[attributes[x]['fields'][j]['name']] = field_values[j]
                    tmp_array.append(tmp_object)
                    json_object[attributes[x]['name']] = tmp_array
                else:
                    for j in range(len(test_case[x])):
                        field_values.append(test_case[x][j])
                    json_object[attributes[x]['name']] = field_values
            else:
                json_object[attributes[x]['name']] = test_case[x]
        testcases_params.append(json_object)
    return testcases_params

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
