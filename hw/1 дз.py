
expenses = []

days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

for day in days:
    expense = float(input(f'Введите расходы за {day}: '))
    expenses.append(expense)

total = sum(expenses)
print(f'\nОбщие расходы за неделю: {total} сом.')




# print("привет,")
# print("скажи какой цвет светофора: красный, желтый, зеленый.")
# print("если не хочешь переходить напиши 'выход',\n")
# while True:
#     user_input = input("Цвет: ").strip().lower()
#     if user_input == "выход":
#         print("пока")
#         break
#     if user_input == "красный":
#         print("стоп\n")
#     elif user_input == "желтый":
#         print("будь на старте\n")
#     elif user_input == "зеленый":
#         print("иди\n")
#     else:
#         print("нет такого ответа'.\n")

