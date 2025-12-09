# функции: виды параметров, возвращение данных, виды аргументов.
# from ipaddress import summarize_address_range


# определение наименование(параметры):
#     тело функции (логика)
#     возвращение обьекта (результат)
# вызов функции
# наименование(аргументы)


# def some_name(name, surname='unknown'):  #regueier positional parameter (обезациальный параметр)
#     print(f'name: {name} surname: {surname}')
#
# some_name('bruce','lee')     #regueier positional parameter (обезательный позиционный оргумент)
# some_name(surname='bruce', name='lee')     # keyword arguments (оргумент)
#                        возвращениеобьекта(результат)

# def get_area(length, width):
#     return length * width
#
# square_2 = get_area(7,5)
# square_coworking = get_area(15, 10)
# print(square_2)
# print(square_coworking)

# def get_area(length: int, width: int)-> int:
#     """эта функция возврощает площадь геометрической фигуры """
#     return length * width
#
#
# print(get_area.__doc__)
# print(help(get_area))

#
# def check_password(password):
#     if len(password) < 6:
#         return False
#     has_digit = False
#     has_upper = False
#     has_lower = False
#     has_symbol = False
#     for char in password:
#         if char.isdigit():
#             has_digit = True
#         elif char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         else:
#             has_symbol = True
#     if has_digit and has_upper and has_lower and has_symbol:
#         return True
#     else:
#         return False
#
# print(check_password("$PassW/12"))
# print(check_password("password"))
# print(check_password("12345"))
#
#
# def find_closest_number(numbers, target=0):
#
#     closest = numbers[0]
#     min_difference = abs(numbers[0] - target)
#     for num in numbers:
#         difference = abs(num - target)
#         if difference < min_difference:
#             min_difference = difference
#             closest = num
#
#     return closest
#
# numbers_list = [1, 2, 3, 8, 10]
# print(find_closest_number(numbers_list, 5))
# print(find_closest_number(numbers_list, 7))
# print(find_closest_number(numbers_list))
#







