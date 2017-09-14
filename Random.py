import random
print("Hello, what's your name?")
name = input()

print("Hi " + name + " , I was thinking of a number between 1 & 20")
secretNumber = random.randint(1,20)

#Loop
for guesses in range(1,7):
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("You guessed too low")
    elif guess > secretNumber:
        print("You guessed too high")
    else:
        break
if guess == secretNumber:
    print("Good job! You guessed the correct one in " + str(guesses) + " guesses.")
else:
    print("Nope. I was thinking of the number " + str(secretNumber))
