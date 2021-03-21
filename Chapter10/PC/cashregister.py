#cash register class file

import retail

class CashRegister:
    def __init__(self):
        #initialize the class with an empty
        #list to add items to each time a user
        #purchases an item
        self.__item_list = []
    
    def purchase_item(self, item):
        #add items the user purchases to the list
        self.__item_list.append(item)

    def get_total(self):
        #total cost accumulator
        total_cost = 0

        #total cost of internal list
        for item in __item_list:
            #get the items cost from retail and
            #add it to the accumulator
            total_cost += retail.item.__price
        
        return total_cost

    def show_items(self):
        #show all items in the list each time a
        #user adds an item and 
        return self.__item_list

    def clear(self):
        #clear the items in the list
        self.__item_list.clear()


def main():
    #create an instance of the object
    cash_register = CashRegister()

    #variable to control the loop
    choice = 0

    while choice < 0 and choice > 5:
        print('#' * 10)
        print('# Cash Register #')
        print('# 1: Purchase Item #')
        print('# 2: Show Items # ')
        print('# 3: Clear Items #')
        print('# 4: Checkout #')
        print('# 5: Quit #')
        print('#' * 10)

        choice = input('Enter your choice: ')

        if choice == '1':
            print(retail.item_list)
        elif choice == '2':
            print(cash_register.show_items)
        elif choice == '3':
            cash_register.clear()
        elif choice == '4':
            print(cash_register.get_total())
    #this will be used to display options to the
    #user get the option they want to do, like purchase
    #an item, clear their list of items, or finish their
    #transaction
main()