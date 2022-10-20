# collect the necessary inputs: principal, apr, years
def main():
    print('This is a monthly payment loan calculator')
    print('')

while True:
    principal = float(input('Input the loan amount: '))
    apr = float(input('Input the annual interest rate: '))
    years = int(input('Input amount of years: '))

# calculate the monthly payment

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payments = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (- amount_of_months))

# show to the user
    print('The monthly payment for this loan is: ₦%.2f ' % monthly_payments)
    print('')
    print('')

main()
