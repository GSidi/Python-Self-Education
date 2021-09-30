#Example 1

def greet(name,msg):
    print(("Hello", name + " , " + msg))
greet("Monica", "I like you") #if we input only one argument then we will face an error message


#Example 2 Default arguments in functions

def greet(name, msg = "Good morning"):
    print(("Hello", name + " , " + msg))
greet("Kate")
greet("Bruce","Whats up")

#Example 3 arbitary aruments

def greet(*names):
    print(names)
greet("monica","Is Lukes","Ex","Girlfriend")