class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Птица чирикает"
    def eat(self):
        return "Птица питается семенами"

class Mammal(Animal):
    def make_sound(self):
        return "Млекопитающее рычит"
    def eat(self):
        return "Млекопитающее питаетя травой"

class Reptile(Animal):
    def make_sound(self):
        return "Рептилия шипит"
    def eat(self):
        return "Рептилия питается насекомыми"

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}"

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

def animal_eat(animals):
    for animal in animals:
        print(animal.eat())

# Пример использования

bird = Bird("Голубь", 5)
mammal = Mammal("Лев", 10)
reptile = Reptile("Змея", 3)

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zookeeper = ZooKeeper("Саша")
veterinarian = Veterinarian("Маша")

print(zookeeper.feed_animal(bird))
print(veterinarian.heal_animal(mammal))

animal_sound(zoo.animals)
animal_eat(zoo.animals)
