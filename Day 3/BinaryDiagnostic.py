# Advent of Code (2021)
# Day 3: Binary Diagnostic

# Helpers

from lib2to3.pgen2.pgen import generate_grammar


def importData():
    scanData = open('input.txt', 'r')
    return scanData

def computeMostAndLeastCommon(data):
    """
    Given the data this function returns a tuple of 3 lists.
    The first list contains the "most" common value for each position i.e.
    1010 -> 1 is the most common value for position (0), 
            0 is the most common value for position (1),
            1 is the most common value for position (2),
            0 is the most common value for position (3).

    The second list contains the "least" common value for each position (opposite of the first list).
    0101 -> 0 is the least common value for position (0) etc.

    The third list is just the input data itself but in a list data structure
    """
    occuranceofZero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    occuranceofOne  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dataList = list()
    
    for bit in data:
        newList = list(bit)
        
        end = len(newList) - 1  # Removing the last element from the list; the last element is the char "\n"
        newList = newList[0:end]
        dataList.append(newList) # Saving every binary number in a list for future use case. (part -2) 
        
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

    return (mostCommon, leastCommon, dataList)


# Main
# Power consumption of the submarine - Part 1
def powerConsumption(data):
    """
    Calculates the power consumption of the submarine.
    """

    x = computeMostAndLeastCommon(data)
    mostCommon, leastCommon = x[0], x[1]

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
    Oxgen generator rating and the CO2 scrubber rating
    """

    # Helpers
    def generateMatch(xs, index, match):
        """
        ListOflists, Natural, Natural -> List
            xs:    list to be considered.
            index: position in each element of the list to be considered.
            match: the value xs[index] is compared against
        returns only valid xs's that have a 'match' at xs[index]

        """
        result = list()        
        for elem in xs:
            if elem[index] == str(match):
                result.append(elem)
        return result

    def generateOxyAndCO2(xs, val):
        """
        ListOflists, List -> List
            xs  -> The input data in list data structure
            val -> Either (mostCommon or leastCommon).
        This function assumes there will be no ties when comparing values.
        len(2) and both binary numbers match the val[index]
        """
        for index in range(12):
            result = generateMatch(xs, index, val[index])
            xs = result
            if len(xs) == 1:
                break
        return xs

    # Main
    mostCommon, leastCommon, dataList = computeMostAndLeastCommon(data)
    oxyGenRatingBinary   = generateOxyAndCO2(dataList, mostCommon)
    scrubberRatingBinary = generateOxyAndCO2(dataList, leastCommon)

    oxyGenRating   = "".join(str(x) for x in oxyGenRatingBinary[0])   
    scrubberRating = "".join(str(x) for x in scrubberRatingBinary[0])

    return int(oxyGenRating, 2) * int(scrubberRating, 2)


lifeSR = lifeSupportRating(importData())
print(lifeSR)
