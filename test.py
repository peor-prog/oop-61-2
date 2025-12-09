# def calculate_discount(hw_score, test_score, visits):
#     if 70 <= hw_score <= 80:
#         if test_score > 80:
#             return 3000
#         elif test_score > 60:
#             if visits >= 8:
#                 return 2500
#             else:
#                 return 2000
#
#     elif 50 <= hw_score <= 60:
#         if test_score > 80:
#             return 2000
#         elif test_score > 60:
#             if visits >= 6:
#                 return 2000
#             else:
#                 return 1000
#
#     return 0

def reverse_layout(text):
    ru = "йцукенгшщзхъфывапролджэячсмитьбю.ё"
    en = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    mapping = dict(zip(ru + en, en + ru))

    result = []
    for char in text:
        result.append(mapping.get(char, char))

    return ''.join(result).lower()
print("Конвертер раскладки (exit - выход)")

while True:
    text = input("Введите текст: ").strip()

    if text.lower() in ['exit', 'выход']:
        break

    if text:
        print(f"Результат: {reverse_layout(text)}")
    else:
        print("Введи текст а то поругаю!😡")








