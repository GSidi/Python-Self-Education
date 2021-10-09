#User defined exception

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def print_exception(self):
        print("This is a user defined exception",self.msg)

try:
    raise Accident("Crash between cars")
except Accident as e:
    e.print_exception()


#System defined exception

try:
    raise MemoryError ("Memory Error")
except MemoryError as e:
    print(e)
    