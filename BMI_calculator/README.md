BMI_calculator.py - documentation

This program is an implementation of a simple BMI calculator.

How does this program work?

This program asks user to insert their height (in centimeters) and weight (in kilograms), then it calculates BMI based on provided data, displays it to user and informs them whether their weight is too low, within the norm or too high, based on their BMI.

How to use this program?

If user uses linux device:

In order to use this program, user simply has to type 'python3 BMI_calculator.py' into the terminal while being in directory where this program is located on user's device and then insert all the necessary data. After all these steps, program will display user's BMI.

Description of all program's variables:

| variable name | variable description |
| ------------- | -------------------- |
| weight | Float number, stores user's weight in kilograms |
| height | Float number, stores user's height in centimeters |
| bmi | Float number, stores value of user's BMI calculated from the formula - weight (in kilograms) / height (in meters) ^ 2 |
| messages | Dictionary, stores all messages that program displays based on user's bmi (as items) and BMI value ranges for which various messages are relevant (as keys) |
| bmiRange | Tuple, which first element means lower limit of BMI value for which certain message is valid and second element means upper limit of BMI value for which certain message is valid |
| outputMessage | String, stores the message program chose based on previously calculated value of user's BMI |

Description of all program's functions

| function name | function description |
| ------------- | -------------------- |
| takeInputWeight | This function takes user's weight in kilograms and checks if it's not lower than 0 or higher than 1000 and raises error if it is |
| takeInputHeight | This function takes user's height in centimeters and checks if it's not lower than 0 or higher than 1000 and raises error if it is |
| calculateBMI | This function calculates user's BMI based on their weight and height. If BMI < 0 or BMI > 1000, function raises error |
| createOutputMessage | This function chooses message about user's weight to display based on the value of user's BMI |