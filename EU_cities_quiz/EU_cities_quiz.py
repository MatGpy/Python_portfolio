import random

def takeAmountOfQuestions():
    amountOfQuestions = int(input("How many questions do you want this quiz to have (type a number)? "))
    if amountOfQuestions < 1 or amountOfQuestions > 100:
        raise TypeError
    return amountOfQuestions

def takeThreeCities(citiesNums, citiesLocations, countryNums, country):
    city1 = 1
    city2 = 1
    city3 = 1 
    while city1 == city2 or city1 == city3 or city2 == city1 or city2 == city3 or city3 == city1 or city3 == city2 and citiesLocations[citiesNums[city1]] != countryNums[country] or citiesLocations[citiesNums[city2]] != countryNums[country] or citiesLocations[citiesNums[city3]] != countryNums[country] and citiesLocations[citiesNums[city1]] == citiesLocations[citiesNums[city2]] or citiesLocations[citiesNums[city1]] == citiesLocations[citiesNums[city3]] or citiesLocations[citiesNums[city2]] == citiesLocations[citiesNums[city1]] or citiesLocations[citiesNums[city2]] == citiesLocations[citiesNums[city3]] or citiesLocations[citiesNums[city3]] == citiesLocations[citiesNums[city1]] or citiesLocations[citiesNums[city3]] == citiesLocations[citiesNums[city2]]:
        city1 = random.randint(1, 81)
        city2 = random.randint(1, 81)
        city3 = random.randint(1, 81)
    cityNames = [citiesNums[city1], citiesNums[city2], citiesNums[city3]]
    return cityNames

def shuffleCities(cityNames):
    cityNames = random.shuffle(cityNames)

def printQuestion(questionNumber, country, countryNums, cityNames):
    print("\nQuestion #{}:\nWhich one of these cities is situated in {}?\na) {}\nb) {}\nc) {}".format(questionNumber, countryNums[country], cityNames[0], cityNames[1], cityNames[2]))

def takeAnswer():
    answer = str(input("Write the answer here (name of the city): "))
    return answer

def checkAnswer(answer, country, citiesLocations, countryNums, correctAnswers, wrongAnswers):
    if citiesLocations[answer] == countryNums[country]:
        print("Correct answer")
        correctAnswers = correctAnswers+1
    else:
        print("Wrong answer")
        wrongAnswers = wrongAnswers+1
    return correctAnswers, wrongAnswers

def printSummary(correctAnswers, wrongAnswers, amountOfQuestions):
    print("\nSummary of the quiz:\nCorrect answers: {}/{}\nWrong answers: {}/{}\nAccuracy: {}%".format(correctAnswers,amountOfQuestions,wrongAnswers,amountOfQuestions,correctAnswers/amountOfQuestions*100))

