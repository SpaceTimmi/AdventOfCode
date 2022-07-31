# Advent of Code (2021)
# Day 3: Binary Diagnostic

# Helpers


def importData():
    """
    Takes the input.txt and returns it in a list so it's easy to work with 
    """
    scanData = open('input.txt', 'r')
    newList = list()
    
    for bit in scanData:
        tempList = list(bit)
        end = len(tempList) - 1  # Removing the last element from the list; the last element is the char "\n"
        tempList = tempList[0:end]
        newList.append(tempList)
    return newList 


def determineMostandLeast(i, xs):
    occuranceofZero = 0
    occuranceofOne  = 0
    for index, element in enumerate(xs):
        if int(element[i]) == 0:
            occuranceofZero += 1
        elif int(element[i]) == 1:
            occuranceofOne += 1

    if (occuranceofZero > occuranceofOne):
        return (0, 1)
    else: 
        return (1, 0)
   



# Main
# Power consumption of the submarine - Part 1
def powerConsumption(data):
    """
    Calculates the power consumption of the submarine.
    """
    mostCommon, leastCommon = list(), list()

    for index in range(12):
        most, least = determineMostandLeast(index, data)
        mostCommon.append(most)
        leastCommon.append(least)

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
        returns a list that contains only valid xs's (binaries) either that match most or least (depending on the match value). 
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
        i.e. a case where xs is of length 2 and both binary numbers match the val[index]
        """
        for index in range(12):
            most, least = determineMostandLeast(index, xs)
            if val == 'most':
                result = generateMatch(xs, index, most)
            else:
                result = generateMatch(xs, index, least)
            xs = result
            if len(xs) == 1:
                break
        return xs
    
    # Main
    oxyGenRatingBinary   = generateOxyAndCO2(data, 'most')
    scrubberRatingBinary = generateOxyAndCO2(data, 'least')

    oxyGenRating   = "".join(str(x) for x in oxyGenRatingBinary[0])   
    scrubberRating = "".join(str(x) for x in scrubberRatingBinary[0])

    return int(oxyGenRating, 2) * int(scrubberRating, 2)


lifeSR = lifeSupportRating(importData())
print(lifeSR)
