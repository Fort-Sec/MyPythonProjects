#define the functions; add, sub, mutiplication, division
def add(a, b):
    answer = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer) + '\n')

def sub(a, b):
    answer = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer) + '\n')

def multiplication(a, b):
    answer = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(answer) + '\n')

def division(a, b):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer) + '\n')


#print options to the user ie what the user want to do

while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('Input your choice: ')
#ask for values / call the function     
    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        add(a, b)

    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        sub(a, b) 

    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        multiplication(a, b)

    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Input first number: '))
        b = int(input('Input second number: '))
        division(a, b)

    elif choice == 'e' or choice == 'E':
        print('END')
        quit()
#while loop to continue the program untill the user want to exit
