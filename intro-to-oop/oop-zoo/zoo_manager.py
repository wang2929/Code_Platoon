class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return "Animal sound"
    
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"
    
class Primate(Mammal):
    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

class Marsupial(Mammal):
    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"
    
class Aviary():
    def __init__(self):
        self.birds = []
        
    def add_bird(self, **kwargs):
        new_bird = Bird(**kwargs)
        print(isinstance(new_bird, Bird))
        print(type(new_bird) == Bird)
        self.birds.append(new_bird)
        
class ReptileEnclosure():
    def __init__(self):
        self.reptiles = []
        
aviary = Aviary()
new_bird = { 'wingspan':'3', 'name':'Amsterdam Albatross', 'species':'Diomedea amsterdamensis' }
aviary.add_bird(**new_bird)