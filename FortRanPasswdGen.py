import string
import random
Characters = list(string.ascii_letters + string.digits ) # variable created with a list assigned to it

# Generate password
def generate_password(): # function created
    password_length = int(input('How long would you like your password to be? ')) 

    random.shuffle(Characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(Characters))

    random.shuffle(password)   

    password = ''.join(password)
    print(password)

# User input 
Option = input('Do you want to Generate password? (Yes/No): ')

if Option == 'Yes':
    generate_password() # If yes, ask for password length # Print password
elif Option == 'No':
    print('Goodbye have a great day!')
    quit() # if intial response is no, exit program
else:
    print('Invalid input, Please input Yes or No')
    quit()        
  