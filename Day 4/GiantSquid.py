# Advent of code (2021)
# Day 4 - Giant Squid

def importData():
    """
    Parses the input data and returns two lists.
    The first list contains the guesses in sequential order
    The second list is a list of boards.
    list one -> list of numbers 
                [1,2,3, ....]
    list two -> list of boards, where board is a list of numbers. i.e.
                [[1, 2, 3...],
                [1, 2, 3...],
                [..........]] 
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
    for board in boards:
        newBoard = board.split(',')
        singleBoard = list()
        
        for line in newBoard:
            if line[0] != "\n":
                temp = line.split(" ")
                temp[-1] = temp[-1][:-1]
                temp = [int(elem) for elem in temp if elem]
                if len(temp) != 0:
                    singleBoard.append(temp)
            print(singleBoard) 
        listOfBoards.append(singleBoard)



        #newBoard[-1] = newBoard[-1][:-1]

        #if newBoard[0] != "":
            #newBoard = newBoard[0].split(" ")
            #newBoard = [int(elem) for elem in newBoard if elem]
            #listOfBoards.append(newBoard) 
    
    print(listOfBoards)


importData()
