X_O_game.py - documentation.

This program is an implementation of a certain game, where user has to replace all the cells of 9x9 table with 'X' signs. User can do this by choosing the table cell they want to replace - then, not only user's chosen cell will be replaced, but also 4 cells which are congruent to user's chosen cell (if cell's initial value is 'O' sign, its value will be replaced with 'X' sign, if cell's initial value is 'X' sign, its value will be replaced with 'O' sign).

How does this program work?

Firstly, this program displays initial state of the table (where all cells' values are 'O' signs), then asks user about coordinates of the cell where they want to place their first 'X' (including 4 cells that are congruent to this cell) and replaces values of all these cells with 'X' sign. Program will repeatedly ask user about the cells which value they want to replace (including 4 cells that are congruent to this cell) and replace values of these cells ('O' with 'X' and 'X' with 'O') until all table cells' values will be 'X' signs - if user will manage to do that, program will display information about user's victory and amount of rounds it took user to get the table to this state.

How to use this program?

If user uses linux device:

In order to use this program, user simply has to type 'python3 X_O_game.py' into the terminal while being in directory where this program is located on user's device. Then, user has to repeatedly insert coordinates of the cell which value they want to replace (together with 4 cells congruent to that cell) every turn, until they'll manage to replace all table cells' values with 'X' signs.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| table | It's a table which stores all 'X's and 'O's. In order to win, all values of its cells must be 'X' signs |
| row | Integer, it's used to iterate through all the table rows |
| column | Integer, it's used to iterate through all the table columns |
| amountOfX | Integer, stores the amount of 'X's on the table in a certain round |
| comparisonOutcomes | Dictionary, its keys are ranges of possible amounts of 'X' table cells and its values are strings saying if amounts of 'X' cells from a certain range result in victory (0-80: no, 81 and more: yes) |
| amountRange | Tuples which are keys in comparisonOutcomes dictionary |
| outcome | Strings which are values in comparisonOutcomes dictionary |
| userMove | String, it's a double digit number which stores coordinates of the cell which valuie user wants to replace (first digit means number of the row, second digit means number of the column) |
| XaxisPlacement | Integer, it's used during value replacement of the value in cells congruent to user's cell, it determines column difference compared to user's cell (congruent cell can be either in the same column, previous column or next column) |
| YaxisPlacement | Integer, it's used during value replacement of the value in cells congruent to user's cell, it determines row difference compared to user's cell (congruent cell can be either in the same row, previous row or next row) |
| tableValues | Dictionary, it's used during replacement of the value in a table cell |
| victory | String, its value determines if user has already won the game and there will be no next rounds (victory = "yes") or if user hasn't won the game yet and there will be next rounds, during which program will ask user for next cells they want to replace (victory = "no") |
| turn | Integer, it stores the number of current round and total number of rounds if user won the game |

Description of all program's functions:

| function name | function description |
| ------------- | -------------------- |
| printTable | This function displays the table with all 'X's and 'O's |
| checkIfVictory | This function counts 'X's on the table and uses amount of 'X's on the table to determine whether user already won the game or not |
| takeUserMove | This function takes coordinates of the table cell which value user wants to replace (in form of double digit number where first digit means number of row and second digit means number of column) |
| modifyTable | This function replaces the value of the table cell which either has been chosen by the user (then XaxisPlacement = 1 and YaxisPlacement = 1, because computers count from 0 and user counts from 1) or is congruent to user's chosen table cell (then values of XaxisPlacement and YaxisPlacement will vary, based on if their numbers of rows and columns are equal to user's chosen cell, higher or lower) |