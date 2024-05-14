class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.species.capitalize()} {self.name}, полных лет: {self.age}"

    def make_sound(self):
        pass

    def eat(self):
        print("Ням ням...")

class Bird(Animal):
    def __init__(self, species, name, age, can_fly = True):
        super().__init__(species, name, age)
        self.can_fly = can_fly

    def __str__(self):
        return f"{super().__str__()}\n\t{'' if self.can_fly else 'не '}летает"
    
    def make_sound(self):
        print("чик-чирик")

    def eat(self):
        super().eat()
        print("Я ем зёрна!")

class Mammal(Animal):
    def __init__(self, species, name, age, terrestrial = True, can_fly = False, predator = True, says = "Meow"):
        super().__init__(species, name, age)
        self.terrestrial = terrestrial
        self.can_fly = can_fly
        self.predator = predator
        self.says = says
    
    def __str__(self):
        return f"{super().__str__()}\n\t{'наземное' if self.terrestrial else 'водное'}, {'' if self.can_fly else 'не '}летает, {'' if not self.predator else 'не '}хищник"
    
    def make_sound(self):
        print(self.says)

    def eat(self):
        super().eat()
        if self.predator:
            print("Я ем мясо!")
        else:
            print("Я ем растения!")

class Reptile(Animal):
    def __init__(self, species, name, age, poisony = True):
        super().__init__(species, name, age)
        self.poisony = poisony

    def __str__(self):
        return f"{super().__str__()}\n\t{'' if self.poisony else 'не '}ядовито"
    
    def make_sound(self):
        print("ш-ш-ш")

    def eat(self):
        super().eat()
        print("Съем тебя!")