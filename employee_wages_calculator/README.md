**Employee_wages_calculator.py - documentation.**

Thsi program's purpose is calculating wages for all employees based on the data about these employees stored in a csv file.

**How does this program work?**

Firstly, this program takes name and location of the csv file where data about employees are present. Then, program counts amount of the employees whose data are present in provided csv file, creates two tables - inputFileTable and wagesTable (first one will be used to store all contents from user's csv file, second one will only store employees' names, surnames and wages), copies all data from user's input file into inputFileTable and populates wagesTable with employees' names, surnames and their wages calculated based on the data from inputFileTable. After filling wagesTable with all the necessary data, program creates OutputFile.csv in the directory where this program is stored on user's device, writes all the information from wagesTable into this file and once it's done, program informs the user about successful creation of OutputFile.csv, where employees' calculated wages, together with their names and surnames, are stored. Disclaimer - For optimal experience with this program, it's recommended to use csv files where all the data about employees are stored in single table no matter their form of employment and cells that don't apply to certain employee are described as 'nie dotyczy' (InputFile.csv is a good example how optimal csv file should look like).

**How to use this program?**

If user uses linux device:

In order to use this program, user has to open terminal, change directory to the location where this program is saved on user's device and type 'python3 employee_wages_calculator.py'. Then, user has to insert name and location of the csv file with employees' data on their device and after it's done, program will create OutputFile.csv in the directory where this program is saved on user's device and inform user about it.

If user uses windows device:

In order to use this program, user has to open employee_wages_calculator.py file with Python IDE of their choice (for example Visual Studio Code) and run it (for example, you can run the file in Visual Studio Code by pressing a triangle on the top right side of the window). Then, user has to insert the location and name of their input csv file.

Alternatively, user can run this file using windows powershell - then, process of running the program is similar to running the program on linux device: user has to change directory to the location where this program is saved on their device and type 'python3 employee_wages_calculator.py' into the terminal. After these steps, user can use this program.

**Description of all program's variables:**

| variable name | variable description |
| ------------- | -------------------- |
| employeesCount | Integer, stores the amount of employees, whose data are present in user's csv file. |
| wagesTable | Table, stores employees' names, surnames and calculated wages, which will be put into the output csv file later. |
| inputFileTable | Table, stores all employees' data from user's file. |
| contractType | String, stores information about every employee's type of contract, which is used during calculating employees' wages. |
| name | String, stores contents of first row of user's file (employee's name). |
| surname | String, stores contents of second row of user's file (employee's surname). |
| baseWage | String, stores contents of fourth row of user's file (base wage, doesn't apply to employees whose contractType = "umowa zlecenie" or "umowa o dzielo"). |
| overtimeHours | String, stores contents of sixth row of user's file (amount of overtime hours, doesn't apply to employees whose contractType = "umowa zlecenie" or "umowa o dzielo"). |
| overtimeHourlyWage | String, stores contents of fifth row of user's file (hourly wage for every overtime hour, doesn't apply to employees whose contractType = "umowa zlecenie" or "umowa o dzielo"). |
| hourlyWage | String, stores contents of seventh row of user's file (hourly wage, doesn't apply to employees whose contractType = "umowa o prace" or "umowa o dzielo"). |
| amountOfHours | String, stores contents of eighth row of user's file (amount of hours worked, doesn't apply to employees whose contractType = "umowa o prace" or "umowa o dzielo"). |
| workWage | String, stores contents of ninth row of user's file (wage for performed work, doesn't apply to employees whose contractType = "umowa o prace" or "umowa zlecenie"). |
| workStatus | String, stores contents of tenth row of user's file (information wherher employee performed the work specified in the contract, doesn't apply to employees whose contractType = "umowa o prace" or "umowa zlecenie"). |
| wage | Integer, stores amount of every employee's wage. |
| inputFileLocation | String, stores location of user's csv file with data about employees. |
| i,j | Integers, used to iterate through files and wagesTable. |

**Description of all program's objects:**

| object name | object description | 
| ----------- | ------------------ |
| inputFile | References csv file from user's input with all data about employees. |
| outputFile | References output csv file, where data about employees' wages will be written. |
| reader | object which is used to iterate through all lines in user's file and read their contents. |
| writer | object which is used to write employees' names, surnames and wages into the output file. |

**Description of all program's functions:**

| function name | function description |
| ------------- | -------------------- |
| createWagesTable | function which is used to generate table, where employees' names, surnames and wages will be stored. |
| calculateWage | function which is used to calculate employees' wages based on data from user's csv file. |
| populateWagesTable | function which is used to populate wagesTable with employees' names, surnames and wages. |
| createInputFileTable | function which is used to create inputFileTable. |
| takeInputLocation | function which is used to take location and name of user's csv file. |
| readInputFile | function which is used to read contents from user's csv file and put them into inputFileTable. |
| writeOutputFile | function which is used to write data from wagesTable to OutputFile.csv . |