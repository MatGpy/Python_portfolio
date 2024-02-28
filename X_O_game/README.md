X_O_game.py - documentation.

This program is an implementation of a certain game, where user has to replace all the cells of 9x9 table with 'X' signs. User can do this by choosing the table cell they want to replace - then, not only user's chosen cell will be replaced, but also 4 cells which are congruent to user's chosen cell (if cell's initial value is 'O' sign, its value will be replaced with 'X' sign, if cell's initial value is 'X' sign, its value will be replaced with 'O' sign).

How does this program work?

Firstly, this program displays initial state of the table (where all cells' values are 'O' signs), then asks user about coordinates of the cell where they want to place their first 'X' (including 4 cells that are congruent to this cell) and replaces values of all these cells with 'X' sign. Program will repeatedly ask user about the cells which value they want to replace (including 4 cells that are congruent to this cell) and replace values of these cells ('O' with 'X' and 'X' with 'O') until all table cells' values will be 'X' signs - if user will manage to do that, program will display information about user's victory and amount of rounds it took user to get the table to this state.

How to use this program?

In order to use this program, user simply has to type 'python3 X_O_game.py' into the terminal while being in directory where this program is located on user's device. Then, user has to repeatedly insert coordinates of the cell which value they want to replace (together with 4 cells congruent to that cell) every turn, until they'll manage to replace all table cells' values with 'X' signs.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| table | it's a table which stores all 'X's and 'O's. In order to win, all values of its cells must be 'X' signs |
| row | integer, it's used to iterate through all the table rows |
| column | integer, it's used to iterate through all the table columns |
| amountOfX | integer, stores the amount of 'X's on the table in a certain round |
| comparisonOutcomes | dictionary, 