def GetOpCode(intcode, currentIndex):
    return int(intcode[currentIndex])

def GetNumOne(intcode, currentIndex):
    return int(intcode[int(intcode[currentIndex + 1])])

def GetNumTwo(intcode, currentIndex):
    return int(intcode[int(intcode[currentIndex + 2])])

def GetOutputPosition(intcode, currentIndex):
    return int(intcode[currentIndex + 3])

def OpCodeAdd(numOne, numTwo):
    return numOne + numTwo

def OpCodeEscape(finalNumber):
    print(finalNumber)

def OpCodeMultiply(numOne, numTwo):
    return numOne * numTwo

def ApplyOpCode(numOne, numTwo, opCode):
    if opCode == 1:
        return OpCodeAdd(numOne, numTwo)
    else:
        return OpCodeMultiply(numOne, numTwo)

def Operate(intcode, currentIndex):
    numOne = GetNumOne(intcode, currentIndex)
    numTwo = GetNumTwo(intcode, currentIndex)
    opCode = GetOpCode(intcode, currentIndex)
    outputPosition = GetOutputPosition(intcode, currentIndex)

    if opCode == 99:
        return -1
    elif opCode != 1 and opCode != 2 :
        return -1
    else:
        opCodeValue = ApplyOpCode(numOne, numTwo, opCode)

        if opCodeValue == 19690720:
            return 1
        else:
            intcode[outputPosition] = opCodeValue
            return Operate(intcode, currentIndex + 4)

noun = 0
verb = 0
output = -1

for n in range (0, 172):
    if output != -1:
        break
    for v in range (0, 172):
        with open(r"C:\Users\Jake\Documents\Git\advent\Advent\PythonApplication1\Day002\input.txt") as input:
            intcode = input.read().split(',')
            intcode[1] = n
            intcode[2] = v
            output = Operate(intcode, 0)
            if output != -1:
                noun = n
                verb = v
                break

print(100 * noun + verb)

