import random
import decimal

illegalString = "!@#$%^&*()_+-,.<>"
legalString = "123456790abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numString = "0123456789"


def randomInt(minimum, maximum):
    return random.randint(minimum, maximum)


def randomLegalString(minLen, maxLen):
    length = randomInt(minLen, maxLen)
    return ''.join(random.choice(legalString) for _ in range(length))


def randomNumString(minLen, maxLen):
    length = randomInt(minLen, maxLen)
    return ''.join(random.choice(numString) for _ in range(length))


def randomIllegalString(minLen, maxLen):
    length = randomInt(minLen, maxLen)
    return ''.join(random.choice(illegalString) for _ in range(length))


def randomLegalStringByLength(length):
    return ''.join(random.choice(legalString) for _ in range(length))


def randomNumStringByLength(length):
    return ''.join(random.choice(numString) for _ in range(length))


def randomIllegalStringByLength(length):
    return ''.join(random.choice(illegalString) for _ in range(length))


def randomBigDecimal(min, max):
    minInt = int(min)
    maxInt = int(max)

    minStr = str(min)
    maxStr = str(max)

    minPointIndex = minStr.find(".")
    maxPointIndex = maxStr.find(".")

    if minPointIndex == -1 and maxPointIndex == -1:
        return decimal.Decimal(randomInt(minInt, maxInt))
    else:
        minDecimalLen = 0 if minPointIndex == -1 else len(minStr[minPointIndex + 1:]) - 1
        maxDecimalLen = 0 if maxPointIndex == -1 else len(maxStr[maxPointIndex + 1:]) - 1

        decimal_len = max(minDecimalLen, maxDecimalLen)
        patten = "."
        for i in range(decimal_len):
            patten += str(random.randint(0, 9))

        value = randomInt(minInt, maxInt)
        bigDecimalValue = decimal.Decimal(str(value) + patten)
        while bigDecimalValue < min or bigDecimalValue > max:
            patten = "."
            for i in range(decimal_len):
                patten += str(random.randint(0, 9))
            value = randomInt(minInt, maxInt)
            bigDecimalValue = decimal.Decimal(str(value) + patten)
        return bigDecimalValue
