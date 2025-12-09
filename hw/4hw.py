data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')


letters = []
numbers = []


for item in data_tuple:

    if type(item) == str:
        letters.append(item)
    else:
        numbers.append(item)


numbers.remove(6.13)
true_value = numbers.pop(1)
letters.append(true_value)


numbers.insert(1, 2)


numbers.sort()


letters.reverse()


for i in range(len(letters)):
    if letters[i] == 'C':
        letters[i] = 'c'
    elif letters[i] == 'h':
        letters[i] = 'H'


for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2


letters = tuple(letters)
numbers = tuple(numbers)


print("letters:", letters)
print("numbers:", numbers)