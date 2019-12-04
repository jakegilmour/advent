
totalMass = 0

with open(r"C:\Users\Jake\Documents\Git\advent\2019\Day001\input.txt") as input:
    currentLine = input.readline()
    while currentLine:
        currentMass = int(currentLine)
        currentMass = (currentMass // 3) - 2
        totalMass += currentMass

        while currentMass >= 0:
            currentMass = (currentMass // 3) - 2

            if (currentMass > 0):
                totalMass += currentMass

        currentLine = input.readline()
            

print(totalMass)