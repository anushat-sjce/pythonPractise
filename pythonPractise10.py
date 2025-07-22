class Car:
    max_speed = 120
    
    def __init__(self, make, model, color, speed=10):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        if (self.speed + acceleration <= Car.max_speed):
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
        
    def get_speed(self):
        return self.speed


car1 = Car("Toyota", "Camry", "Silver")
car2 = Car("Honda", "Civic", "Red")

car1.accelerate(100)
car2.accelerate(150)

print(car1.get_speed())
print(car2.get_speed())
