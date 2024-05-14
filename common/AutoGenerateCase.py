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
                y = []
                for j in range(len(attribute["range"])):
                    y.append(str_to_bool(attribute["range"][j]))
                parameters.append(y)
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
                field_values = []
                if attributes[x]["type"] == "TYPE_MESSAGE":
                    field_values = [process_message_field_assign(attributes[x], test_case[x])]
                    if is_2d_array(field_values):
                        field_values = field_values[0]
                elif attributes[x]["type"] != "TYPE_MESSAGE" and attributes[x]["is_repeated"]:
                    for j in range(len(test_case[x])):
                        field_values.append(test_case[x][j])
                elif attributes[x]["type"] == "TYPE_BOOL":
                    for j in range(len(test_case[x])):
                        field_values.append(bool(test_case[x][j]))
                else:
                    for j in range(len(test_case[x])):
                        field_values.append(test_case[x][j])
                json_object[attributes[x]['name']] = field_values
            else:
                caseval = test_case[x]
                if attributes[x]["type"] == "TYPE_MESSAGE":
                    json_object[attributes[x]['name']] = process_message_field_assign(attributes[x], caseval)
                elif attributes[x]["type"] == "TYPE_BOOL":
                    json_object[attributes[x]['name']] = bool(caseval)
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
        if is_2d_array(field["fields"]):
            field["fields"] = field["fields"][0]
        tmp_object = {}
        for subfield, subcaseval in zip(field["fields"], caseval):
            tmp_object[subfield["name"]] = process_message_field_assign(subfield, subcaseval)
        return tmp_object
    elif field["type"] == "TYPE_BOOL":
        return bool(caseval)
    else:
        return caseval


def str_to_bool(s):
    s = s.lower()
    if s == "true":
        return True
    elif s == "false":
        return False
    else:
        raise ValueError(f"Cannot convert {s} to bool")
