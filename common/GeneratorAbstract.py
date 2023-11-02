import json


class Generator:
    def genString(self, key, desc, allowIllegal, allowEmpty, minLen, maxLen, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "allowIllegal": allowIllegal,
            "allowEmpty": allowEmpty,
            "minLen": minLen,
            "maxLen": maxLen,
            "allowNull": allowNull
        })

    def genNumber(self, key, desc, min, max, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "min": min,
            "max": max,
            "allowNull": allowNull
        })

    def genInDb(self, key, desc, dbId, sql, elementType, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "dbId": dbId,
            "sql": sql,
            "elementType": elementType,
            "allowNull": allowNull
        })

    def genNotInDb(self, key, desc, dbId, sql, elementType, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "dbId": dbId,
            "sql": sql,
            "elementType": elementType,
            "allowNull": allowNull
        })

    def genConst(self, key, desc, value, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "value": value,
            "allowNull": allowNull
        })

    def genInArray(self, key, desc, array, elementType, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "array": array,
            "elementType": elementType,
            "allowNull": allowNull
        })

    def genNotInArray(self, key, desc, array, elementType, allowNull):
        return json.dumps({
            "key": key,
            "desc": desc,
            "array": array,
            "elementType": elementType,
            "allowNull": allowNull
        })

    def model(self, type, desc, value, key):
        jsonObject = {
            "desc": desc,
            "value": value,
            "key": key
        }

        if type == "invalidEquivalenceClass":
            jsonObject["type"] = "invalidEquivalenceClass"
            jsonObject["desc"] = "!" + desc
        else:
            jsonObject["type"] = "validEquivalenceClass"

        return json.dumps(jsonObject)

    def getLessThanMinNum(self, min):
        jsonObject = {}
        bigDecimalStr = str(min)
        i = bigDecimalStr.find(".")

        if i == -1:
            jsonObject["num"] = min - 1
            jsonObject["step"] = 1
        else:
            length = len(bigDecimalStr[i + 1:])
            patten = "0." + "0" * (length - 1) + "1"
            jsonObject["num"] = min - float(patten)
            jsonObject["step"] = float(patten)

        return json.dumps(jsonObject)

    def getGreaterThanMaxNum(self, max):
        jsonObject = {}
        bigDecimalStr = str(max)
        i = bigDecimalStr.find(".")

        if i == -1:
            jsonObject["num"] = max + 1
            jsonObject["step"] = 1
        else:
            length = len(bigDecimalStr[i + 1:])
            patten = "0." + "0" * (length - 1) + "1"
            jsonObject["num"] = max + float(patten)
            jsonObject["step"] = float(patten)

        return json.dumps(jsonObject)

    def function(self, name, *params):
        if len(params) == 0:
            return "${%s()}" % name
        param_str = ", ".join(["'%s'" % param for param in params])
        return "${%s(%s)}" % (name, param_str)
