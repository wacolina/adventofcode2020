# Advent Code 2020
# Day 8, step 2

def main():
    valuesMap = {}
    valuesMove = {}
    step = 1

    f = open("8.2-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesMap[step] = x
        valuesMove[step] = False
        step += 1

    f.close()

    acc = 0
    step = 1
    tries = 1
    sameStep = False
    changedValues = {}
    newValuesMap = valuesMap.copy()

    while not sameStep:
        value = newValuesMap[step]
        if valuesMove[step]:
            acc = 0
            step = 1
            tries += 1
            newValuesMap = valuesMap.copy()
            for move in valuesMove:
                valuesMove[move] = False
        elif step == len(valuesMove):
            print('Last step reached. Current acc: ' + str(acc))
            sameStep = True
        elif value[:3] == 'nop':
            if changedValues.get(step) or len(changedValues) == tries:
                valuesMove[step] = True
                step += 1
            else:
                changedValues[step] = value
                newValuesMap[step] = 'jmp ' + value[4:]
        elif value[:3] == 'acc':
            sign = value[4:5]
            operateValue = int(value[5:])
            if sign == '+':
                acc += operateValue
            elif sign == '-':
                acc -= operateValue
            valuesMove[step] = True
            step += 1
        elif value[:3] == 'jmp':
            if changedValues.get(step) or len(changedValues) == tries:
                valuesMove[step] = True
                sign = value[4:5]
                operateValue = int(value[5:])
                if sign == '+':
                    step += operateValue
                elif sign == '-':
                    step -= operateValue
            else:
                changedValues[step] = value
                newValuesMap[step] = 'nop ' + value[4:]


if __name__ == "__main__":
    main()