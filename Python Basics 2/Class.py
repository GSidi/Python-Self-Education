class Human:
    #constructor
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    #methods
    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name,"plays tennis")
        elif self.occupation == "Actor":
            print(self.name, "shoots a film")
    
    def speaks(self):
        print(self.name, "say how are you managing")

tom = Human("Tom","Actor")
tom.do_work()
tom.speaks()
maria = Human("Maria","Tennis Player")
maria.do_work()
maria.speaks()

