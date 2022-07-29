# Advent Of Code (2021)
# Day 2: Dive

def importData():
    scanData = open('input.txt', 'r')
    return scanData

# Final Horizontal Position x Final Depth
def finalPositionAndDepth(data):
    horizontalPosition = 0
    depth = 0

    for command in data:
        newCommand = command.split()
        move = newCommand[0]
        change = newCommand[1]

        if move == "forward":
            horizontalPosition += int(change)
        elif move == "down":
            depth += int(change)
        elif move == "up":
            depth -= int(change) 

    return (horizontalPosition * depth)

result = finalPositionAndDepth(importData())
print(result)
