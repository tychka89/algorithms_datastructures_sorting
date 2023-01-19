#79891378
from typing import List

# я поменяла способ выбора опорного элемента
# но стало только медленнее)))
# решила оставить так, чтобы продемонстировать проделанную работу)
def partition(players: List, left: int, right: int) -> int:
    pivot = players[(right + left) // 2]
    i = left
    j = right - 1
    while True:
        if i == j and players[j] == pivot:
            return j
        if (i <= j and players[j] > pivot):
            j -= 1
        elif (i <= j and players[i] < pivot):
            i += 1
        elif (players[j] > pivot) or (players[i] < pivot):
            continue
        if i <= j:
            players[i], players[j] = players[j], players[i]
        else:
            players[left], players[j] = players[j], players[left]
            return j

def quick_sort_effective(players: List, left: int, right: int) -> None:
    if ((right - left) > 1):
        p = partition(players, left, right)
        quick_sort_effective(players, left, p)
        quick_sort_effective(players, p + 1, right)

def transformation(players: List) -> List:
    players[1] = - int(players[1])
    players[2] = int(players[2])
    return [players[1], players[2], players[0]]

if __name__ == '__main__':
    n = int(input())
    players = [transformation(input().split()) for _ in range(n)]
    left = 0
    quick_sort_effective(players, left, len(players))
    print(*(list(zip(*players))[2]), sep="\n")