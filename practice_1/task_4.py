# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""
while True:
    number = input("Введите четырехзначное число: ")

    if (len(number) == 4):
        break
    else:
        print("Попробуй еще!")

sum_of_digit = 0
for digit in number:
    sum_of_digit += int(digit)

print("Сумма цифр числа {}: {}".format(number, sum_of_digit))
