#Creating a simple class
""" class parrot :

    species = "bird"

    def __init__(self, name, age) :
        self.name = name
        self.age = age

blu = parrot("Blue", 12)
woo = parrot("Red", 20)

#access the class attributes

print("Blu is a {}".format(blu.__class__.species))

print("Woo is a {}".format(woo.__class__.species))

#access the instance attributes

print ("{} is {} years old".format(blu.name,blu.age))
print ("{} is {} years old".format(woo.name,woo.age))   """"

#Creating methids in a class

""" class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance()) """

#Inheritance 

""" class Bird :

    def __init__(self) :
        print ("Bird is ready")
    
    def whoisThis (self):
        print("Bird")

    def swim(self):
        print("Swim faster")

#child class

class Penguin(Bird):

    def __init__(self):
        #call super function
        super().__init__()
        print("Penguin is ready ")
    
    def whoisThis(self):
        print("Penguin ")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run() 
 """

#Encapsulation


class Computer :

    def __init__(self) :
        self.__maxprice = 900 #this is how we create private variables with one _ or __ (two)

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the max price
c.__maxprice = 1000
c.sell()

#using setter function 
c.setMaxPrice(1000)
c.sell()

#Polymorphism in Python OOP

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)