import csv

def countEmployees(inputFile):
    employeesCount = (sum(1 for line in inputFile)-1)
    inputFile.seek(0)
    return employeesCount

def createWagesTable(employeesCount):
    wagesTable = [[0 for x in range(employeesCount)] for y in range(3)] 
    return wagesTable

def createInputFileTable(employeesCount):
    inputFileTable = [[0 for x in range(employeesCount)] for y in range(10)]
    return inputFileTable

def calculateWage(contractType, baseWage, overtimeHourlyWage, overtimeHours, hourlyWage, amountOfHours, workWage, workStatus, wage):
    if contractType == "umowa o prace":
        wage = (int(baseWage) + (int(overtimeHourlyWage) * int(overtimeHours)))
    elif contractType == "umowa zlecenie":
        wage = (int(hourlyWage)*int(amountOfHours))
    elif contractType == "umowa o dzielo":
        if workStatus == "tak":
            wage = int(workWage)
        else:
            wage = 0
    return wage
    
def takeInputLocation():
    inputFileLocation = str(input("Insert location of the file where employees' data are stored: "))
    return inputFileLocation

def readInputFile(reader, inputFileTable, inputFile):
    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            for j in range(10):
                inputFileTable[j][i-1] = row[j]
    inputFile.seek(0)
    return inputFileTable

def populateWagesTable(inputFileTable, wagesTable, wage, i):
    contractType = inputFileTable[2][i]
    baseWage = inputFileTable[3][i]
    overtimeHourlyWage = inputFileTable[4][i]
    overtimeHours = inputFileTable[5][i]
    hourlyWage = inputFileTable[6][i]
    amountOfHours = inputFileTable[7][i]
    workWage = inputFileTable[8][i]
    workStatus = inputFileTable[9][i]
    name = inputFileTable[0][i]
    surname = inputFileTable[1][i]
    wage = calculateWage(contractType, baseWage, overtimeHourlyWage, overtimeHours, hourlyWage, amountOfHours, workWage, workStatus, wage)
    wagesTable[0][i] = name
    wagesTable[1][i] = surname
    wagesTable[2][i] = str(wage)

def writeOutputFile(writer, wagesTable, employeesCount):
    writer.writerow(["Imie", "Nazwisko", "Finalna wyplata"])
    for i in range(employeesCount):
        writer.writerow([str(wagesTable[0][i]), str(wagesTable[1][i]), str(wagesTable[2][i])])

def main():
    try:
        inputFileLocation = takeInputLocation()
        with open(inputFileLocation, 'r', newline='') as inputFile:
            employeesCount = countEmployees(inputFile)
            reader = csv.reader(inputFile, delimiter=',')
            wage = 0
            wagesTable = createWagesTable(employeesCount)
            inputFileTable = createInputFileTable(employeesCount)
            readInputFile(reader, inputFileTable, inputFile)
            for i, row in enumerate(reader):
                populateWagesTable(inputFileTable, wagesTable, wage, i-1)
        with open('./OutputFile.csv', 'w', newline='') as outputFile:
            writer = csv.writer(outputFile, delimiter=',')
            writeOutputFile(writer, wagesTable, employeesCount)
    except (FileNotFoundError, IsADirectoryError):
        print("Error: file provided by the user or file location provided by the user is invalid")
    else:
        print("Output file (OutputFile.csv) has been successfully created")

if __name__ == "__main__":
    main()
