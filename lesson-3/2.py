"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def my_func(fname, surname, byear, city, email, phone):
    print(fname, surname, byear, city, email, phone)


my_func(fname='nik', surname='evt', byear=1991, city='Astr', email='tminn91@mail.ru', phone='9999999')
