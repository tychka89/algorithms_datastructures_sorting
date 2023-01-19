"""
Двоичная система

Тимофей записал два числа в двоичной системе счисления и попросил Гошу
вывести их сумму, также в двоичной системе. Встроенную в язык
программирования возможность сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.
Решение должно работать за O(N), где N –— количество разрядов максимального
числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.

Пример
Ввод	            Вывод
1010                10101
1011
"""

num1 = input()
num2 = input()
if (len(num1) >= len(num2)):
    n = len(num1)
    num2 = num2.zfill(n)
else:
    n = len(num2)
    num1 = num1.zfill(n)
num1 = list(num1)
num2 = list(num2)
for i in range(len(num1)):
    num1[i] = int(num1[i])
for i in range(len(num2)):
    num2[i] = int(num2[i])
num1.reverse()
num2.reverse()
num_it = []
if (len(num1) >= len(num2)):
    n = len(num1)
else:
    n = len(num1)
flag = 0
for i in range(n):
    temp = num1[i] + num2[i] + flag
    if temp == 0:
        num_it.append(0)
    elif temp == 1:
        num_it.append(1)
        flag = 0
    elif temp == 2:
        num_it.append(0)
        flag = 1
    else:
        num_it.append(1)
        flag = 1
if flag == 1:
    num_it.append(1)
num_it.reverse()
for i in range(len(num_it)):
    print(num_it[i], end='')