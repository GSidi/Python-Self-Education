""" class Person :
    "This i a class that creates a person"
    age = 10

    def greet(self):
        print('Hello')

#create new object of Person class
George = Person()

print(Person().greet)

print(George.greet)

#Calling objects greet method
George.greet() """

class ComplexNumber:

    #constructor
    def __init__(self, r=0, i=0) :
        
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

#creat new ComplexNumber object
num1 = ComplexNumber(2, 3)

#call get_dat method
num1.get_data()

#create 2nd ComplexNumber Object
num2 = ComplexNumber(2)
#new attribute
num2.attr = 10

print((num2.real, num2.imag, num2.attr))
#We created a new attribute attr for object num2 and read it as well.
#  But this does not create that attribute for object num1
print(num1.attr)

