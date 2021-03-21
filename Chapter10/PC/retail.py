#retail class file

class RetailItem:
    def __init__(self, item_num, descr, num_units, price):
        self.__item_num = item_num
        self.__descr = descr
        self.__num_units = num_units
        self.__price = price

item1 = RetailItem(1, 'Jacket', 12, 59.95)
item2 = RetailItem(2, 'Designer Jeans', 40, 34.95)
item3 = RetailItem(3, 'Shirt', 20, 24.95)

item_list = [item1, item2, item3]