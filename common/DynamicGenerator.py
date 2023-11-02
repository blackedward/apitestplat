from common import RandomUtil
from common.Description import Description
from common.GeneratorAbstract import Generator
from common.StaticGenerator import StaticGenerator


class DynamicGenerator(Generator):  # 动态生成测试用例的类
    def __init__(self, filter, Description, dbService):
        self.filter = filter
        self.Description = Description
        self.dbService = dbService

    # 生成字段类型为String的用例
    def genString(self, key, desc, allowIllegal, allowEmpty, minLen, maxLen, allowNull):
        result = []

        # 1. null
        if allowNull:
            result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4Null(key, desc), None, key))
        else:
            result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4Null(key, desc), None, key))

        # 2. empty
        if allowEmpty:
            result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4Empty(key, desc), "", key))
        else:
            result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4Empty(key, desc), "", key))

        # 3. length
        # A. within length range
        randomLegalString = self.function("randomLegal", minLen, maxLen)
        result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4Length(key, desc, minLen, maxLen),
                                 randomLegalString, key))

        # B. exactly maximum length
        randomMax = self.function("randomLegal", maxLen)
        while randomMax == randomLegalString:
            randomMax = RandomUtil.randomLegalStringByLength(maxLen)
        result.append(
            self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4EqualsMaxLength(key, desc, maxLen), randomMax,
                       key))

        # C. exactly minimum length
        randomMin = self.function("randomLegal", minLen)
        while randomMin == randomLegalString or randomMin == randomMax:
            randomMin = RandomUtil.randomLegalStringByLength(minLen)
        result.append(
            self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4EqualsMinLength(key, desc, minLen), randomMin,
                       key))

        # D. exactly maximum length + 1
        randomMaxAddOne = self.function("randomLegal", maxLen + 1)
        result.append(
            self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4GreaterLength(key, desc, maxLen, 1),
                       randomMaxAddOne, key))

        # E. exactly minimum length - 1
        randomMinSubOne = self.function("randomLegal", minLen - 1)
        result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4LessLength(key, desc, minLen, 1),
                                 randomMinSubOne, key))

        # 4. illegal characters
        if allowIllegal is not None:
            randomIllegalString = self.function("randomIllegal", minLen, maxLen)
            if allowIllegal:
                result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS,
                                         Description.desc4IllegalLength(key, desc, minLen, maxLen), randomIllegalString,
                                         key))
            else:
                result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS,
                                         Description.desc4IllegalLength(key, desc, minLen, maxLen), randomIllegalString,
                                         key))
        return result

    def gen_number(self, key, desc, min_val, max_val, allow_null):
        return StaticGenerator.gen_number(self, key, desc, min_val, max_val, allow_null)


class CaseType:
    VALID_EQUIVALENCE_CLASS = "VALID_EQUIVALENCE_CLASS"
    INVALID_EQUIVALENCE_CLASS = "INVALID_EQUIVALENCE_CLASS"
