'''
Польский калькулятор

Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации. Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

Формат вывода
Выведите единственное число — значение выражения.

Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * -
означает 10 - 2 * 4 и равно 2
'''

from typing import List

class Stack:
    def __init__(self):
        self.items: List[int] = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

def polish_calculator(line) -> str:
    stack = Stack()
    operators = OPERATORS
    for element in line:
        if element in operators:
            operand1, operand2 = stack.pop(), stack.pop()
            stack.push(int(operators[element](operand2, operand1)))
        else:
            stack.push(int(element))
    return stack.pop()


if __name__ == '__main__':
    line = input().split()
    print(polish_calculator(line))
