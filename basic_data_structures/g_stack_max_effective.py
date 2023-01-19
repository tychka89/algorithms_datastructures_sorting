'''
Стек - MaxEffective

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000.
Далее идут команды по одной в строке.

Команды могут быть следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример
Ввод
9
5
19 21 100 101 1 4 5 7 12

Вывод
6
'''

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items) - 1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items) - 1])
        self.items.append(item)

    def get_max(self):
        if self.isEmpty():
            return 'None'
        return self.max[len(self.items) - 1]


def pop(self):
    if self.isEmpty():
        return 'error'
    self.max.pop()
    return self.items.pop()


if __name__ == '__main__':
    s = StackMaxEffective()
    n = int(input())
    result = []
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            s.push(command[1])
        if command[0] == 'pop':
            if pop(s) == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(s.get_max())
    for i in result:
        print(i)