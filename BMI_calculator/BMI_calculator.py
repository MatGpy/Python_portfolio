def takeInputWeight():
    weight = float(input("Insert your weight in kilograms: ")) 
    if weight < 0 or weight > 1000:
        raise ValueError
    return weight

def takeInputHeight():
    height = float(input("Insert your height in centimeters: "))
    if height < 0 or height > 1000:
        raise ValueError
    height = height/100
    return height

def calculateBMI(weight, height):
    bmi = round((weight/(height**2)), 2)
    if bmi < 0 or bmi > 1000:
        raise ValueError
    return bmi

def createOutputMessage(bmi):
    messages = {(0,18): "too low", (18,24): "perfect", (24,29): "a bit too high", (29,35): "too high", (35,1000): "way too high"}
    for bmiRange, outputMessage in messages.items():
        if bmiRange[0] <= bmi <= bmiRange[1]:
            return outputMessage

def main():
    try:
        height = takeInputHeight()
        weight = takeInputWeight()
        bmi = calculateBMI(weight, height)
        outputMessage = createOutputMessage(bmi)
        print("Your BMI = {}\nYour weight is {}.".format(bmi, outputMessage))
    except ValueError:
        print("Error: something went wrong")
    
if __name__ == "__main__":
    main()	