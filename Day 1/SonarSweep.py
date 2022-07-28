# Advent Of Code (2021)
# Day 1: Sonar Scan

scanData = open('puzzle.txt', 'r')

previousMeasurement = 0 
for mesurement in scanData:
    newMeasure = int(mesurement)  