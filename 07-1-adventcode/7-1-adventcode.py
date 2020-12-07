# Advent Code 2020
# Day 7, step 1

def main():
    valuesInput = []

    f = open("7.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    bags = ['shiny gold']
    stepsCount = 1
    done = False

    while not done:
        addedNewBag = False
        for value in valuesInput:
            for bag in bags:
                if value.find(bag) > 0:
                    newBag = value[0:value.find('bag') - 1]
                    if any(newBag in s for s in bags):
                        continue
                    else:
                        addedNewBag = True
                        bags.append(newBag)
            if len(valuesInput) == stepsCount:
                stepsCount = 0

            stepsCount += 1
        if addedNewBag is False:
            done = True

    print('Count: ' + str(len(bags) - 1))


if __name__ == "__main__":
    main()