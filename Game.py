# Guess the number game

import random
print("Hello. what's your name?")
name = input()
print("Hi " + str(name) + " , I was thinking of a number between 1 and 20")
secretNumber = random.randint(1,20)



for GuessesTaken in range(1,7):  #Loop
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your number is too low")
    elif guess > secretNumber:
        print("Your number is too high")
    else:
        break

if secretNumber == guess:
    print("Correct guess! You've guessed the number in " + str(GuessesTaken) + " guesses")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
