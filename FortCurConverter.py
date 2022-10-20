from email.errors import NonASCIILocalPartDefect


def main():
    print('This program converts Naira to Dollars')
    print()

    Naira = eval(input('Enter amount in ₦(Naira): '))

    Dollar = convert_to_dollars(Naira)

    print('Thats is', Dollar, 'Dollar.')

convert_to_dollars = lambda Naira: Naira / 670

main()

    