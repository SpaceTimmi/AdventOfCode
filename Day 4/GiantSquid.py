# Advent of code (2021)
# Day 4 - Giant Squid

def importData():
    """
    Parses the input data into two lists.
    The first list contains the guesses in sequential order 
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
    
    # ========= Parsing each board (list of numbers) and inputting all boards into a single list =========
    boards = dataList[1::]
    listOfBoards = list()
    for board in boards:
        newBoard = board.split(',')
        #newBoard[-1] = newBoard[-1][:-1]

        if newBoard[0] != "":
            #newBoard = newBoard[0].split(" ")
            #newBoard = [int(elem) for elem in newBoard if elem]
            listOfBoards.append(newBoard) 
    
    print(listOfBoards)


importData()
