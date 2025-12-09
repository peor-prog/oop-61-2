class Product:
    def _init_(self, name, price):
        self.name = name
        self._price = price
        self.__discount = 0
    def get_price(self):

        final_price = self.price * (1 - self._discount / 100)
        return final_price

    def set_discount(self, percent):

        if percent <= 50:
            self.__discount = percent
        else:
            return "Ошибка: скидка не может быть больше 50%"

    def apply_extra_discount(self, secret_code):

        if secret_code == "VIP123":
            current_price = self.get_price()
            self._price = current_price * 0.95  # Уменьшаем на 5%
        else:
            print("Неверный код")
print("=== Проверка класса Product ===")
p = Product("Iphone", 1000)

p.set_discount(20)
print("Цена со скидкой:", p.get_price())

p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())

p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())

print()
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        result = {
            "type": "crypto",
            "amount": amount,
            "currency": "USDT"
        }
        print(result)

    def refund(self, amount):
        result = {
            "type": "crypto_refund",
            "amount": amount,
            "currency": "USDT"
        }
        print(result)

class PaymentProcessor:
    def _init_(self, payment_method):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.pay(amount)


print("=== Проверка системы оплаты ===")

print("1. Оплата картой:")
processor = PaymentProcessor(CardPayment())
processor.process(100)

print("\n2. Оплата наличными:")
processor = PaymentProcessor(CashPayment())
processor.process(50)

print("\n3. Оплата криптовалютой:")
processor = PaymentProcessor(CryptoPayment())
processor.process(200.0)

print("\n=== Проверка возвратов ===")
card = CardPayment()
card.refund(30)

cash = CashPayment()
cash.refund(20)

crypto = CryptoPayment()
crypto.refund(100.0)