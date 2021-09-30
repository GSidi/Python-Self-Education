num  = [1,5,0,-4,10,9]

for val in num :
    if val <0:
        break
    print(val)

sum = 0

while True:
    n = input("Enter number")
    n = float(n)
    if n <0 :
        sum += n
        break

print("sum =",sum)

num2 = [1,4,-100,5,-9]

for val2 in num2:
    if val <= 0 :
        continue
    print(val)
print("this is out")
