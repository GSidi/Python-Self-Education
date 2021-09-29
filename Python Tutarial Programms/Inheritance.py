
class Polygon:

    def __init__(self, no_of_sides):
       self.n = no_of_sides
       self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides =  [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triange(Polygon):

    def __init__(self):
        return super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

class Square(Polygon):

    def __init__(self):
        return super().__init__(2)
    
    def findArea2(self):
        a, b = self.sides
        area = a*b
        print ("The area of the square is ",area)



t = Triange()

t.inputSides()
t.dispSides()
t.findArea()

s = Square()
s.inputSides()
s.dispSides()
s.findArea2()



