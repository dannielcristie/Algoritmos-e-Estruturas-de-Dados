# coding=utf-8
'''
Escreva um programa que calcule e mostre o seno dos ângulos entre 0 e 360 (de 10 em 10).
dica: Use a função sin do pacote math

'''
#ASCII

import math

for x in range(1,360,10):
    print(math.sin(x))