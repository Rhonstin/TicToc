import os
WON = 0
theBoard = {"7" : " ", "8": " ", "9": " ",
            "4" : " ", "5": " ", "6": " ",
            "1" : " ", "2": " ", "3": " "}
winCombination=[["1","2","3"],
                ["4","5","6"],
                ["7","8","9"],
                ["7","4","1"],
                ["1","5","9"],
                ["7","5","3"],
                ["2","5","8"],
                ["3","6","9"]]
def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
#Проверка на победные комбинации
def wintest(player,x):
    if theBoard[x[0]] == player and theBoard[x[1]] == player and theBoard[x[2]] == player:
        global WON
        WON += 1  
#Проверка на число
def testInt(localMove):
    try:
        val = int(localMove)
        return 1
    except ValueError:
        clearTheBoard()
        print("That not an int!")


#Функция для сокращения кода main
def shorts():
    inmpun = input()
    while testInt(inmpun) != 1:
        inmpun = input()
        testInt(inmpun)
    return inmpun

#Очищает всю поверхность коммандной строки.
def clearTheBoard():
        clear = lambda: os.system('cls')
        clear()
        printBoard(theBoard)

#Проверяет ход на правильность ввода числа.
def moveTest():
    move = shorts()
    if int(move) >= 10 or int(move) <= 0:
        clearTheBoard()
        print("Turn for " + turn + ".")
        print("Ячейка находится за границами поля.Выбери другое")
        move = moveTest()
    elif theBoard[move] != " ":
        clearTheBoard()
        print("Turn for " + turn + ".")
        print("Нельзя ходить на занятое место. Выбери другое")
        move = moveTest()
    return move

#Меняет ход игрока
def playerChange(player):
    if player == "x":
        player = "O"
    else:
        player = "x"
    return player

#Основная функция.
turn = "x"
printBoard(theBoard)
for i in range(9):
    print("Turn for " + turn + ".")
    move = moveTest()    
    theBoard[move] = turn
    i = 0
    for i in winCombination:
        wintest(turn,i)     
    if WON == 1:
        print("Победил игрок " + turn)
        break
    else:
        clearTheBoard()
    turn = playerChange(turn)
if WON != 1:
    print("Ничия!")

    
