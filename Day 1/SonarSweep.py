# Advent Of Code (2021)
# Day 1: Sonar Scan

scanData = open('puzzle.txt', 'r')

# Total is initialized as -1 because for the first measurement there is no previous measurement.
# i.e total at first measurement = 0
previousMeasure = 0
total = -1

for mesurement in scanData:
    newMeasure = int(mesurement)
    if newMeasure > previousMeasure:
        total += 1
    previousMeasure = newMeasure

print(total)
