def squares():
    a = 0
    while True:
        yield a*a
        a +=1

for s in squares():
    if s > 100:
        break
    print(s)
    
