def calculate_area(base, height, shape = "Triangle"):

    if shape == "Triangle":
        area = (1/2)*base * height
    elif shape == "Rectangle":
        area = base * height
    else:
        print("Not an area we can calculate")

    return area

num = calculate_area(3,3,"Triangle")
num = calculate_area(3,3,"Rectangle")
num = calculate_area(3,3,)

print("The area of our shape is: ",num)


def print_pattern(n=5):
    '''
    :param n: Integer number representing number of lines
    to be printed in a pattern. If n=3 it will print,
      *
      **
      ***
    If n=4, it will print,
      *
      **
      ***
      ****
    Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    '''
    # we need to run two for loops. Outer loop prints patterns line by line
    # where as inner loop print the content of that specific lines
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)




