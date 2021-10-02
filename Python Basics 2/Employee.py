class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"{self.id} \nName: {self.name}")


emp = Employee(1, "coder")
emp.display()

del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")