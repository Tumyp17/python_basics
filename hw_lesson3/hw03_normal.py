# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_list = [1, 1]
    i = 1
    while i <= (m - 2):
        num_add = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
        fib_list.append(num_add)
        i += 1
    if n == 0 or n == 1:
        print(fib_list)
        return fib_list
    i = 1
    while i <= n:
        fib_list.remove(fib_list[0])
        i += 1
    print(fib_list)
    return fib_list

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    i = 1
    attempt = 0
    n = len(origin_list)
    max_attempts = ((n - 1) * (n // 2) * 2)
    while attempt < max_attempts:
        if origin_list[i - 1] > origin_list[i]:
            origin_list[i - 1], origin_list[i] = origin_list[i], origin_list[i - 1]
            if i == n - 1:
                origin_list[i], origin_list[n - 1] = origin_list[n - 1], origin_list[i]
                i = 0
        if i == n - 1:
            i = 0
        i += 1
        attempt += 1
    print(origin_list)
    return origin_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(word, list):
    new_list = []
    if not word in list:
        return list
    else:
        i = 0
        while i <= len(list) - 1:
            if list[i] == word:
                new_list.append(word)
            i += 1
    return new_list

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def check_dots(a, b, c, d):
    check = False
    if (a[0] + b[0]) / 2 is (c[0] + d[0]) / 2:
        if (a[1] + b[1]) / 2 is (c[1] + d[1]) / 2:
            check = True
    if (a[0] + d[0]) / 2 is (b[0] + c[0]) / 2:
        if (a[1] + d[1]) / 2 is (b[1] + c[1]) / 2:
            check = True
    if (a[0] + c[0]) / 2 is (d[0] + b[0]) / 2:
        if (a[1] + c[1]) / 2 is (d[1] + b[1]) / 2:
            check = True
    if (b[0] + a[0]) / 2 is (d[0] + c[0]) / 2:
        if (b[1] + a[1]) / 2 is (d[1] + c[1]) / 2:
            check = True
    if (b[0] + c[0]) / 2 is (a[0] + d[0]) / 2:
        if (b[1] + c[1]) / 2 is (a[1] + d[1]) / 2:
            check = True
    if (b[0] + c[0]) / 2 is (a[0] + d[0]) / 2:
        if (b[1] + c[1]) / 2 is (a[1] + d[1]) / 2:
            check = True
    if (c[0] + a[0]) / 2 is (b[0] + d[0]) / 2:
        if (c[1] + a[1]) / 2 is (b[1] + d[1]) / 2:
            check = True
    if (c[0] + b[0]) / 2 is (a[0] + d[0]) / 2:
        if (c[1] + b[1]) / 2 is (a[1] + d[1]) / 2:
            check = True
    if (c[0] + d[0]) / 2 is (a[0] + b[0]) / 2:
        if (c[1] + d[1]) / 2 is (a[1] + b[1]) / 2:
            check = True
    if (d[0] + a[0]) / 2 is (b[0] + c[0]) / 2:
        if (d[1] + a[1]) / 2 is (b[1] + c[1]) / 2:
            check = True
    if (d[0] + b[0]) / 2 is (a[0] + c[0]) / 2:
        if (d[1] + b[1]) / 2 is (a[1] + c[1]) / 2:
            check = True
    if (d[0] + c[0]) / 2 is (a[0] + b[0]) / 2:
        if (d[1] + c[1]) / 2 is (a[1] + b[1]) / 2:
            check = True
    return check

a1 = (-3, 11)
a2 = (12, -4)
a3 = (1, -7)
a4 = (-14, 8)

z = check_dots(a1, a2, a3, a4)

print(z)
