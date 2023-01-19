'''
Списочная очередь

Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка.
Помогите ему с реализацией.

Очередь должна поддерживать выполнение трёх команд:
get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000.
В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Пример
Ввод
10
put -34
put -23
get
size
get
size
get
get
put 80
size

Вывод
-34
1
-23
0
error
error
1
'''

class ListQueue:
    class Node:
        def __init__(self, value=None, next_item=None):
            self.value = value
            self.next_item = next_item

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def get(self):
        if self.isEmpty():
            return 'error'
        if self.size == 1:
            removed = self.head
            self.__init__()
            return removed.value
        if self.size == 2:
            removed = self.head
            self.head = self.tail
            self.size -= 1
            return removed.value
        removed = self.head
        self.head = self.tail.next_item.next_item
        self.tail.next_item = self.head
        self.size -= 1
        return removed.value

    def put(self, item):
        if self.isEmpty():
            self.head = self.Node(value=item)
            self.tail = self.head
        else:
            self.tail.next_item = self.Node(value=item)
            self.tail.next_item.next_item = self.head
            self.tail = self.tail.next_item
        self.size += 1

    def size(self):
        return self.size


if __name__ == '__main__':
    n = int(input())
    stack = ListQueue()
    result_list = []

    for i in range(n):
        command = input().split()
        if command[0] == 'put':
            stack.put(int(command[1]))
        if command[0] == 'get':
            result_list.append(stack.get())
        if command[0] == '__size':
            result_list.append(stack.size)

    for i in result_list:
        print(i)