# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = input('Введите число, а мы просуммируем его в формате n + nn + nnn: ')
double = (user_number * 2)
triple = (user_number * 3)
s8um_arg = int(user_number) + int(double) + int(triple)
print(f'Сумма чисел {user_number} + {double} + {triple} = {sum_arg}')
