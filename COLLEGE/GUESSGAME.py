import random as rd
PLAYER = input("ENTER PLAYER NAME:").upper()
print(f"\nWELCOME,{PLAYER} TO THE GUESSING GAME IN THIS GAME YOU "
      f"\nHAVE TO GUESS THE RANDOM NUMBER SELECTED BY ME. YOU HAVE 10 ATTEMPTS TO GUESS THE GAME "
      f"\nTHE RANDOM NUMBER IS BETWEEN 1 TO 1000. AFTER 10 ATTEMPTS YOU WILL AUTOMATICALLY "
      f"\nGET CHECKED OUT OF THE GAME RESULTING YOU INTO A LOOSE. I HOPE I AM CLEAR HENCE "
      f"\nLET'S START THE GAME.\n")
jackpot = rd.randint(1, 1000)
guess = int(input("GUESS THE NUMBER:"))
count = 0
while count < 10:
    if guess > jackpot:
        print(f"\nGUESS A LOWER NUMBER.\n")
        count = count + 1
        guess = int(input("TRY GUESSING AGAIN:"))
    elif guess < jackpot:
        print(f"\nGUESS A HIGHER NUMBER.\n")
        count = count + 1
        guess = int(input("TRY GUESSING AGAIN:"))
    else:
        count = count + 1
        print(f"\nYOU GUESSED IT RIGHT {PLAYER}."
              f"\nRIGHT ANSWER IS {jackpot}."
              f"\n{PLAYER}, YOU TOOK {count} TURNS TO GUESS THE NUMBER RIGHT. ")
        quit()
print(f"\n{PLAYER}, YOU ARE UNABLE TO GUESS THE NUMBER RIGHT WITHIN THE GIVEN GUESS LIMIT."
      f"\nYOU TOOK MORE THAN 10 ATTEMPTS TO GUESS THE NUMBER."
      f"\nTHE CORRECT ANSWER WAS {jackpot}"
      f"\nYOU LOST.")
