
__author__ = 'Чирков Тимур Романович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = input('Введите произвольное целое число: \n')

i = len(number)
num = ''

while i > 0:
    if i == 1:
        num += number[i - 1]
    else:
        num += number[i - 1] + ' '
    i -= 1

print('Результат: ', num)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

var_a = input("Введите значение первой переменной var_a: ")
var_b = input("Введите значение второй переменной var_b: ")
var_c = var_a
var_d = var_b
var_a = var_d
var_b = var_c

print("Новое значение переменной var_a: " + var_a)
print("Новое значение переменной var_b: " + var_b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print("Доступ разрешен только лицам, старше 18 лет")
answer = ""
while answer != "Q":
    answer = input("Вам есть 18 лет (Y/N или Q для выхода)? \n")
    if answer == "Y":
        print("Доступ разрешен")
        break
    elif answer == "N":
        print("Доступ запрещен")
        break
    elif answer == "Q":
        print("До свидания!")
    else:
        print("Неверный ответ, введите Y/N или Q для выхода")
        continue
















