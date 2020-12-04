# Advent Code 2020
# Day 4, step 2

def main():
    valuesInput = []

    f = open("4.2-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    newValues = []
    searchedValues = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    conStr = ''
    validPassports = []
    validPassportsNumber = 0
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
            validPassports.append(value)

    for validPassport in validPassports:
        details = validPassport.split()
        matchingByr = [s for s in details if 'byr:' in s]
        if 1920 <= int(matchingByr[0][4:]) <= 2002:
            matchingIyr = [s for s in details if 'iyr:' in s]
            if 2010 <= int(matchingIyr[0][4:]) <= 2020:
                matchingEyr = [s for s in details if 'eyr:' in s]
                if 2020 <= int(matchingEyr[0][4:]) <= 2030:
                    matchingPid = [s for s in details if 'pid:' in s]
                    if len(matchingPid[0][4:]) == 9:
                        matchingEcl = [s for s in details if 'ecl:' in s]
                        matchingEclCode = matchingEcl[0][4:]
                        if matchingEclCode == 'amb' or matchingEclCode == 'blu' or matchingEclCode == 'brn' or matchingEclCode == 'gry' or matchingEclCode == 'grn' or matchingEclCode == 'hzl' or matchingEclCode == 'oth':
                            matchingHcl = [s for s in details if 'hcl:' in s]
                            matchingHclCode = matchingHcl[0][4:]
                            if matchingHclCode:
                                if len(matchingHclCode) == 7 and matchingHclCode[0] == '#':
                                    goNext = True
                                    for hcl in matchingHclCode:
                                        if hcl == '#':
                                            continue
                                        if hcl != 'a' and hcl != 'b' and hcl != 'c' and hcl != 'd' and hcl != 'e' and hcl != 'f' and not hcl.isdigit():
                                            goNext = False
                                            break
                                    if goNext:
                                        matchingHgt = [s for s in details if 'hgt:' in s]
                                        heightMeasure = matchingHgt[0][4:][-2:]
                                        if heightMeasure == 'cm':
                                            height = matchingHgt[0][4:].split('cm')[0]
                                            if 150 <= int(height) <= 193:
                                                validPassportsNumber += 1
                                        elif heightMeasure == 'in':
                                            height = matchingHgt[0][4:].split('in')[0]
                                            if 59 <= int(height) <= 76:
                                                validPassportsNumber += 1

    print('Passports: ' + str(validPassportsNumber))


if __name__ == "__main__":
    main()