#car class program

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed

    
def main():
    year = int(input('Enter the year of the car: '))
    make = input('Enter the make of the car: ')

    car = Car(year, make)

    for i in range(5):
        car.accelerate()
        print('The current speed is: ', car.get_speed())

    for i in range(5):
        car.brake()
        print('The current speed is: ', car.get_speed())

main()