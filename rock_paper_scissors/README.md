**rock_paper_scissors.py - documentation.**

This program is an implementation of rock paper scissors game.

**How does this program work?**

Firstly, user has to choose their move (rock, paper or scissors). Then, program takes userprogram won's move, chooses randomly its move and compares both moves to determine which side won. After these steps, program displays user's move, program's move and result of the game (user won/program won/neither one of the players won).

**How to use this program?**

If user uses Linux device:

In order to use this program, user has to open terminal, change directory to the location where this program is saved on user's device and type 'python3 rock_paper_scissors.py'. Then, user has to insert their move (rock, paper or scissors) into the specified field. After these steps, results of rock paper scissors game between user and the program will be displayed.

If user uses Windows device:

In order to use this program, user has to open rock_paper_scissors.py file with Python IDE of their choice (for example Visual Studio Code) and run it (for example, you can run the file in Visual Studio Code by pressing a triangle on the top right side of the window). Then, user has to insert their move (rock, paper or scissors) into the specified field. After these steps, results of rock paper scissors game between user and the program will be displayed. 

Alternatively, user can run this file using Windows Powershell - then, process of running the program is similar to running the program on linux device: user has to change directory to the location where this program is saved on their device and type 'python3 rock_paper_scissors.py' into the terminal. After these steps, user can use this program.

**Description of all program's variables:**

| variable name | variable description |
| ------------- | -------------------- |
| playerMove | String, stores user's move in rock papaer scissors game. |
| programMoveNum | Integer, its value is randomly chosen between 1, 2 and 3, its value defines program's move in rock paper scissors game. |
| programMoves | Dictionary, its values are possible moves program can make in rock paper scissors game and keys are programMoveNum values which cause program to make a certain move. |

**Description of all program's functions:**

| function name | function description |
| ------------- | -------------------- |
| takePlayerMove | This function takes user's move in rock paper scissors game and returns the error if user chose an invalid move. |
| takeProgramMove | This function defines program's move in rock paper scissors game based on the value of programMoveNum. |
| compareMoves | This function compares user's move with program's move and returns the outcome of this comparison (user's victory, program's victory or draw). |