def MapWirePoints(wire):
    wirePoints = []
    currentR = 0
    currentU = 0
    for wireIndex in range (0, len(wire)):
        key = wire[wireIndex]
        if 'L' in key:
            distance = int(key.replace("L", ""))
            while distance > 0:
                currentR -= 1
                distance -= 1
                wirePoints.append((currentR, currentU))
        elif 'R' in key:
            distance = int(key.replace("R", ""))
            while distance > 0:
                currentR += 1
                distance -= 1
                wirePoints.append((currentR, currentU))
        elif 'U' in key:
            distance = int(key.replace("U", ""))
            while distance > 0:
                currentU += 1
                distance -= 1
                wirePoints.append((currentR, currentU))
        else:
            distance = int(key.replace("D", ""))
            while distance > 0:
                currentU -= 1
                distance -= 1
                wirePoints.append((currentR, currentU))
    return wirePoints


def MoveUD(key):
    if 'D' in key:
        distance = key.replace("D", "")
        return -1 * int(distance)
    else:
        distance = key.replace("U", "")
        return int(distance)

def WirePoint(wire, intersectionIndex):
    distanceR = 0
    distanceU = 0
    for move in range (0, intersectionIndex + 1):
        if 'R' in wire[move] or 'L' in wire[move]:
            distanceR += MoveRL(wire[move])
        else:
            distanceU += MoveUD(wire[move])

    return distanceR, distanceU

def ManhattanDistance(distanceR, distanceU):
    return abs(distanceR) + abs(distanceU)


input = open(r"C:\Users\Jake\Documents\Git\advent\Advent\PythonApplication1\Day003\input.txt")
wireOne = input.readline().split(',')
wireTwo = input.readline().split(',')

#wireOne = ["R1","U3"]
#wireTwo = ["U3","R1"]

wireOnePoints = MapWirePoints(wireOne)
wireTwoPoints = MapWirePoints(wireTwo)

distances = []

intersection = list(set(wireOnePoints).intersection(set(wireTwoPoints)))
steps = []

for i in range (0, len(intersection)):
    stepsA = list(wireOnePoints).index(intersection[i])
    stepsB = list(wireTwoPoints).index(intersection[i])
    totalSteps = int(stepsA) + int(stepsB) + 2
    steps.append(totalSteps)




a = 0
print(min(steps))


