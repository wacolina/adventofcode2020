# Advent Code 2020
# Day 3, step 1

def main():
    valuesInput = []
    trees = 0
    movingPoint = [1, 0]

    f = open("3.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    for x in valuesInput:
        if valuesInput.index(x) == len(valuesInput) - 1:
            break

        newXPoint = movingPoint[0] + 3
        newYPoint = movingPoint[1] + 1

        if newXPoint <= 31:
            movingPoint = [newXPoint, newYPoint]
            if valuesInput[movingPoint[1]][movingPoint[0] - 1] == '#':
                trees += 1
        else:
            newLinePoint = newXPoint - 31
            movingPoint = [newLinePoint, newYPoint]
            if valuesInput[movingPoint[1]][movingPoint[0] - 1] == '#':
                trees += 1

    print('Trees: ' + str(trees))


if __name__ == "__main__":
    main()