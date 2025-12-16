# операторы пренадлежности in
from itertools import count

# print(5 in range(1,6))
# print(25 in range(1,6))
#
# print('p' in 'python')

# number = 5
# print(number)
# number = number + 3
# number += 3
# number **= 2
# number //=3
#
# counter = 0
# while counter < 100:
#     counter += 1
#     if counter == 55:
#         break
#     if counter ==52:
#         continue
#     print('hello world')

# counter = 10
# while counter > 0:
#   print(f'попыток осталось: {counter}')
#   counter -= 1
#   time = input('введите время суток').lower()
#   if time == 'exit' or time =='выход':
#         print('exit....')
#         break
#   if time == 'morning' or time == 'утро':
#         print ==('good morning')
#   elif time == 'day' or time == 'день':
#         print ('good afternoon')
#   elif time == 'evening' or time == 'вечер':
#         print ("good evening")
#   else:
#      print('hello \n(время суток не распознано)')



# word = 'KYRGYZSTAN'
# for letter in word:
#     if letter == 's':
#         break
#     if letter in 'YRZ':
#         continue
#     print(letter)




while True:


        slovo = input("Введите слово (или 'выход' для завершения): ")


        if slovo.lower() == "выход":
            print("До свидания!")
            break


        vsego = len(slovo)


        glasnye = 0
        soglasnye = 0
        glasnye_bukvy = "аеёийоуыэюяАЕЁИЙОУЫЭЮЯ"

        for bukva in slovo:
            if bukva in glasnye_bukvy:
                glasnye += 1
            else:
                soglasnye += 1


        if vsego > 0:
            procent_glasnyh = round((glasnye / vsego) * 100, 2)
            procent_soglasnyh = round((soglasnye / vsego) * 100, 2)
        else:
            procent_glasnyh = 0
            procent_soglasnyh = 0

        print(f"Слово: {slovo}")
        print(f"Количество букв: {vsego}")
        print(f"Согласных букв: {soglasnye}")
        print(f"Гласных букв: {glasnye}")
        print(f"Гласные/Согласные: {procent_glasnyh}% / {procent_soglasnyh}%")
        print("-" * 30)

