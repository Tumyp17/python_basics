__author__ = 'Чирков Тимур Романович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit_list = []

# Решил сделать программу, которая берет у пользователя произвольный список, а не с уже данным списком

answer = 0
i = 0
max_list = 5
user_name = input('Введите свое имя: \n')

input(user_name + '! Данная программа нумерует список фруктов, введите что-нибудь для продолжения: \n')

while answer != 'N':
    user_input = input('Введите название фрукта, для добавления его в список: \n')
    fruit_list.append(user_input)
    answer = input('Хотите добавить еще значение в список? Если нет, введите N: \n')
    i += 1
    if i == max_list:
        print('Длина списка достигла максимального значения, переходим к следующей части программы')
        break

for idx, itm in enumerate(fruit_list, 1):
    print(f'{idx}: {itm.rjust(10)}')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = [1, 2, 3, 4, 5, 7, 9, 10, 11, "яблоко"]
second_list = [2, 3, 4]
third_list = []
for i in first_list:
    if not (i in second_list):
        third_list.append(i)

print(third_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Фразу "Дан произвольный список из целых чисел" воспринимаю буквально, что он действительно дан, а не я его создал

import random

num_list = []
num_list2 = []

n = int(random.uniform(5, 10))
i = 0
while i < n:
    num_list.append(int(random.uniform(0, 100)))
    i += 1
print(num_list)

for itm in num_list:
    if itm % 2 == 0:
        itm /= 2
        num_list2.append(int(itm))
    else:
        itm *= 2
        num_list2.append(int(itm))

print(num_list2)
