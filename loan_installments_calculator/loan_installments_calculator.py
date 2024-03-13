from rich.table import Table
from rich import print

def takeUserDate(daysReversed, monthsReversed):
    userDate = str(input("Insert the date when your loan was taken (in dd-mm-yyyy format): "))
    userDay = userDate[:2]
    userMonth = userDate[3:5]
    userYear = userDate[6:]
    if userDay not in daysReversed or userMonth not in monthsReversed or int(userYear) <= 0:
        raise ValueError
    return userDay, userMonth, userYear

def takeLoanAmount():
    loanAmount = int(input("Insert amount of your loan (in PLN): "))
    if loanAmount < 1000:
        raise TypeError
    return loanAmount

def takeLoanCommission():
    loanCommission = int(input("Insert your bank's loan commission (in %): "))
    loanCommission = loanCommission/100
    if loanCommission <= 0:
        raise ValueError
    return loanCommission

def takeLoanInterestRate():
    loanInterestRate = int(input("Insert your loan's annual interest rate (in %): "))
    loanInterestRate = loanInterestRate/100
    if loanInterestRate <= 0:
        raise ValueError
    return loanInterestRate

def takePeriodOfPayment():
    periodOfPayment = int(input("Insert period of your loan's payment (in months): "))
    if periodOfPayment > 240 or periodOfPayment <= 0:
        raise TypeError
    return periodOfPayment

def calculateTotalLoan(loanAmount, loanCommission):
    totalLoanAmount = loanAmount + (loanAmount*loanCommission)
    return totalLoanAmount

def calculateInstallment(totalLoanAmount, loanInterestRate, periodOfPayment):
    installment = (totalLoanAmount*((loanInterestRate+1)**periodOfPayment)*loanInterestRate)/(((loanInterestRate+1)**periodOfPayment)-1)
    return installment

def calculateAverage(periodOfPayment, loanInterestRate, totalLoanAmount, wibor_rates, month):
    i = 1
    Installment = 0
    while i <= periodOfPayment:
        Installment = Installment + calculateInstallment(totalLoanAmount, (loanInterestRate+(wibor_rates[month]/100))/12, periodOfPayment)
        i=i+1
        if month == 12:
            month = 1
        else:
            month = month+1
    Installment = Installment/periodOfPayment
    return Installment

def createTable(periodOfPayment, days, months, day, month, year, installment):
    print("\n\n")
    paymentPlan = Table(title="Your loan's payment plan")
    paymentPlan.add_column("Date of the payment")
    paymentPlan.add_column("Installment (in PLN)")
    i = 1
    while i <= periodOfPayment:
        if day == 31 or day == 30:
            if month == 1:
                day = 28
            else:
                day = 30
        if month == 12:
            month = 1
            year = year+1
        else:
            month = month + 1
        paymentPlan.add_row("{}-{}-{}".format(days[day], months[month], year), str(round(installment, 2)))
        i=i+1
    print(paymentPlan)

def main():
    try:
        months = {1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "10", 11: "11", 12: "12"}
        monthsReversed = {v: k for k, v in months.items()}
        days = {1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "10", 11: "11", 12: "12", 13: "13", 14: "14", 15: "15", 16: "16", 17: "17", 18: "18", 19: "19", 20: "20", 21: "21", 22: "22", 23: "23", 24: "24", 25: "25", 26: "26", 27: "27", 28: "28", 29: "29", 30: "30", 31: "31"}
        daysReversed = {v: k for k, v in days.items()}
        wiborRates = {1: 7.00, 2: 7.00, 3: 6.95, 4: 6.95, 5: 6.95, 6: 6.95, 7: 6.70, 8: 6.55, 9: 5.65, 10: 5.60, 11: 5.80, 12: 5.65}
        userDay, userMonth, userYear = takeUserDate(daysReversed, monthsReversed)
        loanAmount = takeLoanAmount()
        loanCommission = takeLoanCommission()
        loanInterestRate = takeLoanInterestRate()
        periodOfPayment = takePeriodOfPayment()
        totalLoanAmount = calculateTotalLoan(loanAmount, loanCommission)
        installment = calculateAverage(periodOfPayment, loanInterestRate, totalLoanAmount, wiborRates, monthsReversed[userMonth])
        createTable(periodOfPayment, days, months, daysReversed[userDay], monthsReversed[userMonth], int(userYear), installment)
    except ValueError:
        print("Error: incorrect data in the input.")
    except TypeError:
        print("Error, amount of your loan can't be lower than 1000 PLN and period of your loan's payment can't be longer than 20 years or shorter than 0 months.")

if __name__ == "__main__":
    main()
