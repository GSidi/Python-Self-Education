def remote_control_next():
    yield "cnn"# yield retains the values where as return terminates the rest
    yield "espn"

itr = remote_control_next()

for c in remote_control_next():
    print(c)

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fibo():
    if f > 50:
        break
    print(f)
    
     
