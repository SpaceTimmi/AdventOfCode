# Advent of Code (2021)
# Day 3: Binary Diagnostic

# Helpers
def importData():
    scanData = open('input.txt', 'r')
    return scanData

def computeMostAndLeastCommon(data):
    """
    Given the data this function returns a tuple of 2 lists.
    The first list contains the "most" common value for each position i.e.
    1010 -> 1 is the most common value for position (0), 
            0 is the most common value for position (1),
            1 is the most common value for position (2),
            0 is the most common value for position (3).

    The second list contains the "least" common value for each position (opposite of the first list).
    0101 -> 0 is the least common value for position (0) etc.
    """
    occuranceofZero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    occuranceofOne  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for bit in data:
        newList = list(bit)
        
        # Removing the last element from the list; the last element is the char "\n"
        end = len(newList) - 1
        newList = newList[0:end]  
        
        for index, element in enumerate(newList):
            if int(element) == 0:
                occuranceofZero[index] += 1
            elif int(element) == 1:
                occuranceofOne[index] += 1


    mostCommon  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    leastCommon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(12):
        if occuranceofZero[i] > occuranceofOne[i]:  
            mostCommon[i]  = 0
            leastCommon[i] = 1
        else:
            mostCommon[i]  = 1
            leastCommon[i] = 0

    return (mostCommon, leastCommon)


# Power consumption of the submarine - Part 1
def powerConsumption(data):
    """
    Calculates the power consumption of the submarine.
    """

    mostCommon, leastCommon = computeMostAndLeastCommon(data)

    mostCommonBinary  = "".join(str(x) for x in mostCommon)
    leastCommonBinary = "".join(str(y) for y in leastCommon)
    
    gammaRate   = int(mostCommonBinary, 2) 
    epsilonRate = int(leastCommonBinary, 2)

    return gammaRate * epsilonRate


powerC = powerConsumption(importData())
print(powerC)


# Life support rating - Part 2
def lifeSupportRating(data):
    """
    Computes the life support rating of the submarine.
    """

    mostCommon, leastCommon = computeMostAndLeastCommon(data)




    return 
    