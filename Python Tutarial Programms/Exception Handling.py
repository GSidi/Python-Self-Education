#catching exceptions in python

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)


#code to print the reciprocal of even numbers

try:
    num = int(input("Enter a number"))
    assert num % 2 == 0
except:
    print("This is not an even number")
else:
    reciprocal = 1/num
    print(reciprocal)