# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    if ndigits == 0:
        return number
    elif int(number) == 0:
        if number >= 0.5:
            number = 1
            return number
        else:
            number = 0
            return number
    else:
        number_f = number - int(number)
        number_f *= 10 ** (ndigits + 1)
        number_f = int(number_f)
        number_f /= 10
        if number_f - int(number_f) > 0.5:
            number_f = int(number_f) + 1
        else:
            number_f = int(number_f)
        number_f /= 10 ** ndigits
        number = int(number) + number_f
        return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    num = list(str(ticket_number))
    if len(num) < 6:
        luck = 'Номер билета не шестизначный'
        return luck
    if (int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5])):
        luck = True
        return luck
    else:
        luck = False
        return luck



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
