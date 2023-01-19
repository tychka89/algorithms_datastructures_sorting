'''
Дек

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000.
Во второй строке записано число m — максимальный размер дека.
Он не превосходит 50000.

В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример
Ввод
4
4
push_front 861
push_front -819
pop_back
pop_back

Вывод
861
-819
'''

class FullQueueError(Exception):
    def __str__(self):
        return 'error'

    def __init__(self):
        super().__init__('error')


class EmptyQueueError(Exception):
    def __str__(self):
        return 'error'

    def __init__(self):
        super().__init__('error')


class Deque:

    def __init__(self, max_size: int):
        self.__elements = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __is_full_queue(self):
        return self.__size == self.__max_size

    def __is_empty_queue(self):
        return self.__size == 0

    def __get_index(self, method: str):
        if method == 'push_front':
            if self.__is_empty_queue():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__head - 1) % self.__max_size
        if method == 'push_back':
            if self.__is_empty_queue():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__tail + 1) % self.__max_size
        if method == 'pop_front':
            return (self.__head + 1) % self.__max_size
        if method == 'pop_back':
            return (self.__tail - 1) % self.__max_size

    def push_front(self, x: int):
        if self.__is_full_queue():
            print(FullQueueError())
            return
        self.__head = self.__get_index('push_front')
        self.__elements[self.__head] = x
        self.__size += 1

    def push_back(self, x: int):
        if self.__is_full_queue():
            print(FullQueueError())
            return
        self.__tail = self.__get_index('push_back')
        self.__elements[self.__tail] = x
        self.__size += 1

    def pop_front(self):
        if self.__is_empty_queue():
            print(EmptyQueueError())
            return
        x: int = self.__elements[self.__head]
        self.__head = self.__get_index('pop_front')
        self.__size -= 1
        return x

    def pop_back(self):
        if self.__is_empty_queue():
            print(EmptyQueueError())
            return
        x: int = self.__elements[self.__tail]
        self.__tail = self.__get_index('pop_back')
        self.__size -= 1
        return x


def main():
    count_command = int(input())
    queue_size = int(input())

    deque = Deque(queue_size)
    commands = {
        'push_front': deque.push_front,
        'push_back': deque.push_back,
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
    }

    for _ in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            result = commands[operation](int(*value))
            if result is not None:
                print(result)
        else:
            result = commands[operation]()
            if result is not None:
                print(result)


if __name__ == '__main__':
    main()