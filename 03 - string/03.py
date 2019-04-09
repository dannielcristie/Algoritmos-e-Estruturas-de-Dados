#coding=utf-8
'''
3) Exercício - Inversão Maiuscula
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
Exemplo:
Entrada de dados: Alana
Saída de dados: ANALA

'''
name = str(input('Digite o seu nome:\t')).upper()
print(name[::-1])
