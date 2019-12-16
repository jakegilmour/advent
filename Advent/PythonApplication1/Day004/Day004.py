def TwoAdjacentDigitsSame(number):
    digits = str(number)
    streak = False

    currentString = digits[0]
    
    for i in range (1, len(digits)):
        if digits[i] == currentString[0]:
            currentString += digits[i]
        elif len(currentString) == 2:
            return True
        else:
            currentString = digits[i]

    if len(currentString) == 2:
        return True

    return False

def ThreeDigitsSame(number):
    digits = str(number)

    for i in range(1, len(digits)):
        if digits[i] == digits [i + 1] and digits [i + 1] == digits[i + 2]:
            return True

    return False

def DigitsAlwaysIncrease(number):
    digits = str(number)

    for i in range (0, len(digits) - 1):
        if int(digits[i]) > int(digits[i + 1]):
            return False

    return True

def ValidCode(number):
    return DigitsAlwaysIncrease(number) and TwoAdjacentDigitsSame(number)

min = 372304
max = 847060
numPossible = max - min
count = 0

for x in range (min, max):
    if ValidCode(x):
        count += 1

print(count)