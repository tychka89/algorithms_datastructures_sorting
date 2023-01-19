'''
Заботливая мама

Мама Васи хочет знать, что сын планирует делать и когда.
Помогите ей: напишите функцию solution,
определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке,
если значение присутствует. Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка и искомый элемент,
а возвращает целое число — индекс найденного элемента или -1.

Формат ввода
Функция на вход принимает голову односвязного списка и элемент, который нужно найти.
Длина списка не превосходит 10000 элементов. Список не бывает пустым.

Формат вывода
Функция возвращает индекс первого вхождения искомого элемента в список (индексация начинается с нуля).
Если элемент не найден, нужно вернуть -1.
'''

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

def solution(node, elem):
    # Your code
    index = 0
    while node:
        if node.value == elem:
            return index
        node = node.next_item
        index += 1
    return -1

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2

if __name__ == '__main__':
    test()