EU_cities_quiz.py - documentation.

This program is a quiz game about cities situated in EU.

How does this program work?

Firstly, this program asks user for amount of questions they want the quiz to have. Then, for every question, program randomly chooses one of available countries, randomly picks three cities (including one that is situated in randomly chosen country), puts them into a list and shuffles their order within the list. Then, program displays names of all three cities (including one that is situated in previously chosen country, which is a correct answer) and asks user which one of them is situated in previously chosen country - if user's answer is correct, program increases amount of correct answers by 1, if not - program increases amount of wrong answers by 1. After the program asked user all the questions and gathered all their answers, program displays stats about the quiz - amount of correct answers, amount of wrong answers and accuracy (% of correct answers). If user chooses amount of questions lower than 1 or higher than 100, or user answer isn't a city name, program returns an error and stops working.

How to use this program?

In order to use this program, user simply has to type 'python3 EU_cities_quiz.py' into the terminal while being in directory where this program is located on user's device. Then, user simply has to insert amount of questions they want to answer and answer all of them (disclaimer: all cities' names should be written with first letter uppercase). Then, after user answered all the questions, quiz summary is displayed.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| amountOfQuestions | Integer, stores amount of questions user wants to answer |
| city1 | Integer, stores the value of key which corresponds to the name of first randomly choosen city |
| city2 | Integer, stores the value of key which corresponds to the name of second randomly choosen city |
| city3 | Integer, stores the value of key which corresponds to the name of third randomly choosen city |
| cityNames | List, stores names of all three randomly chosen cities |
| answer | String, stores user's answer for the question asked by the program |
| correctAnswers | Integer, stores amount of user's correct answers during the quiz |
| wrongAnswers | Integer, stores amount of user's wrong answers during the quiz |
| questionNumber | Integer, stores the number of question program asks user at the moment |
| citiesLocations | Dictionary, stores city names (key) and names of countries where these cities are situated (value) |
| citiesNums | Dictionary, stores city names (value) and numbers corresponding to every one of these cities (key) |
| countryNums | Dictionary, stores country names (value) and numbers corresponding to every one of these countries (key) |
| country | Integer, stores the number corresponding to randomly chosen country where the correct answer city is situated |

Description of all program's functions:

| function name | function description |
| ------------- | -------------------- |
| takeAmountOfQuestions | This function takes amount of questions user want to answer in the quiz. If user chooses negative amount of questions or amount of questions greater than 100, program raises an error. |
| takeThreeCities | This function randomly chooses three cities (one of them is the city which will be the correct answer) and puts them into the cityNames list. |
| shuffleCities | This function takes cityNames list and shuffles the order among the cities inside of it |
| printQuestion | This function outputs the question with all three possible answers below it (one of them is correct, two of them are false) |
| takeAnswer | This function takes answer for given question from the user |
| checkAnswer | This function checks whether user's answer is correct or not and either increases amount of corect user's answers or wrong user's answers depending on it |
| printSummary | This function outputs summary of the quiz after all the questions are answered, amount of correct answers, wrong answers and % of correct answers |