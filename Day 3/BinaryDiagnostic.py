# Advent of Code (2021)
# Day 3: Binary Diagnostic

def importData():
    scanData = open('input.txt', 'r')
    return scanData

# Power consumption of the submarine - Part 1
def powerConsumption(data):
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
    
    mostCommonBinary  = "".join(str(x) for x in mostCommon)
    leastCommonBinary = "".join(str(y) for y in leastCommon)
    
    gammaRate   = int(mostCommonBinary, 2) 
    epsilonRate = int(leastCommonBinary, 2)

    return gammaRate * epsilonRate


result = powerConsumption(importData())
print(result)
