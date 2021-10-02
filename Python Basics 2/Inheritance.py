class Vehicle:
    def general_usage(self):
        print("The general use of a vehicle is transportation")

class Car(Vehicle):
    def __init__(self):
        print("This is a car")
        self.weels = 4
        self.roof = True

    def specific_usage(self):
        print("Specific use of a car: Commute to work, vacation with the family")

class Moto(Vehicle):
    def __init__(self):
        print("This is a motorcycle")
        self.weels = 2
        self.roof = False

    def specific_usage(self):
        print("Specific use of a motorcycle: Road trip and racing")


c = Car()
c.general_usage()
c.specific_usage()

m = Moto()
m.general_usage()
m.specific_usage()
