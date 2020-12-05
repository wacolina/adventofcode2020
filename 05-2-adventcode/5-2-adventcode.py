# Advent Code 2020
# Day 5, step 2
import math


def main():
    valuesInput = []
    seatIds = []

    f = open("5.2-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    for value in valuesInput:
        row = [0, 127]
        col = [0, 7]
        seatRow = 0
        seatCol = 0
        count = 0

        for seatDetail in value:
            if count > 6:
                if count == 9:
                    if seatDetail == 'L':
                        seatCol = col[0]
                    else:
                        seatCol = col[1]
                if seatDetail == 'L':
                    col = [col[0], col[0] + math.floor((col[1] - col[0]) / 2)]
                else:
                    col = [col[0] + math.ceil((col[1] - col[0]) / 2), col[1]]
            if count == 6:
                if seatDetail == 'F':
                    seatRow = row[0]
                else:
                    seatRow = row[1]
            else:
                if seatDetail == 'F':
                    row = [row[0], row[0] + math.floor((row[1] - row[0]) / 2)]
                else:
                    row = [row[0] + math.ceil((row[1] - row[0]) / 2), row[1]]
            count += 1
        seatIds.append(seatRow * 8 + seatCol)
    seatIds.sort()

    missingValues = []
    for seatId in seatIds:
        if seatIds.index(seatId) + 1 < len(seatIds):
            if seatIds[seatIds.index(seatId)] + 1 != seatIds[seatIds.index(seatId) + 1]:
                missingValues.append(seatIds[seatIds.index(seatId) + 1] - 1)

    print('Missing values: ' + str(missingValues))


if __name__ == "__main__":
    main()