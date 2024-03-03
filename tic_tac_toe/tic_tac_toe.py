import random

def printTable(table):
    print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(table[0][0],table[0][1],table[0][2],table[1][0],table[1][1],table[1][2],table[2][0],table[2][1],table[2][2]))
    
def takeUserSign():
    userSign = str(input("choose sign you want to use (x or o): "))
    programSignValues = {"x": "o", "o": "x"}
    programSign = programSignValues[userSign]
    return userSign, programSign

def takeUserMove(table):
    userMove = str(input("your turn - insert coordinates of the field where you want to put your number (in a following order - rc, where r means number of row and c means number of column): "))
    while not table[int(userMove[0])-1][int(userMove[1])-1] == ' ':
        print("player chose field that's already occupated")
        userMove = str(input("your turn - insert coordinates of the field where you want to put your number (in a following order - rc, where r means number of row and c means number of column): "))
    if len(userMove) > 2:
        raise ValueError
    return userMove

def takeProgramMove(table):
    programMoveRow = random.randint(1,3)
    programMoveColumn = random.randint(1,3)
    while table[programMoveRow-1][programMoveColumn-1] == "x" or table[programMoveRow-1][programMoveColumn-1] == "o":
        programMoveRow = random.randint(1,3)
        programMoveColumn = random.randint(1,3)
    return programMoveRow, programMoveColumn

def checkVictory(table, userSign, programSign, userVictory, programVictory):
    if table[0][0] == table[0][1] == table[0][2] == userSign or table[1][0] == table[1][1] == table[1][2] == userSign or table[2][0] == table[2][1] == table[2][2] == userSign or table[0][0] == table[1][1] == table[2][2] == userSign or table[0][2] == table[1][1] == table[2][0] == userSign or table[0][0] == table[1][0] == table[2][0] == userSign or table[0][1] == table[1][1] == table[2][1] == userSign or table[0][2] == table[1][2] == table[2][2] == userSign:
        userVictory = 1
    if table[0][0] == table[0][1] == table[0][2] == programSign or table[1][0] == table[1][1] == table[1][2] == programSign or table[2][0] == table[2][1] == table[2][2] == programSign or table[0][0] == table[1][1] == table[2][2] == programSign or table[0][2] == table[1][1] == table[2][0] == programSign or table[0][0] == table[1][0] == table[2][0] == programSign or table[0][1] == table[1][1] == table[2][1] == programSign or table[0][2] == table[1][2] == table[2][2] == programSign:
        programVictory = 1
    return userVictory, programVictory
    
def main():
    try:
        table = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
        ]
        occupatedFields = 0
        userVictory = 0
        programVictory = 0
        userSign, programSign = takeUserSign()
        while userVictory+programVictory == 0:
            userMove = takeUserMove(table)
            table[int(userMove[0])-1][int(userMove[1])-1] = userSign
            printTable(table)
            occupatedFields = occupatedFields+1
            if occupatedFields == 9:
                print("the end")
                break
            programMoveRow, programMoveColumn = takeProgramMove(table)
            table[programMoveRow-1][programMoveColumn-1] = programSign
            print("program's move:")
            printTable(table)
            occupatedFields = occupatedFields+1
            userVictory, programVictory = checkVictory(table, userSign, programSign, userVictory, programVictory)
            if userVictory+programVictory == 1:
                if userVictory == 1:
                    print("you win")
                    break
                elif programVictory == 1:
                    print("program wins")
                    break
                else:
                    print("something went wrong")
                    break
            if userVictory+programVictory == 2:
                print("draw")
                break
            if occupatedFields >= 9 and userVictory+programVictory == 0:
                print("the end")
                break
    except (ValueError, IndexError):
        print("Error: user chose invalid coordinates of table field")
    except KeyError:
        print("Error: user chose invalid sign")

if __name__ == "__main__":
    main()	