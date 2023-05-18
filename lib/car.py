from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass
  
print(Car.__base__)
print(type(Car))
car2=Car(20,4)
print(car2.go())