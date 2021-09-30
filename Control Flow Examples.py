num1,num2,num3 = -5,13.7,8
if(num1 >= num2) and (num1 >=num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest is:",largest)

year = 2000

if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print(year, "is leap year")
        else:
            print(year, "is not leap year")
    else:
        print(year, "is leap year")

else:
    print(year, "is leap year")


year = input("Enter year:")
year = int(year)

n_terms = 10
n1,n2 = 0,1
count = 0

print("Fibo sequence up to ",n_terms," : ")
while count < n_terms:
    print(n1, end= ',' )
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print ()
