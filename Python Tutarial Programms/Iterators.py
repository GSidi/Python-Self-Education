""" #define a list
my_list = [4, 5, 6 , 7]

#get an iterator 
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))

# next(obj) is same as obj.__next__()
print(my_iter.__next__())
print(my_iter.__next__())

"""
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
