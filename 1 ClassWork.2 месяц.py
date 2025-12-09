


class Car:
    """
    Класс Car — описывает автомобили
    """
    def _init_(self, name, age, color):
        self.name = name         # марка/модель
        self.age = age           # возраст в годах
        self.color = color       # цвет
        self.fuel = True         # есть ли топливо

    def start(self):
        """Машина заводится"""
        if self.fuel:
            return f"{self.name} говорит: Vroom Vroom!"
        else:
            return f"{self.name} не заводится - нет топлива!"

    def refuel(self, fuel_type="бензин"):
        """Заправляем машину"""
        self.fuel = True
        return f"{self.name} заправлен {fuel_type} и готов к поездке!"

    def info(self):
        """Информация о машине"""
        status = "нуждается в заправке" if not self.fuel else "заправлена"
        return f"Машина: {self.name}, {self.age} лет, цвет: {self.color}, сейчас {status}"


# Создаём несколько машин и проверяем
car1 = Car("Toyota", 3, "серый")
car2 = Car("BMW", 2, "чёрный")
car3 = Car("Lada", 5, "красный")

# Проверяем методы
print(car1.info())
print(car1.start())
print(car1.refuel("бензин"))
print(car1.info())

print("\n" + car2.info())
print(car2.start())
print(car2.refuel())

print("\n" + car3.info())
print(car3.start())

# HeroMage
# hero_mage

class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def base_method(self):
        return f"base action {self.name}"

# объект/экземпляр на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)

print(asuna.base_method())
# объект/экземпляр на основе класса
my_text = "Just text"
my_text_2 = "Just text 2"
my_int = 123
my_list = (1,2,3,45)

my_list_2 = (1,2,3,45)

# print(type(kirito))
# print(type(my_text))
# print(my_text)
# print(my_text)
# print(my_text)
# print(my_text)
# print(my_text)
































