minesweeper.py - documentation

This program is an implementation of a minesweeper game.

How does this program work?

Firstly, this program creates two tables - mainTable and displayedTable (mainTable is the table where contents of all the cells are stored - mines and point prizes, while displayedTable is the table that is visible for the user - only contents of uncovered cells are visible and all cells aside from uncovered ones are covered). Then, program creates 4 dictionaries, which store information about amount of mines (cells with mines inside are marked as 'X') and certain point prizes (+1/+2/+3 points, cells with point prizes are marked as '1'/'2'/'3') which will be put into cells of mainTable based on level of difficulty chosen by the user. Then, program asks user about level of difficulty they want to play with and randomly populates the table with amount of mines and certain point prizes accordingly to chosen level of difficulty. After the table has been populated, the game begins - program repeatedly displays user the displayTable, asks them to uncover one cell of their choice and, based on contents of uncovered cell, either increases amount of points gained by the user (if chosen cell contains a point prize) or stops the game with user's defeat (if chosen cell contains a mine). If user manages to uncover all mainTable cells with point prize without uncovering any of the cell with a mine, user wins and program stops the game. 

How to use this program?

In order to use this program, user simply has to type 'python3 minesweeper.py' into the terminal while being in directory where this program is located on user's device. Then, user has to specify the level of difficulty they want to play with and then the game begins - program will repeatedly show user current state of the table and ask user about table cell they want to uncover until user's victory or defeat.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| mines | Integer, stores amount of mines that will be present on the table |
| points1 | Integer, stores amount of cells with +1 point prize that will be present on the table |
| points2 | Integer, stores amount of cells with +2 points prize that will be present on the table |
| points3 | Integer, stores amount of cells with +3 points prize that will be present on the table |
| displayedTable | Table, it's shown to the user with every turn of the game, every cell that hasn't been uncovered by the user has value of 'O' |
| column | Integer, it's used to iterate through all the columns of displayedTable every time it's displayed to the user |
| row | Integer, it's used to iterate through all the rows of displayedTable every time it's displayed to the user |
| difficultyLevel | String, stores the name of level of difficulty chosen by the user |
| attempt | String, stores coordinates of table cell user wants to uncover during a certain turn (its first character means number of row of uncovered cell and its second character means number of column of uncovered cell) |
| mainTable | Table, it's filled with mines and point prizes before game starts, it's not shown to the user |
| difficultyLevelMines | Dictionary, stores amount of mines that will be put into mainTable based on level of difficulty chosen by the user |
| difficultyLevelPoint1 | Dictionary, stores amount of +1 point prizes that will be put into mainTable based on level of difficulty chosen by the user |
| difficultyLevelPoint2 | Dictionary, stores amount of +2 point prizes that will be put into mainTable based on level of difficulty chosen by the user |
| difficultyLevelPoint3 | Dictionary, stores amount of +3 point prizes that will be put into mainTable based on level of difficulty chosen by the user |
| uncoveredMines | Integer, stores amount of mines uncovered by the user. If it's larger than 0, game ends with user's defeat |
| uncoveredCells | Integer, stores amount of table cells uncovered by the user |
| points | Integer, stores amount of points gained by the user |

Description of all program's functions:

| function name | function description |
| ------------- | -------------------- |
| populateTableWithMines | This function randomly puts mines into mainTable. Amount of mines put into mainTable depends on level of difficulty chosen by the user |
| populateTableWith1 | This function randomly puts +1 point prizes into mainTable. Amount of +1 point prizes put into mainTable depends on level of difficulty chosen by the user |
| populateTableWith2 | This function randomly puts +2 points prizes into mainTable. Amount of +2 points prizes put into mainTable depends on level of difficulty chosen by the user |
| populateTableWith3 | This function randomly puts +3 points prizes into mainTable. Amount of +3 points prizes put into mainTable depends on level of difficulty chosen by the user |
| printTable | This function is used to print displayTable every time it's necessary |
| takeDifficultyLevel | This function asks user about difficulty level they want to choose and takes the name of difficulty level chosen by the user |
| takeAttempt | This function asks user about coordinates of displayedTable cell they want to uncover and takes these coordinates from the user |

