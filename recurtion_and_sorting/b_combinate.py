'''
Комбинации

На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:
2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.

Пример
Ввод
23

Вывод
ad ae af bd be bf cd ce cf
'''

SYMBOLS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

def letter_combinations(*prefix):
    if not prefix:
        return [[]]
    else:
        return [[x] + p for x in prefix[0] for p in letter_combinations(*prefix[1:])]


numbers = list(map(int, input()))
seqs = []
for number in numbers:
    seqs.append(list(SYMBOLS[number]))
result = letter_combinations(*seqs)
print(' '.join([''.join(index) for index in result]))