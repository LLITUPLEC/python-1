# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_number = int(input('Введите количество секунд, а мы его конвертируем: '))
hours = user_number // 3600
minuts = (user_number // 60) % 60
seconds = user_number % 60

print(f'{hours} часов {minuts} минут {seconds} секунд')
