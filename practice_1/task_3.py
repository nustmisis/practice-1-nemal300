# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = input()
height = input()

#Ваш код

print("Индекс тела: {}".format(float(weight)/float(height)**2))

