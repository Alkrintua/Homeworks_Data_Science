# create a car class
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


blue_car = Car("blue", 20000)
red_car = Car("red", 30000)
print(blue_car)
print(red_car)


