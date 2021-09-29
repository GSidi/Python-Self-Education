#A simple generator 

def my_gen():
    i = 1
    print("This is printed first ")
    yield i 

    i +=1
    print("This is printed second")
    yield i

    i += 1
    print("This is printed last")
    yield i

""" a = my_gen()

next(a)
next(a)
next(a)"""

# Using for loop
for item in my_gen():
    print(item)

# A more complicated and acctual example of an generator

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1 , -1, -1):
        yield my_str[i]

for char in rev_str("George Sidiropoulos"):
    print(char)


# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))