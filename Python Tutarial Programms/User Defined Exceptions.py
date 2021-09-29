#User Defined Exceptions

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmall(Exception):
    """Raised when input is too small"""
    pass

class ValueTooBig(Exception):
    """Raised when input is too big"""
    pass

number = 100

#user guesses the number until it is true

while True:
    try:
        i_num = int(input("Enter a number : "))
        if i_num < number :
            raise ValueTooSmall
        elif i_num > number:
            raise ValueTooBig
        break
    except ValueTooSmall:
        print("This value is too small, try again!!")
        print()

    except ValueTooBig:
        print("This value is too big, try again!!")
        print()

print("Congratulations, you guessed right")


#part 2 of user defined exceptions

class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
