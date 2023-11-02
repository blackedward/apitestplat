import json

from common.Inventory import Inventory


def generate_case(schema_file_object, case_rule, is_return_mix, data_type):
    # 读取配置文件
    property = schema_file_object["property"]
    url = property["url"]
    case_desc = property["desc"]
    method = property["method"]
    doc = property["doc"]
    headers = property["headers"]
    schema_type = property["schemaType"]
    valid_equivalence_class = property["validEquivalenceClass"]
    invalid_equivalence_class = property["invalidEquivalenceClass"]
    valid_equivalence_class_assert = valid_equivalence_class["asserts"]
    invalid_equivalence_class_assert = invalid_equivalence_class["asserts"]
    valid_equivalence_class_case_level = valid_equivalence_class["caseLevel"]
    invalid_equivalence_class_case_level = invalid_equivalence_class["caseLevel"]
    schema = schema_file_object["schema"]

    item_list = []
    # 读取schema为每个属性生成条件
    if schema is not None and len(schema) > 0:
        for jo in schema:
            name = jo["name"]
            desc = jo["desc"]
            type = jo["type"]
            config = jo["config"]
            if data_type == 1:
                item_list.append(Inventory.gen_single_field(static_generator, name, desc, type, config))
            else:
                item_list.append(Inventory.gen_single_field(dynamic_generator, name, desc, type, config))

    if not is_return_mix:
        return item_list

    # 确定用例生成规则
    if case_rule == CaseRule.ORT:  # 正交法
        key = NoUtil.gen_py_ort_no()
        case_list = rule.ort(key, item_list)
    else:  # 笛卡尔积
        # 接口总字段数
        prop_size = len(item_list)
        # 每个字段数，生成的条件总数总集合
        item_size_list = [len(item) for item in item_list]
        case_list = rule.cartesian(item_size_list, item_list, [])

    # 封装成导入用例的格式
    result = []
    for field_array in case_list:
        field_object = {}
        case_name = case_desc
        is_valid_equivalence_class = True
        for obj in field_array:
            field_type = obj["type"]
            key = obj["key"]
            desc = obj["desc"]
            value = obj["value"]
            field_object[key] = value
            case_name += " " + desc
            if field_type == "invalidEquivalenceClass" and is_valid_equivalence_class:
                is_valid_equivalence_class = False

        cs = {
            "url": url,
            "method": method,
            "desc": "有效等价类 " + case_name if is_valid_equivalence_class else "无效等价类 " + case_name,
            "level": valid_equivalence_class_case_level if is_valid_equivalence_class else invalid_equivalence_class_case_level,
            "doc": doc,
            "headers": headers
        }

        if schema_type.lower() == "data":
            cs["data"] = json.dumps(field_object, ensure_ascii=False)
        elif schema_type.lower() == "json":
            cs["json"] = json.dumps(field_object, ensure_ascii=False).replace("\\\\\\", "\\").replace("\\\"", "\"")
        else:
            cs["params"] = json.dumps(field_object, ensure_ascii=False)

        cs[
            "asserts"] = valid_equivalence_class_assert if is_valid_equivalence_class else invalid_equivalence_class_assert
        result.append(cs)

    return result
