import random
def takePlayerMove():
    playerMove = str(input("Your turn (you can choose rock, paper, or scissors): "))
    if playerMove not in ("rock", "paper", "scissors"):
        raise ValueError
    return playerMove
    
def takeProgramMove():
    programMoveNum = random.randint(1,3)
    programMoves = {1: "rock", 2: "paper", 3: "scissors"}
    programMove = programMoves[programMoveNum]
    return programMove

def compareMoves(programMove, playerMove):
    if programMove == "rock" and playerMove == "scissors" or programMove == "paper" and playerMove == "rock" or programMove == "scissors" and playerMove == "paper":
        return "program won"
    elif programMove == "rock" and playerMove == "paper" or programMove == "paper" and playerMove == "scissors" or programMove == "scissors" and playerMove == "rock":
        return "you won"
    elif programMove == "rock" and playerMove == "rock" or programMove == "paper" and playerMove == "paper" or programMove == "scissors" and playerMove == "scissors":
        return "draw"
    else:
        return "something went wrong"

def main():
    try:
        playerMove = takePlayerMove()
        programMove = takeProgramMove()
        print("\nYour move: {}\nProgram's move: {}\nGame result: {}".format(playerMove, programMove, compareMoves(programMove, playerMove)))
    except ValueError:
        print("Error: user chose invalid move")

if __name__ == "__main__":
    main()