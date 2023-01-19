"""
Соседи

Дана матрица. Нужно написать функцию, которая для элемента возвращает
всех его соседей. Соседним считается элемент, находящийся от текущего
на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы
соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0.
А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй —
количество столбцов m. Числа m и n не превосходят 1000. В следующих n
строках задана матрица. Элементы матрицы — целые числа, по модулю не
превосходящие 1000. В последних двух строках записаны координаты элемента,
соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.

Пример
Ввод	            Вывод
4                   7 7
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
"""

from typing import List, Tuple


def calculate_distance(numbers: List[int], length_street: int) -> List[int]:
    distance = []
    zero_position = None
    for i, value in enumerate(numbers):
        if value == 0:
            zero_position = i
            distance.append(0)
            continue
        if zero_position is not None:
            distance.append(i - zero_position)
        else:
            distance.append(length_street)
    return distance


def nearest_zero(length_street: int, house_numbers: List[int]) -> List[int]:
    distance = calculate_distance(house_numbers, length_street)
    distance2 = (calculate_distance(house_numbers[::-1], length_street))[::-1]
    result = []
    for step in range(length_street):
        result.append(min(distance[step], distance2[step]))
    return result


def read_input() -> Tuple[int, List[int]]:
    length_street = int(input())
    house_numbers = [int(num) for num in input().split(' ')]
    return length_street, house_numbers


if __name__ == '__main__':
    length_street, house_numbers = read_input()
    print(' '.join([str(x) for x in nearest_zero(length_street, house_numbers)]))