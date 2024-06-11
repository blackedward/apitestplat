from common.log import logger


def assert_value(data, path, expected_value, operator):
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, list):
            current = current[int(key)]
        else:
            current = current[key]

    operators = {
        'is_equal_to': is_equal_to,
        'is_less_than': is_less_than,
        'is_greater_than': is_greater_than,
        'is_less_than_or_equal_to': is_less_than_or_equal_to,
        'is_greater_than_or_equal_to': is_greater_than_or_equal_to,
        'string_equal_to': string_equal_to,
        'is_not_equal_to': is_not_equal_to,
        'matches': matches,
        'is_none': is_none,
        'is_not_none': is_not_none,
        'contains': contains,
        'is_empty': is_empty,
        'is_not_empty': is_not_empty,
    }

    if operator in operators:
        return operators[operator](current, expected_value)
    else:
        raise ValueError(f"Unsupported operator: {operator}")


def is_equal_to(a, b):
    result = (a == b) if isinstance(a, bool) and isinstance(b, bool) else (str(a) == str(b))
    return result


def is_less_than(a, b):
    a, b = float(a), float(b)
    result = a < b
    return result


def is_greater_than(a, b):
    a, b = float(a), float(b)
    result = a > b
    return result


def is_less_than_or_equal_to(a, b):
    a, b = float(a), float(b)
    result = a <= b
    return result


def is_greater_than_or_equal_to(a, b):
    a, b = float(a), float(b)
    result = a >= b
    return result


def string_equal_to(a, b):
    result = str(a) == str(b)
    return result


def is_not_equal_to(a, b):
    result = (a != b) if isinstance(a, bool) and isinstance(b, bool) else (str(a) != str(b))
    return result


def matches(a, pattern):
    import re
    result = bool(re.match(pattern, str(a)))
    return result


def is_none(a, b=None):
    result = (a is None)
    return result


def is_not_none(a, b=None):
    result = (a is not None)
    return result


def contains(a, b):
    result = str(b) in str(a)
    return result


def is_empty(a, b=None):
    result = not a
    return result


def is_not_empty(a, b=None):
    result = bool(a)
    return result


# if __name__ == '__main__':
#     data = {
#         "banned_platform_contact_info": [],
#         "info": [
#             {
#                 "clubid": 12097,
#                 "icon": "https://jiaruitesting.s3.ap-southeast-1.amazonaws.com/club_icon/250785920230509143025.jpg",
#                 "league_list": [],
#                 "name": "KK - KINGS",
#                 "num": 1741,
#                 "platform": "Japan",
#                 "role": 1,
#                 "room_num": 0,
#                 "room_num_h5": 0
#             },
#             {
#                 "clubid": 12848,
#                 "icon": "http://47.91.130.120:10012/poker/headicon/head/430294a7c0c98e8.jpg",
#                 "league_list": [
#                     {
#                         "leagueid": 107,
#                         "official": 1,
#                         "room_num": 185,
#                         "room_num_h5": 0
#                     }
#                 ],
#                 "name": "Fish Here",
#                 "num": 0,
#                 "platform": "Brazil",
#                 "role": 2,
#                 "room_num": 0,
#                 "room_num_h5": 0
#             }
#         ],
#         "is_banned_create_club_platform": False,
#         "last_leave_time": "0",
#         "platform_solo_agent_clubid": 0,
#         "platform_solo_agent_contact_info": ""
#     }
#
#     assert_value(data, 'info.0.name', 'KK - KINGS', 'is_equal_to')
#     assert_value(data, 'info.1.league_list.0.leagueid', 107, 'is_equal_to')
#     assert_value(data, 'info.0.num', 200, 'is_less_than_or_equal_to')
#     assert_value(data, 'info.0.platform', 'Japan', 'string_equal_to')
#     assert_value(data, 'info.0.clubid', 12098, 'is_not_equal_to')
#     assert_value(data, 'info.1.icon', 'http://47.91.130.120:10012/poker/headicon/head/430294a7c0c98e8.jpg', 'matches')
#     assert_value(data, 'info.0.platform', None, 'is_not_none')
#     assert_value(data, 'info.0.icon', 'club_icon', 'contains')
#     assert_value(data, 'info.1.league_list', [], 'is_not_empty')
#     assert_value(data, 'is_banned_create_club_platform', False, 'is_equal_to')
