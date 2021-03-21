import random

#PPr10-1

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