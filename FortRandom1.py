import random

def guess(x):
    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        print(guess)
        if guess < random_number:
            print('sorry too low try again')
        elif guess > random_number:
            print('sorry too high try again')

    print(f'WOW you guessed the number {random_number}correctly')


def Computer_guess(x):
    low = 1
    high= x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c high equals low 
        guess = random.randint(low, high)
        feedback = input(f'is {guess} too high(H), too low(L), or correct(C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! the computer guessed your number, {guess} correctly')
Computer_guess(10)    