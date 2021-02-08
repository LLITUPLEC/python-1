"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
f = open('5-2.txt', 'r')
data = f.readlines()
f.close()
count_word = []
i = 1
with open('5-2.txt', 'r') as f:
    for line in f:
        count_word.append(f'{i}я строка - {len(line.split())}  слов(а)')
        i += 1
print(f"Количество строк в файле:  {len(data)}")
for p in count_word:
    print(p)

# Вариант с показом самой строки

# i = 0
# for p in count_word:
#     print(f'{p} = {data[i]}')
#     i += 1
