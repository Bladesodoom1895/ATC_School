#program tests the cellphone class

#PPr10-13

import cellphone

def main():
    #get the phone data
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model numer: ')
    retail = float(input('Enter the retail price: '))

    #create an instance of the Cellphone class
    phone = cellphone.CellPhone(man, mod, retail)

    #display the data that was entered
    print('Here is the data that you entered: ')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), ',.2f'), sep='')

#call the main function
main()