class ZooWorker:
    def __init__(self, name):
        self.name = name

    def work(self, animal):
        pass

class ZooKeeper(ZooWorker):
    def __str__(self):
        return f"Заводчик {self.name}"
    def work(self, animal):
        print(f"{self.name} кормит следующее животное: {animal.species} {animal.name}...")
        animal.eat()

class Veterinarian(ZooWorker):
    def __str__(self):
        return f"Ветеринар {self.name}"
    
    def work(self, animal):
        print(f"{self.name} лечит следующее животное: {animal.species} {animal.name}...")
        animal.make_sound()