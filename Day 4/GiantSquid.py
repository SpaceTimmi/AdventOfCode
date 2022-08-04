# Advent of code (2021)
# Day 4 - Giant Squid

def importData():
    """
    Parses the input.txt data and returns two lists.
    The first list contains the guesses in sequential order
    The second list is a list of boards.
    list one -> listOf numbers 
                [1,2,3, ....]
    list two -> listOf boards, where board is a listOf listOf numbers (3D list). i.e.
                board         -> [[1, 2, 3...],
                                  [1, 2, 3...],
                                  [..........]]
                listOf boards -> [board1, board2, ...]  
    """
    scanData = open('input.txt', 'r')
    dataList = list()

    for data in scanData:
        dataList.append(data)


    # ========= Parsing out and inputting all guesses into a single list ===============
    guesses = dataList[0]
    listOfGuesses = guesses.split(",")
    listOfGuesses[-1] = listOfGuesses[-1][:2] # Removing the '\n' char at the end.
    listOfGuesses = [int(elem) for elem in listOfGuesses]
    
    # ========= Parsing each board out of the data and inputting into a single list =========
    boards = dataList[1::]
    listOfBoards = list()
    singleBoard = list()
    for board in boards:
        newBoard = board.split(',')
        
        for line in newBoard:
            if line[0] != "\n":
                temp = line.split(" ")
                temp[-1] = temp[-1][:-1]
                temp = [int(elem) for elem in temp if elem]
                singleBoard.append(temp)
            else:
                listOfBoards.append(singleBoard)
                singleBoard = list()
    listOfBoards = listOfBoards[1::]
        
    
    return (listOfGuesses, listOfBoards)

# Final score - Part 1
# What will the final score be if I choose a board?
def finalScore(data):
    pass
