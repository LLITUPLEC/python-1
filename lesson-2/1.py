# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
new_list = ['a', 123, False, 3.3, (1, 'два'), {'урок': 2, 'задание': 1}, [1, 2]]
for el in new_list:
    print(f'У элемента "{el}" тип данных - {type(el)}')

