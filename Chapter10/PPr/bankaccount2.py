#bank account class simulates a bank account

#PPr10-9.py

class BankAccount:

    #__init__ method accepts argument
    #for accounts balance, assigns to
    #__balance attribute

    def __init__(self, bal):
        self.__balance = bal

    #depost method makes a deposit into
    #the account

    def deposit(self, amount):
        self.__balance += amount
    
    #withdraw method withdraws an amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds.')
        
    #get_balance method returns the account balance

    def get_balance(self):
        return self.__balance
    
    #the __str__ method returns a string
    #indicating the object's state

    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')