def main():
    try:
        questionNumber = 1
        correctAnswers = 0
        wrongAnswers = 0
        citiesLocations = {"Berlin": "Germany", "Munich": "Germany", "Hanover": "Germany", "Paris": "France", "Lyon": "France", "Toulouse": "France", "Madrid": "Spain", "Barcelona": "Spain", "Seville": "Spain", "Milan": "Italy", "Rome": "Italy", "Naples": "Italy", "Lisbon": "Portugal", "Porto": "Portugal", "Coimbra": "Portugal", "Dublin": "Ireland", "Cork": "Ireland", "Galway": "Ireland", "Brussels": "Belgium", "Antwerp": "Belgium", "Charleroi": "Belgium", "Amsterdam": "Netherlands", "Rotterdam": "Netherlands", "Utrecht": "Netherlands", "Vienna": "Austria", "Linz": "Austria", "Innsbruck": "Austria", "Athens": "Greece", "Thessaloniki": "Greece", "Patras": "Greece", "Copenhagen": "Denmark", "Billund": "Denmark", "Aarhus": "Denmark", "Malmo": "Sweden", "Stockholm": "Sweden", "Gothenburg": "Sweden", "Helsinki": "Finland", "Turku": "Finland", "Oulu": "Finland", "Nicosia": "Cyprus", "Girne": "Cyprus", "Limassol": "Cyprus", "Valletta": "Malta", "Mdina": "Malta", "Birgu": "Malta", "Luxembourg": "Luxembourg", "Ettelbruck": "Luxembourg", "Steinfort": "Luxembourg", "Tallinn": "Estonia", "Tartu": "Estonia", "Keila": "Estonia", "Riga": "Latvia", "Ogre": "Latvia", "Ludza": "Latvia", "Vilnus": "Lithuania", "Kaunas": "Lithuania", "Klaipeda": "Lithuania", "Warsaw": "Poland", "Krakow": "Poland", "Gdansk": "Poland", "Prague": "Czechia", "Brno": "Czechia", "Ostrava": "Czechia", "Bratislava": "Slovakia", "Kosice": "Slovakia", "Trencin": "Slovakia", "Budapest": "Hungary", "Debrecen": "Hungary", "Miskolc": "Hungary", "Ljubljana": "Slovenia", "Maribor": "Slovenia", "Celje": "Slovenia", "Zagreb": "Croatia", "Rijeka": "Croatia", "Split": "Croatia", "Bucharest": "Romania", "Cluj-Napoka": "Romania", "Timisoara": "Romania", "Sofia": "Bulgaria", "Varna": "Bulgaria", "Plovdiv": "Bulgaria"}
        citiesNums = {1: "Berlin", 2: "Munich", 3: "Hanover", 4: "Paris", 5: "Lyon", 6: "Toulouse", 7: "Madrid", 8: "Barcelona", 9: "Seville", 10: "Milan", 11: "Rome", 12: "Naples", 13: "Lisbon", 14: "Porto", 15: "Coimbra", 16: "Dublin", 17: "Cork", 18: "Galway", 19: "Brussels", 20: "Antwerp", 21: "Charleroi", 22: "Amsterdam", 23: "Rotterdam", 24: "Utrecht", 25: "Vienna", 26: "Linz", 27: "Innsbruck", 28: "Athens", 29: "Thessaloniki", 30: "Patras", 31: "Copenhagen", 32: "Billund", 33: "Aarhus", 34: "Malmo", 35: "Stockholm", 36: "Gothenburg", 37: "Helsinki", 38: "Turku", 39: "Oulu", 40: "Nicosia", 41: "Girne", 42: "Limassol", 43: "Valletta", 44: "Mdina", 45: "Birgu", 46: "Luxembourg", 47: "Ettelbruck", 48: "Steinfort", 49: "Tallinn", 50: "Tartu", 51: "Keila", 52: "Riga", 53: "Ogre", 54: "Ludza", 55: "Vilnus", 56: "Kaunas", 57: "Klaipeda", 58: "Warsaw", 59: "Krakow", 60: "Gdansk", 61: "Prague", 62: "Brno", 63: "Ostrava", 64: "Bratislava", 65: "Kosice", 66: "Trencin", 67: "Budapest", 68: "Debrecen", 69: "Miskolc", 70: "Ljubljana", 71: "Maribor", 72: "Celje", 73: "Zagreb", 74: "Rijeka", 75: "Split", 76: "Bucharest", 77: "Cluj-Napoka", 78: "Timisoara", 79: "Sofia", 80: "Varna", 81: "Plovdiv"}
        countryNums = {1: "Germany", 2: "France", 3: "Spain", 4: "Italy", 5: "Portugal", 6: "Ireland", 7: "Belgium", 8: "Netherlands", 9: "Austria", 10: "Greece", 11: "Denmark", 12: "Sweden", 13: "Finland", 14: "Cyprus", 15: "Malta", 16: "Luxembourg", 17: "Estonia", 18: "Latvia", 19: "Lithuania", 20: "Poland", 21: "Czechia", 22: "Slovakia", 23: "Hungary", 24: "Slovenia", 25: "Croatia", 26: "Romania", 27: "Bulgaria"}
        amountOfQuestions = takeAmountOfQuestions()
        while questionNumber <= amountOfQuestions:
            country = random.randint(1, 27)
            cityNames = takeThreeCities(citiesNums, citiesLocations, countryNums, country)
            shuffleCities(cityNames)
            printQuestion(questionNumber, country, countryNums, cityNames)
            answer = takeAnswer()
            correctAnswers, wrongAnswers = checkAnswer(answer, country, citiesLocations, countryNums, correctAnswers, wrongAnswers)
            questionNumber = questionNumber+1
        printSummary(correctAnswers, wrongAnswers, amountOfQuestions)
    except KeyError:
        print("Error: invalid city name (remember that city names should start with uppercase letter)")
    except ValueError:
        print("Error: amount of questions must be a positive number, larger than 0")
    except TypeError:
        print("Error: Invalid amount of questions")

if __name__ == "__main__":
    main()	