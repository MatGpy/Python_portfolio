**Password_generator.py - documentation.**

This program's purpose is generating a password which length is specified by the user.

**How does this program work?**

Firstly, this program takes amount of characters which generated password should have from the user. Then, program randomly generates and converts into signs according to ascii code as many numbers as user specified, packs all these signs into the list, connects all these signs into a single string and outputs this string as a password.

**How to use this program?**

If user uses linux device:

In order to use this program, user has to open terminal, change directory to the location where this program is saved on user's device and type 'python3 Password_generator.py'. Then, user has to insert amount of characters which generated password should have and then program will display generated password.

If user uses windows device:

In order to use this program, user has to open Password_generator.py file with Python IDE of their choice (for example Visual Studio Code) and run it (for example, you can run the file in Visual Studio Code by pressing a triangle on the top right side of the window). Then, user has to insert amount of characters which generated password should have and then program will display generated password.

Alternatively, user can run this file using windows powershell - then, process of running the program is similar to running the program on linux device: user has to change directory to the location where this program is saved on their device and type 'python3 Password_generator.py' into the terminal. After these steps, user can use this program.

**Description of all program's variables:**

| variable name | variable description |
| ------------- | -------------------- |
| amountOfCharacters | Integer, stores amount of characters which generated password should have. Its value is determined by the user. |
| charNumber | Integer, its value is randomly generated and then it's converted into a sign using ascii code. |
| passwordChars | List, stores all the signs converted from previously generated numbers. Its characters will be connected into a single string, which will represent the password. |

**Description of all program's functions:**

| function name | function description |
| ------------- | -------------------- |
| takeAmountOfCharacters | This function takes amount of characters generated password should be made of from the user. |
| generateChar | This function randomly generates a number, which is then converted into a sign according to ascii code. |
