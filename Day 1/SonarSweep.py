# Advent Of Code (2021)
# Day 1: Sonar Scan


scanData = open('puzzle.txt', 'r')


# Depth Measurement Increase - Part 1
def depthMeasurementIncrease(data):
    """given the puzzle data, this function will return the number of
     times the depth measurement increases for the sonar scan"""

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

total = depthMeasurementIncrease(scanData)
print(total)


# Three Measurement Sliding Window - Part 2
def threeMeasurementSlidingWindow(data):
    """given the puzzle data, this function will return the number of
     times the sum of three measurements in the slidng window increases"""
    pass
