#Example no1

def greet(name):
    print("Hello",name)
    print("What is going on?")
greet('Paul')
print("This is outside greet()")

#Example addition of 2 numbers

def add_numbers(n1,n2):
    sum = n1+n2
    print("sum is :", sum)
num1 =2
num2 = 3

add_numbers(num1, num2)

#Addition with return


def add_numbers(n1,n2):
    sum = n1+n2
    return sum
result = add_numbers(5, -12)

print("sum =", result)