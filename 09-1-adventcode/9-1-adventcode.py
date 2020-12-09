# Advent Code 2020
# Day 9, step 1

def main():
    valuesInput = []

    f = open("9.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(int(x))

    f.close()

    step = 0
    preamble = 25

    while step < len(valuesInput):
        subStep = step
        notFound = 0
        while subStep < step + preamble:
            mappedValues = map(lambda num: valuesInput[subStep] + num if valuesInput[subStep] != num else num, valuesInput[step:step + preamble])
            convertedList = list(mappedValues)
            if valuesInput[step + preamble] in convertedList:
                break
            else:
                notFound += 1
            subStep += 1
        if notFound == preamble:
            print('First not found value: ' + str(valuesInput[step + preamble]))
            break
        step += 1


if __name__ == "__main__":
    main()