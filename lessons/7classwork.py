#lambda функци.Об работка исключений
# from distutils.command.build_scripts import first_line_re
# from tkinter.font import names

# def up_first_line_re(word: str):
#     return word.title()
# print(up_first_line_re(kirill))

# def show_words(func, words):
#     for word in words:
#         print(func(words))
#
# list_words = ['red', 'yellow']
# show_words(up_first)

# def def_f(n1, n2):
#     return n1 + n2
# print(type(def_f))
# print(def_f(2,3))
#
# lambda_f = lambda  n1, n2: n1 + n2
# print(type(lambda_f))
# print(lambda_f(3, 2))


# def show_words(func, words):
#     for word in words:
#         print(func(words))
# list_words = ['red', 'yellow', 'blue', 'green', 'white', 'orange']
# show_words(lambda word: word.title(), list_words)

# sorted_words = sorted(list_words, key=lambda word: word[2])
# print(sorted_words)

# list_words = list(filter(lambda words: 'l' in word, list_words))
# print(filter_words)

try:
    print(2 + 1)
except:
    print('обнаружена ошибка и обработана!')
else:
    print('щшибок не обнарежена!')
finally:
    print('проверка завершена!')















