"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
x = 0
with open('5-5.txt', 'w') as f:
    a = [i for i in range(1, random.randrange(1, 15))]
    for el in a:
        f.write(f'{el}\n')
with open('5-5.txt', 'r') as f:
    data = f.readlines()
print(data)
sum = 0
for n in data:
    sum += int(n)
print(sum)
