# Advent Code 2020
# Day 9, step 2

def main():
    valuesInput = []

    f = open("9.2-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(int(x))

    f.close()

    step = 0
    preamble = 25
    firstNotMatchValue = 0

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
            firstNotMatchValue = valuesInput[step + preamble]
            print('First not found value: ' + str(firstNotMatchValue))
            break
        step += 1

    contiguousSetFound = False
    contiguousSet = []

    while not contiguousSetFound:
        addedValues = 0
        for value in valuesInput:
            addedValues += value
            contiguousSet.append(value)
            if addedValues == firstNotMatchValue:
                contiguousSetFound = True
                break
            elif addedValues < firstNotMatchValue:
                continue
            else:
                del valuesInput[0]
                contiguousSet.clear()
                break

    contiguousSet.sort()
    encryptionWeakness = contiguousSet[0] + contiguousSet[len(contiguousSet) - 1]
    print('contiguousSet: ' + str(encryptionWeakness))


if __name__ == "__main__":
    main()