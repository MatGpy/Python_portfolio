import secrets

def takeAmountOfCharacters():
   amountOfCharacters = int(input("How many characters do you want your password to have? (type a positive number): "))
   if amountOfCharacters <= 0 or amountOfCharacters > 100:
      raise ValueError
   return amountOfCharacters

def generateChar():
   charNumber = int()
   while charNumber < 33 or charNumber > 57 and charNumber < 65 or charNumber > 90 and charNumber < 97:
      charNumber = secrets.randbelow(123)
   return chr(charNumber)

def main():
   try:
      amountOfCharacters = takeAmountOfCharacters()
      passwordChars = [generateChar() for i in range (0,amountOfCharacters)]
      print("\nHere's your password: {}".format("".join(passwordChars)))
   except ValueError:
      print("\nError: user chose invalid lenght of the password")

if __name__ == "__main__":
   main()	
