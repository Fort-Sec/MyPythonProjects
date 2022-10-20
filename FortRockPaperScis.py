import random

def play():
    user = input("Whats your choice? 'R' for Rock,'P' for Paper,'S' for scissors\n")
    Computer = random.choice(['R','P','S'])
    if user == Computer:
        return 'It\s a tie'


        # R > S, S > P, P > R
    if Is_win(user,Computer):
        return ' You won!'
    return ' You lost!'

def Is_win(Player,Opponent):
    #return true if player wins 

    if (Player == 'R' and Opponent == 'S') or (Player == 'S' and Opponent == 'P')\
        or (Player == 'P' and Opponent == 'R'):
        return True

print(play())