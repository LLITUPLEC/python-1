# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите число: '))
num = user_number
max_from_x = 0
while user_number > 0:
    n = user_number % 10
    if n >= max_from_x:
        max_from_x = n
    user_number = user_number // 10
print(f'Максимальная цифра в числе {num} - {max_from_x}')
