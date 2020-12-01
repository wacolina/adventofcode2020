# Advent Code 2020
# Day 1, step 1

def main():
    valuesInput = []
    searchedValued = 0

    f = open("1.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    valuesInput = list(map(int, valuesInput))

    for x in valuesInput:
        for y in valuesInput:
            result = x + y
            if result == 2020:
                searchedValued = x * y
                break
        if searchedValued > 0:
            break

    print('Searched value: ' + str(searchedValued))

if __name__ == "__main__":
    main()