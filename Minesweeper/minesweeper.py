import random

def populateTableWithMines(table,mines):
    while mines > 0:
        b1 = random.randint(0,9)
        b2 = random.randint(0,9)
        while not table[b1][b2] == ' ':
            b1 = random.randint(0,9)
            b2 = random.randint(0,9)
        table[b1][b2] = 'X'
        mines = mines-1

def populateTableWith1(table,points1):
    while points1 > 0:
        b1 = random.randint(0,9)
        b2 = random.randint(0,9)
        while not table[b1][b2] == ' ':
            b1 = random.randint(0,9)
            b2 = random.randint(0,9)
        table[b1][b2] = '1'
        points1 = points1-1

def populateTableWith2(table,points2):
    while points2 > 0:
        b1 = random.randint(0,9)
        b2 = random.randint(0,9)
        while not table[b1][b2] == ' ':
            b1 = random.randint(0,9)
            b2 = random.randint(0,9)
        table[b1][b2] = '2'
        points2 = points2-1

def populateTableWith3(table,points3):
    while points3 > 0:
        b1 = random.randint(0,9)
        b2 = random.randint(0,9)
        while not table[b1][b2] == ' ':
            b1 = random.randint(0,9)
            b2 = random.randint(0,9)
        table[b1][b2] = '3'
        points3 = points3-1

def printTable(displayedTable):
    column = 0
    row = 0
    print(" |0|1|2|3|4|5|6|7|8|9|")
    while column <= 9:
        print("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(row,displayedTable[column][0],displayedTable[column][1],displayedTable[column][2],displayedTable[column][3],displayedTable[column][4],displayedTable[column][5],displayedTable[column][6],displayedTable[column][7],displayedTable[column][8],displayedTable[column][9]))
        column = column+1
        row = row+1

def takeDifficultyLevel():
    difficultyLevel = str(input("Choose level of difficulty (easy, medium, hard or very hard): "))
    if difficultyLevel not in ("easy", "medium", "hard", "very hard"):
        raise TypeError
    return difficultyLevel

def takeAttempt(displayedTable):
    attempt = str(input("Which field do you want to uncover? (type the answer in the following order - rc (r - row, c - column)) "))
    if len(attempt) > 2 or attempt == "":
        raise ValueError
    while not displayedTable[int(attempt[0])][int(attempt[1])] == 'O':
        print("chosen field is already uncovered")
        attempt = str(input("Which field do you want to uncover? (type the answer in the following order - rc (r - row, c - column)) "))
        if len(attempt) > 2 or attempt == "":
            raise ValueError
    return attempt

def main():
    try:
        displayedTable = [
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O'],
        ['O', 'O', 'O','O', 'O', 'O','O', 'O', 'O','O']
        ]
        mainTable = [
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' '],
        [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
        ]
        difficultyLevelMines = {"easy": 25, "medium": 35, "hard": 45, "very hard": 55}
        difficultyLevelPoint1 = {"easy": 36, "medium": 32, "hard": 27, "very hard": 22}
        difficultyLevelPoint2 = {"easy": 23, "medium": 20, "hard": 16, "very hard": 14}
        difficultyLevelPoint3 = {"easy": 16, "medium": 13, "hard": 12, "very hard": 9}
        difficultyLevel = takeDifficultyLevel()
        mines = difficultyLevelMines[difficultyLevel]
        points1 = difficultyLevelPoint1[difficultyLevel]
        points2 = difficultyLevelPoint2[difficultyLevel]
        points3 = difficultyLevelPoint3[difficultyLevel]
        populateTableWithMines(mainTable,mines)
        populateTableWith1(mainTable,points1)
        populateTableWith2(mainTable,points2)
        populateTableWith3(mainTable,points3)
        uncoveredMines = 0
        uncoveredCells = 0
        points = 0
        printTable(displayedTable)
        while uncoveredCells < 100-mines:
            attempt = takeAttempt(displayedTable)
            displayedTable[int(attempt[0])][int(attempt[1])] = mainTable[int(attempt[0])][int(attempt[1])]
            printTable(displayedTable)
            match mainTable[int(attempt[0])][int(attempt[1])]:
                case '1':
                    uncoveredCells = uncoveredCells+1
                    print("+1 point")
                    points = points+1
                case '2':
                    uncoveredCells = uncoveredCells+1
                    print("+2 points")
                    points = points+2
                case '3':
                    uncoveredCells = uncoveredCells+1
                    print("+3 points")
                    points = points+3
                case 'X':
                    uncoveredCells = uncoveredCells+1
                    print("Game over\nTotal scored points: {}".format(points))
                    uncoveredMines = 1
                    break
                case _:
                    print("something went wrong")
                    break
        if uncoveredMines == 0:
            print("Victory\nTotal scored points: {}".format(points))
    except TypeError:
        print("Error: user chose invalid level of difficulty")
    except ValueError:
        print("Error: user chose invalid table cell to uncover")

if __name__ == "__main__":
    main()	