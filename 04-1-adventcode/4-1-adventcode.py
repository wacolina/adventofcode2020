# Advent Code 2020
# Day 4, step 1

def main():
    valuesInput = []

    f = open("4.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    newValues = []
    searchedValues = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    conStr = ''
    validPassports = 0
    stepsCount = 0

    for value in valuesInput:
        if value == '':
            stepsCount += 1
            newValues.append(conStr)
            conStr = ''
            continue

        if conStr == '':
            conStr = value
        else:
            conStr = conStr + ' ' + value

        if stepsCount == len(valuesInput) - 1:
            newValues.append(conStr)

        stepsCount += 1

    for value in newValues:
        count = 0
        for searchedValue in searchedValues:
            if value.find(searchedValue) >= 0:
                count += 1

        if count == 7:
            validPassports += 1

    print('Passports: ' + str(validPassports))


if __name__ == "__main__":
    main()