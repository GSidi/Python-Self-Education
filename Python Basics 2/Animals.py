class Animal:
    def __init__(self, type, limbs, habbits):
        self.type = type
        self.limbs = limbs
        self.habbits = habbits
        
    def general_habbitat(self):
        print("Each animal has a preferable habbitat")

class Dog(Animal):
    def __init__(self, type, limbs, habbits):
        super().__init__(type, limbs, habbits)
        print("Type: ", type, "\nNumber of Limbs: ", limbs,"\nHabbits: ", habbits)

    def specific_habbitat(self):
        print("A dogs natural habbitat it is defined by it type/race")



d = Dog("German Shepperd", 4, "Heralding sheep")
d.general_habbitat()
d.specific_habbitat()