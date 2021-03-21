import random

#PPr10-2

#the coin class simulates coin flip

class Coin:

    #the __init__method initializes
    #the sideup attribute with heads

    def __init__(self):
        self.sideup = 'Heads'

    #toss method generates a random number
    #in the range of 0 through 1. if number
    #is 0 then sideup is set to heads
    #if 1 then sideup is set to tails

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    #get_sideup method returns the value
    #referenced by sideup
    def get_sideup(self):
        return self.sideup


#the main function
def main():
    #create an object from the coin class
    my_coin = Coin()

    #display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())

    #toss the coin
    print('I am tossing the coin ...')
    my_coin.toss()

    #display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())

#call the main function
main()