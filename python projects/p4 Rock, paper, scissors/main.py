
#defines play() to get input, selects a random choice, checks the result using is_win(), and prints the outcome.
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])
    
    print(f"Computer chose: {computer}")
    
    if user  == computer:
        return 'It\'s a Tie'
    
    if is_win(user, computer):
        return 'You Won!'
    return  'You Lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print (play())