# def nearest_number(numbers, target):
#     distances = [(abs(num - target), num) for num in numbers]
#     distances.sort()
#     sorted_nums = [num for dist, num in distances]
#     return (target, sorted_nums)
#
# numbers = [1, 5, 8, 12, 3]
# target = 6
# result = nearest_number(numbers, target)
# print(result)  # (6, [5, 8, 3, 1, 12])




# # например с filter оставить строки длиной больше 3 символов
# words = ["cat", "dog", "elephant", "hi", "python"]
# long_words = list(filter(lambda word: len(word) > 3, words))
# print(long_words)  # ['elephant', 'python']
#
# # например с map преобразовать все числа в их квадраты
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)

def get_element(iterable=[1, 2, 3, 4, 5]):
    """
    """
    attempts = 0
    max_attempts = 14

    while attempts < max_attempts:
        try:
            print(f"\nПопытка {attempts + 1} из {max_attempts}")
            index = input("Введите индекс (или 'выход' для завершения): ")

            if index.lower() in ['выход', 'exit', 'quit']:
                print("Программа завершена.")
                break

            index = int(index)
            element = iterable[index]
            print(f"Элемент с индексом {index}: {element}")
            attempts += 1

        except ValueError:
            print("Ошибка: введите целое число!")
        except IndexError:
            last_index = len(iterable) - 1
            print(f"Ошибка: индекс должен быть от 0 до {last_index}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    if attempts == max_attempts:
        print(f"\nДостигнут лимит в {max_attempts} попыток. Программа завершена.")
get_element()
