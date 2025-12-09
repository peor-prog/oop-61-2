# списки, кортежи. Индексы и срезы
# списковое включение list comperehension
from operator import index

# numbers = [8,9,3,5,6]
# print(numbers)
# # Индексы
# print(numbers[0])
# print(numbers[-1])
# print('geeks'[0])

# срезы [start:stop:step]
# numbers =[8,9,3,5,6]
# print(numbers)
# print(numbers[1:4:1])
# print(numbers[::2])
# print(numbers[::-1])
# print('numbers'[::-1])

# numbers =[8,9,3,4,6]
# print(numbers)
# numbers.sort()
# numbers.reverse()
# numbers[2:].sort()
# numbers = numbers[:2] + sorted(numbers[2:1])

# numbers = [8,9,13,0.5,6]
#
# numbers.pop(2)  #удаляет по индексу и межет использаваться после
# numbers.remove(0.5)  #удаляет по значению
# del numbers[:2]   #удаляет по значению
# numbers.clear()   #удаляет полностью

# data = []
# counter = 10
# while counter > 0:
#   print(f'попыток осталось: {counter}')
#   counter -= 1
#   time = input('введите время суток').lower()
#   if time in ['exit', 'выход']:
#         print('exit....')
#         break
#   if time in ['morning', 'утро']:
#         print ==('good morning')
#   elif time in ['day','день']:
#         print ('good afternoon')
#   elif time in ['evening', 'вечер']:
#         print ("good evening")
#   else:
#      print('hello \n(время суток не распознано)')
#   data.append(time)
#   print(data)
# списковое включение list comperehension
# cities = ['toktogul', 'karakol', 'osh', 'bishkek']
# print(cities)
# cinies_edited = [citi.title() for city in cities if'o' in city]              ]
# print(cities_edited)






