number_guessing_game.py - documentation

This program is an implementation of the game where user has to guess number from 1 to 10.

How does this program work?

Firstly, program randomly chooses the value of three integers - guessedNumber (number which user has to guess), hintNumber and hintNumber2 (both numbers will be used to generate a hint for the user). Then, program takes difficulty level with which user wants to play the game, chooses amount of available attempts for the user based on chosen level of difficulty, gives user a hint about the number they have to guess (if user specified they want a hint). After all these steps, program repeatedly asks user for their guess about the number, compares it with the value of guessed number and informs the user if their guess is correct, too high or too low. If user manages to guess value of guessed number before they run out of available attempts, the game ends with user's victory, but if user doesn't manage to do so, the game ends with user's defeat and program reveals the true value of guessed number.

How to use this program?

If user uses linux device:

In order to use this program, user simply has to type 'python3 number_guessing_game.py' into the terminal while being in directory where this program is located on user's device. Then, user has to choose level of difficulty and inform the program whether they want a hint. After these steps, user has specified amount of attempts to guess value of the guessed number.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| guess | Integer, stores value of guessed number proposed by the user in a certain attempt |
| guessedNumber | Integer, stores real value of guessed number, which user has to guess in certain amount of attempts |
| difficultyLevel | String, stores name of difficulty level chosen by the user |
| amountOfAttempts | Integer, stores amount of attempts available for the user, its value is dependent on difficulty level chosen by the user |
| hint | String, stores user's answer whether they want a hint about guessed number or not (its value can be either "yes" or "no") |
| hintNumber | Integer, it's used to choose a type of hint program will give to the user |
| hintNumber2 | Integer, it's used to generate a hint for the user, which informs user if guessed number is higher or lower than hintNumber2 |
| attemptNumber | Integer, it's used to inform about the number of certain attempt and iterate through all user's available attempts |
| difficultyLevelAttempts | Dictionary, stores information about amount of attempts available in every difficulty level |

Description of all program's functions:

| function name | function description |
| ------------- | -------------------- |
| compareGuess | This function compares user's guess with real value of guessed number and returns the information whether user's guess is too high, too low or equal to real value of guessed number |
| takeDifficultyLevel | This function asks user about difficulty level they want to play with and takes its value from the user |
| defineAmountOfAttempts | This function defines amount of attempts available for the user based on chosen difficulty level |
| askAboutHint | This function asks user whether they want a hint about guessed number |
| displayHint | This function displays a hint about guessed number to the user (if they specified that they want a hint earlier) |
| takeGuess | This function takes user's guess about the value of guessed number in a certain attempt |