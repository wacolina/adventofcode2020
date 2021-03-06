# Advent Code 2020
# Day 2, step 2

def main():
    valuesInput = []
    matchPasswords = 0

    f = open("2.2-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    for x in valuesInput:
        prepared = x.split('-')
        prepared2 = prepared[1].split(' ')

        minOccur = prepared[0]
        maxOccur = prepared2[0]
        key = prepared2[1].split(':')[0]
        code = prepared2[2]

        charAppears = code.count(key)
        if code[int(minOccur) - 1] == key and code[int(maxOccur) - 1] != key:
            print('1. Min occur: ' + str(minOccur) + '. Max occur: ' + str(maxOccur) + '. Key: ' + str(key) + '. Code: ' + code + '. Count: ' + str(charAppears))
            matchPasswords += 1
        if code[int(minOccur) - 1] != key and code[int(maxOccur) - 1] == key:
            print('2. Min occur: ' + str(minOccur) + '. Max occur: ' + str(maxOccur) + '. Key: ' + str(key) + '. Code: ' + code + '. Count: ' + str(charAppears))
            matchPasswords += 1

    print('Matching passwords: ' + str(matchPasswords))


if __name__ == "__main__":
    main()