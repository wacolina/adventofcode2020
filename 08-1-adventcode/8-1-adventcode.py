# Advent Code 2020
# Day 8, step 1
valuesMap = {}
valuesMove = {}
acc = 0
step = 1


def operateOnInstruction(value):
    global step
    global acc

    if value[:3] == 'nop':
        valuesMove[step] = True
        step += 1
    elif value[:3] == 'acc':
        sign = value[4:5]
        if sign == '+':
            acc += int(value[5:])
        elif sign == '-':
            acc -= int(value[5:])
        valuesMove[step] = True
        step += 1
    elif value[:3] == 'jmp':
        valuesMove[step] = True
        sign = value[4:5]
        if sign == '+':
            step += int(value[5:])
        elif sign == '-':
            step -= int(value[5:])


def main():
    line = 1

    f = open("8.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesMap[line] = x
        valuesMove[line] = False
        line += 1

    f.close()

    sameStep = False
    global step

    while not sameStep:
        value = valuesMap[step]
        if valuesMove[step]:
            print('Same step found. Current acc: ' + str(acc))
            sameStep = True
        else:
            operateOnInstruction(value)


if __name__ == "__main__":
    main()