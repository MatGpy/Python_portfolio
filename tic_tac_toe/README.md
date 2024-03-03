tic_tac_toe.py - documentation

This program is an implementation of tic tac toe game, where user is playing against program.

How does this program work?

Firstly, this program asks user which sign (x or o) they want to play as, define choosen sign as a user's sign and another sign as a program's sign. Then, as long as none of the sides wins and there still are free fields on the table, program repeatedly asks user about coordinates of table field where they want to put their sign and then, after user placed their sign on a choosen field, program chooses the place where it wants to put their sign. Game ends when user or program will put three of their signs on a table in a row or in a slant (then either user wins or program wins, if both user and program will manage to do that in the same turn, game will end with a draw), or if all the fields on the table will be occupied before user or program will win.

How to use this program?

If user uses linux device:

In order to use this program, user simply has to type 'python3 tic_tac_toe.py' into the terminal while being in directory where this program is located on user's device. After this step, user has to choose a sign they want to use during the game and then, with every turn, user has to choose coordinates of the table field where they want to put their sign.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| table | 3x3 table where user and program will put their signs during every turn |
| userSign | String, stores the sign choosen by the user (its value can be either "x" or "o") |
| programSignValues | Dictionary, it's used to define value of programSign based on the value of userSign |
| programSign | String, stores the sign that will be used by program during the game (if userSign = "x", it's equal to "o", if userSign = "o", it's equal to "x") |
| userMove | String, stores coordinates of the field where user wants to put their sign in certain turn, it's written in the following format - rc (r means number of the row, c means number of the column) |
| programMoveRow | Integer, defines number of the row of the table field where program will put its sign in a certain turn, its value is choosen randomly |
| programMoveColumn | Integer, defines number of the column of the table field where program will put its sign in a certain turn, its value is choosen randomly |
| userVictory | Integer, its value determines whether user managed to put three of their signs into a table in a row or in a slant (if its value is 1 - yes, otherwise - no) |
| programVictory | Integer, its value determines whether program managed to put three of its signs into a table in a row or in a slant (if its value is 1 - yes, otherwise - no) |
| occupatedFields | Integer, stores the amount of occupated fields on the table |

Description of all program's functions:

| function name | function description |
| ------------- | -------------------- |
| printTable | This function displays current state of the table, with every sign that is present on it at the moment |
| takeUserSign | This function takes the sign which user wants to use during the game |
| takeUserMove | This function takes coordinates of the field where user wants to place their sign during the certain turn |
| takeProgramMove | This function takes coordinates of the field where program wants to place its sign during the certain turn |
| checkVictory | This function checks if any of the players (user and/or program) managed to put three of their signs into the table in a row or in a slant and changes values of userVictory and programVictory depending on the result |