class Vehicle:
    def start(self):
        print("Vehicle starting")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class ElectricCar(Vehicle):
    def start(self):
        super().start()
        print("Electric car starting")
class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesla ready")

print(Tesla.mro())
Tesla().start()
