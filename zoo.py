from animals import Bird, Mammal, Reptile
from workers import ZooKeeper, Veterinarian
import random

def add_blank_line_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print()  # Печатает пустую строку
        return result
    return wrapper

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    @add_blank_line_decorator
    def load(self, filename):
        animals = []
        employees = []
        try:
            with open(filename) as file:
                for line in file:
                    line = line.strip().split(",")
                    if line[0] == "bird":
                        animals.append(Bird(line[1], line[2], line[3], line[4] == "True"))
                    elif line[0] == "mammal":
                        animals.append(Mammal(line[1], line[2], line[3], line[4] == "True", line[5] == "True", line[6] == "True", line[7]))
                    elif line[0] == "reptile":
                        animals.append(Reptile(line[1], line[2], line[3], line[4] == "True"))
                    elif line[0] == "zookeeper":
                        employees.append(ZooKeeper(line[1]))
                    elif line[0] == "veterinarian":
                        employees.append(Veterinarian(line[1]))
        except FileNotFoundError:
            pass
        self.animals = animals
        self.employees = employees

    @add_blank_line_decorator
    def save(self, filename):
        with open(filename, "w") as file:
            for animal in self.animals:
                if isinstance(animal, Bird):
                    file.write(f"bird,{animal.species},{animal.name},{animal.age},{animal.can_fly}\n")
                elif isinstance(animal, Mammal):
                    file.write(f"mammal,{animal.species},{animal.name},{animal.age},{animal.terrestrial},{animal.can_fly},{animal.predator},{animal.says}\n")
                elif isinstance(animal, Reptile):
                    file.write(f"reptile,{animal.species},{animal.name},{animal.age},{animal.poisony}\n")
            for employee in self.employees:
                if isinstance(employee, ZooKeeper):
                    file.write(f"zookeeper,{employee.name}\n")
                elif isinstance(employee, Veterinarian):
                    file.write(f"veterinarian,{employee.name}\n")
    
    def __get_name_age(self):
        name = input("Введите имя животного: ")
        age = None
        while age is None:
            try:
                age = int(input("Введите возраст животного: "))
            except ValueError:
                pass
        return name, age
    
    def __get_boolean(self, question):
        while True:
            print(question)
            answer = input("1 - Да, 0 - Нет: ").strip()
            if answer == "1":
                return True
            if answer == "0":
                return False

    @add_blank_line_decorator
    def add_animal(self):
        while True:
            animal_type = input("Выберите вид животного: 1 - Птица, 2 - Млекопитающее, 3 - Рептилия: ").strip()
            if animal_type == "1":
                species = input("Введите вид птицы: ")
                name, age = self.__get_name_age()
                can_fly = self.__get_boolean("Птица умеет летать?")
                self.animals.append(Bird(species, name, age, can_fly))
                return
            if animal_type == "2":
                species = input("Введите вид млекопитающего: ")
                name, age = self.__get_name_age()
                terrestrial = self.__get_boolean("Млекопитающее наземное?")
                can_fly = self.__get_boolean("Млекопитающее может летать?")
                predator = self.__get_boolean("Млекопитающее является хищником?")
                says = input("Какие звуки издает млекопитающее? ")
                self.animals.append(Mammal(species, name, age, terrestrial, can_fly, predator, says))
                return
            if animal_type == "3":
                species = input("Введите вид рептилии: ")
                name, age = self.__get_name_age()
                poisony = self.__get_boolean("Рептилия является ядовитой?")
                self.animals.append(Reptile(species, name, age, poisony))
                return
    
    @add_blank_line_decorator
    def add_employee(self):
        while True:
            employee_type = input("Выберите тип сотрудника: 1 - Заводчик, 2 - Ветеринар: ").strip()
            if employee_type == "1":
                name = input("Введите имя заводчика: ")
                self.employees.append(ZooKeeper(name))
                return
            if employee_type == "2":
                name = input("Введите имя ветеринара: ")
                self.employees.append(Veterinarian(name))
                return

    @add_blank_line_decorator
    def disturb_animals(self):
        for animal in self.animals:
            animal.make_sound()

    @add_blank_line_decorator
    def __show_animals(self):
        if len(self.animals) == 0:
            print("Нет животных")
            return
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal}")

    @add_blank_line_decorator
    def __show_employees(self):
        if len(self.employees) == 0:
            print("Нет сотрудников")
            return
        for i, employee in enumerate(self.employees, 1):
            print(f"{i}. {employee}")

    def show_all(self):
        print("Животные:")
        self.__show_animals()
        print("Сотрудники:")
        self.__show_employees()

    @add_blank_line_decorator
    def feed_animals(self):
        zookeepers = [employee for employee in self.employees if isinstance(employee, ZooKeeper)]
        if len(zookeepers) == 0:
            print("Наймите заводчиков!")
            return
        for animal in self.animals:
            zookeeper = random.choice(zookeepers)
            zookeeper.work(animal)

    @add_blank_line_decorator
    def treat_animals(self):
        veterinarians = [employee for employee in self.employees if isinstance(employee, Veterinarian)]
        if len(veterinarians) == 0:
            print("Наймите ветеринаров!")
            return
        for animal in self.animals:
            veterinarian = random.choice(veterinarians)
            veterinarian.work(animal)