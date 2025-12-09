from abc import ABC


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp, ):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp


    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")



class BankAccount:
    def __init__(self, hero, bank_name, balance, password):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password

    def login(self, password):
        return self.__password == password
    def full_info(self):
        return (f"Герой: {self.hero.name} (Уровень {self.hero.lvl}), "
                f"Банк: {self.bank_name}, Баланс: {self._balance}")

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if isinstance(self.hero, self.hero.__class__) and isinstance(other.hero, self.hero.__class__):
            new_balance = self._balance + other._balance
            return BankAccount(self.hero, self.bank_name, new_balance, "temp_pass")
        else:
            raise TypeError("Сложение балансов возможно только между героями одного типа!")

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl
        return False



