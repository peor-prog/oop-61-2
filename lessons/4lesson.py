class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return self.name + " готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return "Маг " + self.name + " кастует заклинание! MP: " + str(self.mp)

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, rage):
        super().__init__(name, lvl, hp, 0)
        self.rage = rage

    def action(self):
        return "Воин " + self.name + " рубит мечом! Уровень: " + str(self.lvl)

class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance, password, bank_name=None):
        self.hero = hero
        self._balance = balance
        self.__pass = password
        if bank_name:
            BankAccount.bank_name = bank_name

    def login(self, p):
        return p == self.__pass

    @property
    def full_info(self):
        return self.hero.name + " lvl " + str(self.hero.lvl) + " | " + str(self._balance)

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod
    def bonus_for_level():
        return 500

    def _str_(self):
        return self.hero.name + " | Баланс: " + str(self._balance) + " SOM"

    def _add_(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def _eq_(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl

class SmsService:
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return "<text>Код: 1234</text><phone>" + phone + "</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
war = WarriorHero("Conan", 50, 900, 20)

a1 = BankAccount(mage1, 5000, "1234", "Simba")
a2 = BankAccount(mage2, 3000, "0000", "Simba")
a3 = BankAccount(war, 2500, "1111", "Simba")

print(mage1.action())
print(war.action())

print(a1)
print(a2)

print("Банк:", a1.get_bank_name())
print("Бонус за уровень:", a1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", a1 + a2)
print("Сумма мага и воина:", a1 + a3)

sms = KGSms()
print("\n", sms.send_otp("+996777123456"))






























