#cash register class file

import retail

class CashRegister:
    def __init__(self):
        #initialize the class with an empty
        #list to add items to each time a user
        #purchases an item
        self.__item_list = []

    def purchase_item(self, item):
        #add the item to the list
        self.__item_list.append(item)

    def show_items(self):
        return self.__item_list

    def get_total(self):
        #accumulator for cost
        total = 0

        #get a total price for all items in the list
        for item in self.__item_list:
            total += item.get_total()

        return total

    def clear(self):
    #clear the list
        self.__item_list.clear()


def main():
    #create an instance of the object
    cash_register = CashRegister()

    #variable to control the loop
    choice = '0'
    i = 0
    found = False

    while choice != '4':
        print('#' * 20)
        print('# Cash Register #')
        print('#' * 20)
        print('# 1: Purchase Item #')
        print('# 2: Clear Items #')
        print('# 3: Checkout #')
        print('# 4: Quit #')
        print('#' * 20)

        choice = input('Enter your choice: ')

        if choice == '1':
            print('Here is a list of purchasable items.')
            for item in retail.item_list:
                print(item.get_descr())
            print()

            item = input('Which item do you want to purchase? ')

            for x in retail.item_list:
                if item == retail.item_list[i].get_descr():
                    cash_register.purchase_item(item)
                    found = True
                i += 1

            print(cash_register.show_items())

        elif choice == '2':
            cash_register.clear()

        elif choice == '3':
            print(cash_register.get_total())

main()