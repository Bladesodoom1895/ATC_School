#program demonstrates bank account class

#PPr10-8

#import the bankaccount module
import bankaccount

def main():
    #get the starting balance.
    start_bal = float(input('Enter you starting balance: '))

    #create bankaccount object
    savings = bankaccount.BankAccount(start_bal)

    #deposit users paycheck
    pay = float(input('How much were you paid? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    #display the balance
    print('Your account balance is $',
    format(savings.get_balance(), ',.2f'),
        sep='')

    #get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    #display the balance
    print('Your account balance is $',
    format(savings.get_balance(), ',.2f'),
        sep='')

#call main function
main()