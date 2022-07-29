# Advent Of Code (2021)
# Day 2: Dive

def importData():
    scanData = open('input.txt', 'r')
    return scanData

# Final Horizontal Position x Final Depth - Part 1
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
print(f"The result of multiplying the final horizontal position by the final depth for the input data is {result}")

## Part 2
def finalPosAndDepthWithAim(data):
    horizontalPosition = 0
    depth = 0
    aim = 0

    for command in data:
        newCommand = command.split()
        move = newCommand[0]
        change = newCommand[1]

        if move == "down":
            aim += int(change)
        elif move == "up":
            aim -= int(change)
        elif move == "forward":
            horizontalPosition += int(change)
            depth += (aim * int(change)) 
            pass

    return (horizontalPosition * depth)


result2 = finalPosAndDepthWithAim(importData())
print(f"The result of multiplying the final horizontal postion by the final depth for case 2 is {result2}")
