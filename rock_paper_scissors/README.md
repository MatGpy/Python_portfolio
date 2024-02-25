rock_paper_scissors.py - documentation

This program is an implementation of rock paper scissors game.

How does this program work?

Firstly, user has to choose their move (rock, paper or scissors). Then, program takes userprogram won's move, chooses randomly its move and compares both moves to determine which side won. After these steps, program displays user's move, program's move and result of the game (user won/program won/neither one of the players won).

How to use this program?

In order to use this program, user simply has to type 'python3 rock_paper_scissors.py' into the terminal while being in directory where this program is located on user's device. Then, user has to insert their move (rock, paper or scissors) into the specified field. After these steps, results of rock paper scissors game between user and the program will be displayed.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| playerMove | String, stores user's move in rock papaer scissors game |
| programMoveNum | Integer, its value is randomly chosen between 1, 2 and 3, its value defines program's move in rock paper scissors game |
| programMoves | Dictionary, its values are possible moves program can make in rock paper scissors game and keys are programMoveNum values which cause program to make a certain move |

Description of all program's functions:

| function name | function description |
| ------------- | -------------------- |
| takePlayerMove | This function takes user's move in rock paper scissors game and returns the error if user chose an invalid move |
| takeProgramMove | This function defines program's move in rock paper scissors game based on the value of programMoveNum |
| compareMoves | This function compares user's move with program's move and returns the outcome of this comparison (user's victory, program's victory or draw) |