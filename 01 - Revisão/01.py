# coding=utf-8
'''
Escreva um programa que escolha aleatoriamente um numero entre 0 e 10, ao qual o usuário deve tentar adivinhar.
O jogo acaba quando o usuário acerta ou quando ele desiste (digitando 0).

'''
#ascii

import random

print('\tAdivinhe o numero entre 1 e 10.\n\tPara desistir basta aperta 0\n\n')
numeroaleatorio = random.randint(1,10)

while 1>0:
    n = int(input('Digite o numero: '))
    if numeroaleatorio == n:
        print('Você acertou! Parabens.')
        break
    elif n == 0:
        print('Você desistiu')
        break
    else:
        print(' Errou, tente novamente.')
    