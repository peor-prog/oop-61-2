words = {
    'False': True,
    'class': True,
    'from': None,
    'or': True,
    'None': True,
    'continue': True,
    'global': None,
    'pass': None,
    'True': True,
    'def': True,
    'if': True,
    'raise': None,
    'and': True,
    'del': True,
    'import': None,
    'return': True,
    'as': None,
    'elif': True,
    'in': True,
    'try': True,
    'assert': None,
    'else': True,
    'is': None,
    'while': True,
    'async': None,
    'except': True,
    'lambda': True,
    'with': None,
    'await': None,
    'finally': True,
    'nonlocal': None,
    'yield': None,
    'break': True,
    'for': True,
    'not': True
}
total_words = len(words)
print("Всего слов:", total_words)
passed_words = 0
for word_status in words.values():
    if word_status == True:
        passed_words += 1
print("Пройдено слов:", passed_words)
percent = (passed_words / total_words) * 100
print("Пройдено:", round(percent, 1), "%")