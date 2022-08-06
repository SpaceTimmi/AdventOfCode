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
    """
    Takes the importData() function as input and calculates the final score of the winning board.
    funct -> Natural 
    """
    # Helpers.
    def solved(lob):
        """
        Takes a list of  5x5 boards and returns true (and the corresponding board) if any row or column has been totally marked.
        Totally marked means all the cells in a row or column contains the value -1.
        listOf Boards -> Boolean, Board 
        """
        return

    def mark(lob, guess):
        """
        Takes a listOf Boards and a guess. It replaces all occurances of the guess in each board with the number -1.
        -1 is used to represt that a cell has been marked.
        listOf Boards, Natural -> listOf Boards.  
        """
        return 

    listOfGuesses, listOfBoards = data[0], data[1]
    
    for guess in listOfGuesses:
        listOfBoards = mark(listOfBoards, guess)
        winningBoard, finished = solved(listOfBoards)
        if finished is True:
            # sum all the unmarked numbers in winningBoard.
            #       drop all -1 from each row in the winningBoard
            #       sum up each row in the winningBoard individually
            #       combine the results of the sum for each row 
            # return the product of the (sum of unmarked numbers) and guess  
            pass
    return None # no guesses can solve the boards
