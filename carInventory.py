import matplotlib.pyplot as plt
%matplotlib inline

class Car:
    max_speed = 120
    mileage = 30

    def __init__(self, speed, mileage, color="white"):
        self.speed = speed
        self.mileage = mileage
        self.color = color
        
    def assign_seatcap(self, noofseats):
        self.seats = noofseats

    def display_properties(self):
        print("Car details", "\n", self.speed,",",self.mileage,",", self.seats,",", self.color)

car1 = Car(200,20)
car1.assign_seatcap(5)
car2 = Car(185, 25)
car2.assign_seatcap(4)

car1.display_properties()
car2.display_properties()
