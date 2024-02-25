import random
def compareGuess(guess, guessedNumber):
    if guess == guessedNumber:
        return "Correct answer"
    else:
        if guess < guessedNumber:
            return "Your guess is too low"
        if guess > guessedNumber:
            return "Your guess is too high"

def takeDifficultyLevel():
    difficultyLevel = str(input("levels of difficulty:\nvery easy - 8 attempts\neasy - 6 attempts\nnormal - 4 attempts\nhard - 2 attempts\n\nChoose level of difficulty: "))
    if difficultyLevel not in ("very easy", "easy", "normal", "hard"):
        raise TypeError()
    return difficultyLevel

def defineAmountOfAttempts(difficultyLevel, difficultyLevelAttempts):
    amountOfAttempts = difficultyLevelAttempts[difficultyLevel]
    return amountOfAttempts

def askAboutHint():
    hint = str(input("Do you want to get a hint (type 'yes' if you want a hint and 'no' if you don't)? "))
    if hint not in ("yes", "no"):
        raise TypeError()
    return hint

def displayHint(hint, guessedNumber, hintNumber, hintNumber2):
    if hint == "yes":
        if hintNumber == 1:
            if guessedNumber % 2 == 0:
                print("this number is even")
            else:
                print("this number is odd")
        if hintNumber == 2:
            if guessedNumber < hintNumber2:
                print("this number is lower than {}".format(hintNumber2))
            else:
                print("this number is higher or equal to {}".format(hintNumber2))
        if hintNumber == 3:
            if guessedNumber**2 < 10:
                print("this number squared is lower than 10")
            else:
                print("this number squared is higher or equal to 10")

def takeGuess(attemptNumber):
    guess = int(input("Attempt number {}\nInsert your guess: ".format(attemptNumber)))
    if guess < 1 or guess > 10:
        raise ValueError()
    return guess

def main():
    try:
        print("Try to guess a randomly generated number between 1 and 10")
        guessedNumber = random.randint(1,10)
        hintNumber = random.randint(1,3)
        hintNumber2 = random.randint(1,10)
        difficultyLevelAttempts = {"very easy":8, "easy":6, "normal":4, "hard":2}
        difficultyLevel = takeDifficultyLevel()
        amountOfAttempts = defineAmountOfAttempts(difficultyLevel, difficultyLevelAttempts)
        hint = askAboutHint()
        displayHint(hint, guessedNumber, hintNumber, hintNumber2)
        attemptNumber = 1
        while attemptNumber <= amountOfAttempts:
            guess = takeGuess(attemptNumber)
            print(compareGuess(guess, guessedNumber))
            if attemptNumber == amountOfAttempts:
                print("You ran out of attempts. Correct answer is {}".format(guessedNumber))
            attemptNumber = attemptNumber+1
            if guess == guessedNumber:
                break
    except TypeError:
        print("Error: user chose invalid difficulty level or response whether they want a hint")
    except ValueError:
        print("Error: user inserted invalid type of guess (every guess must be an integer between 1 and 10)")

if __name__ == "__main__":
    main()	