# Advent Code 2020
# Day 3, step 2

def checkRoutes(valuesInput, positionXChange, positionYChange):
    trees = 0
    movingPoint = [1, 0]

    for x in valuesInput:
        if positionYChange == 1 or valuesInput.index(x) % 2 == 0:
            if valuesInput.index(x) == len(valuesInput) - 1:
                break

            newXPoint = movingPoint[0] + positionXChange
            newYPoint = movingPoint[1] + positionYChange

            if newXPoint <= 31:
                movingPoint = [newXPoint, newYPoint]
                if valuesInput[movingPoint[1]][movingPoint[0] - 1] == '#':
                    trees += 1
            else:
                newLinePoint = newXPoint - 31
                movingPoint = [newLinePoint, newYPoint]
                if valuesInput[movingPoint[1]][movingPoint[0] - 1] == '#':
                    trees += 1

    return trees


def main():
    valuesInput = []
    points = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees = 1

    f = open("3.2-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    for point in points:
        trees *= checkRoutes(valuesInput, point[0], point[1])

    print('Trees: ' + str(trees))


if __name__ == "__main__":
    main()