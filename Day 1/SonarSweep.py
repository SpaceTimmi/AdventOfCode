# Advent Of Code (2021)
# Day 1: Sonar Scan

def importData():
    scanData = open('puzzle.txt', 'r')
    return scanData


# Depth Measurement Increase - Part 1
def depthMeasurementIncrease(data):
    """given the puzzle data, this function will return the number of
     times the depth measurement increases for the sonar scan."""

    # Total is initialized as -1 because for the first measurement there is no previous measurement.
    # i.e total at first measurement = 0
    previousMeasure = 0
    total = -1

    for mesurement in data:
        newMeasure = int(mesurement)
        if newMeasure > previousMeasure:
            total += 1
        previousMeasure = newMeasure
    return total

depthIncrease = depthMeasurementIncrease(importData())
print(f"The number of measurements larger than the previous measurements is {depthIncrease}")


# Three Measurement Sliding Windows - Part 2
def threeMeasurementSlidingWindow(data):
    """given the puzzle data, this function will return the number of
    times the sum of three measurements in the slidng window increases."""
    
    count = 0
    newData = []
    for element in data:
        newElement = int(element)
        newData.append(newElement)
        count += 1

    # if the length of the data is N then there are (N - 2) possbile three measurement sliding windows.
    possibleWindows = count - 2
    previousMeasure = 0
    total = -1

    for index in range(possibleWindows):
        newMeasure = sum(newData[index:index+3])  
        if newMeasure > previousMeasure:
            total += 1
        previousMeasure = newMeasure
    return total

threeIncrease = threeMeasurementSlidingWindow(importData())
print(f"The number of sums larger than the previous sum is {threeIncrease}")
