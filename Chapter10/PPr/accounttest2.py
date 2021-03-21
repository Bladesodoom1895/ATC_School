#program demonstrates bank account class
#with __str__ method

#PPr10-10

#import the bankaccount module
import bankaccount2

def main():
    #get the starting balance.
    start_bal = float(input('Enter you starting balance: '))

    #create bankaccount object
    savings = bankaccount2.BankAccount(start_bal)

    #deposit users paycheck
    pay = float(input('How much were you paid? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    #display the balance
    print(savings)

    #get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    #display the balance
    print(savings)

#call main function
main()