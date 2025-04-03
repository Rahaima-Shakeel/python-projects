#Import `random`, define `computer_guess(x)`, set range, adjust based on feedback, loop until correct guess, and call `computer_guess(10)`.
import random 

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"IS {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
            
    print ("Yay! The computer guessed the correct number.")
    
computer_guess (10)