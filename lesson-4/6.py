"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
"""
from itertools import count, cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    elem = cycle(my_list)
    while i < iteration:
        print(next(elem))
        i += 1


my_count_func(start_number=int(input("Введите стартовое число: ")), stop_number=int(input("Введите финишное число: ")))
my_cycle_func(my_list=[True, 'ABC', 123, None], iteration=int(input("Введите итерацию: ")))
