'''
Генератор скобок

Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях (ПСП),
состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —–
алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.
Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП в нужном порядке.

Рассмотрим второй пример. Надо вывести ПСП из четырёх символов.
Таких всего две:
(())
()() (()) идёт раньше ()(), так как первый символ у них одинаковый,
а на второй позиции у первой ПСП стоит (, который идёт раньше ).

Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной длины
в алфавитном (лексикографическом) порядке.

Пример
Ввод
3

Вывод
((()))
(()())
(())()
()(())
()()()
'''

def gen_brackets(count, prefix='', left=0, rigth=0):
    if left == count and rigth == count:
        print(prefix)
    else:
        if left < count:
            gen_brackets(count, prefix + '(', left + 1, rigth)
        if rigth < left:
            gen_brackets(count, prefix + ')', left, rigth + 1)

if __name__ == '__main__':
    n = int(input())
    gen_brackets(n)