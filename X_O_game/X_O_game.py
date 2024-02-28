def printTable(table):
    print(" |1|2|3|4|5|6|7|8|9|")
    for row in range(9):
        print("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(row+1, table[row][0],table[row][1],table[row][2],table[row][3],table[row][4],table[row][5],table[row][6],table[row][7],table[row][8],))

def checkIfVictory(table):
    amountOfX = 0
    comparisonOutcomes = {(0,80): "no", (81,82): "yes"}
    for row in range(9):
        for column in range(9):
            if table[row][column] == 'X':
                amountOfX = amountOfX + 1
    for amountRange, outcome in comparisonOutcomes.items():
        if amountRange[0] <= amountOfX <= amountRange[1]:
            return outcome
    
def takeUserMove():
    userMove = str(input("Insert coordinates of the cell on the table where you would like to place 'X' (in a form of double digit number, where first digit is an number of row and second number is a number of column): "))
    if int(userMove[0]) and int(userMove[1]) not in (1,2,3,4,5,6,7,8,9) or len(userMove) > 2:
        raise ValueError
    return userMove

def modifyTable(table, userMove, XaxisPlacement, YaxisPlacement, tableValues):
    if int(userMove[0])-YaxisPlacement < 0 or int(userMove[1])-XaxisPlacement < 0:
        return 
    try:
        table[int(userMove[0])-YaxisPlacement][int(userMove[1])-XaxisPlacement] = tableValues[table[int(userMove[0])-YaxisPlacement][int(userMove[1])-XaxisPlacement]]
    except IndexError:
        return

def main():
    try:
        table = [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ]
        tableValues = {'X': 'O', 'O': 'X'}
        victory = "no"
        turn = 0
        while victory == "no":
            turn = turn+1
            printTable(table)
            userMove = takeUserMove()
            modifyTable(table, userMove, 1, 1, tableValues)
            modifyTable(table, userMove, 2, 1, tableValues)
            modifyTable(table, userMove, 1, 0, tableValues)
            modifyTable(table, userMove, 0, 1, tableValues)
            modifyTable(table, userMove, 1, 2, tableValues)
            victory = checkIfVictory(table)
        print("You won!\nYou managed to set all the table cells as 'X' in {} rounds".format(turn))
    except ValueError:
        print("Error: invalid data in the input")

if __name__ == "__main__":
    main()	
