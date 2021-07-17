from abc import ABC
class animals(ABC):
    def eat(self):
        pass
    def movement(self):
        pass
    def species(self):
        pass
class mammals(animals):
    def eat(self):
        print("mammals are omnivores")
    def movement(self):
        print("mammals move in diferent ways")
    def species(self):
        print("some mammals are: Rats, cats, dogs, monkeys, wahle, human")
class reptiles(animals):
    def eat(self):
        print("reptiles are  carnivores")
    def movement(self):
        print("reptiles crawl")
    def species(self):
        print("some reptiles are: lizards, crocodile, snake, geckos")
class birds(animals):
    def eat(self):
        print("birds are omnivores")
    def movement(self):
        print("birds can fly")
    def species(self):
        print("some birds are: pegion, crow, sparrow, parrot")
class amphibians(animals):
    def eat(self):
        print("amphibians are carnivores")
    def movement(self):
        print("amphibians can crawl,hop")
    def species(self):
        print("some amphibians are: frogs,salamanders,caecilians")
m=mammals()
m.eat()
m.movement()
m.species()
r=reptiles()
r.eat()
r.movement()
r.species()
b=birds()
b.eat()
b.movement()
b.species()
a=amphibians()
a.eat()
a.movement()
a.species()

