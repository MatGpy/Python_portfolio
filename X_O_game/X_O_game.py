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
                amountOfX = amountOfX = 1
    for amountRange, outcome in comparisonOutcomes.items():
        if amountRange[0] <= amountOfX <= amountRange[1]:
            return outcome
    
def takeUserMove():
    userMove = str(input("Insert coordinates of the cell on the table where you would like to place X? (insert them in following format - rc (r - number of the row, c - number of the column)): "))
    if int(userMove[0]) and int(userMove[1]) not in (1,2,3,4,5,6,7,8,9) or len(userMove) > 2:
        raise ValueError
    return userMove

def main():
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
    while victory == "no":
        userMove = takeUserMove()
        table[int(userMove[0])-1][int(userMove[1])-1] = tableValues[table[int(userMove[0])-1][int(userMove[1])-1]]
        table[int(userMove[0])-2][int(userMove[1])-1] = tableValues[table[int(userMove[0])-2][int(userMove[1])-1]]
        table[int(userMove[0])-1][int(userMove[1])] = tableValues[table[int(userMove[0])-1][int(userMove[1])]]
        table[int(userMove[0])][int(userMove[1])-1] = tableValues[table[int(userMove[0])][int(userMove[1])-1]]
        table[int(userMove[0])-1][int(userMove[1])-2] = tableValues[table[int(userMove[0])-1][int(userMove[1])-2]]
        printTable(table)
        victory = checkIfVictory(table)
    print("victory")

if __name__ == "__main__":
    main()	
