print("What operation do you want?")

operator = input("Enter either +,-,*, / :")

number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))

if operator == '+':
    print(number1, operator, number2, "=", number1+number2)
elif operator == '-':
    print(number1, operator, number2, "=", number1-number2)
elif operator == '*':
    print(number1, operator, number2, "=", number1*number2)
elif operator == '/':
    print(number1, operator, number2, "=", number1/number2)
else:
    print("Invalid Operator")