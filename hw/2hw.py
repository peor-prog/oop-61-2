class Animal:
    def __init__(self, n, a, h):
        self.name = n
        self.age = a
        self.health = h

    def info(self):
        return f"{self.name}, {self.age} лет, здоровье {self.health}"

    def ability(self):
        return f"{self.name} использует базовую способность."


class Duck(Animal):
    def ability(self):
        return f"{self.name} использует базовую способность. летает. плавает."


class Bat(Animal):
    def ability(self):
        return f"{self.name} использует базовую способность. летает. становится невидимым."


class Frog(Animal):
    def ability(self):
        return f"{self.name} использует базовую способность. плавает."


class Phoenix(Animal):
    def ability(self):
        return f"{self.name} использует базовую способность. летает. становится невидимым."
zoo = []
zoo.append(Duck("Дональд", 3, 80))
zoo.append(Bat("Бэтти", 5, 60))
zoo.append(Frog("Кермит", 2, 50))
zoo.append(Phoenix("Феникс", 100, 200))

for animal in zoo:
    print(animal.info())
    print(animal.ability())