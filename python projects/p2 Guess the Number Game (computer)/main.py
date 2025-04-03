#Import random to generate a random number, define guess(x) to set the range from 1 to x, generate a random number using random.randint(1, x), loop until correct guess, call guess(10) to start the game.
import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
             print("Sorry, guess again. Too high.")
        
    print("congrats, you have guessed the right number")
    
guess (10) 