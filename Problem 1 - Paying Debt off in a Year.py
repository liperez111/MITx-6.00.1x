#Problem 1 - Paying Debt off in a Year
'''Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

'''
def pay(n, b, r, m):

    while n >= 0:
        if n == 0:

            return b
        else:

            return round(pay(n - 1, b - (b + b * (r / 12)) * m + b * (r / 12), r, m), 2)

'''

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
n= 1

while n <= 12:
    if n == 1:

        bi = balance + (balance*(.2/12))
        bip = bi*monthlyPaymentRate
        balance = round(bi - bip,2)

        print("Month " + str(n) + " Remaining balance:" + str(balance))
        n+=1

    else:
        bi = balance + (balance * (.2 / 12))
        bip = bi * monthlyPaymentRate
        balance = round(bi - bip,2)

        print("Month " + str(n) +" Remaining balance:" + str(balance))
        n += 1




