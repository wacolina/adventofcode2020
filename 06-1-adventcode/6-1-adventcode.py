# Advent Code 2020
# Day 6, step 1

def main():
    valuesInput = []
    conStr = ''
    stepsCount = 0

    f = open("6.1-input", "r")
    num_lines = sum(1 for line in open("6.1-input", "r"))
    for x in f:
        x = x.rstrip('\n')
        if x == '':
            stepsCount += 1
            valuesInput.append(conStr)
            conStr = ''
            continue

        if conStr == '':
            conStr = x
        else:
            conStr = conStr + ' ' + x

        if stepsCount == num_lines - 1:
            valuesInput.append(conStr)

        stepsCount += 1
    f.close()

    count = 0

    for value in valuesInput:
        answers = []
        for char in value:
            if char.isalpha():
                if any(char in s for s in answers):
                    continue
                else:
                    answers.append(char)
        count += len(answers)

    print('Count: ' + str(count))


if __name__ == "__main__":
    main()