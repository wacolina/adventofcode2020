# Advent Code 2020
# Day 10, step 1

def main():
    valuesInput = []

    f = open("10.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(int(x))

    f.close()

    valuesInput.sort()
    valuesInput.append(valuesInput[len(valuesInput) - 1] + 3)

    acc = 0
    diff1 = 0
    diff2 = 0
    diff3 = 0
    for value in valuesInput:
        diff = value - acc
        if diff == 1:
            acc += 1
            diff1 += 1
        elif diff == 2:
            acc += 2
            diff2 += 1
        elif diff == 3:
            acc += 3
            diff3 += 1
    print('Result: ' + str(diff1 * diff3))


if __name__ == "__main__":
    main()