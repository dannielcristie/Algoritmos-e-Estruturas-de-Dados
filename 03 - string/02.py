#coding=utf-8
'''
2) Exercício - Separação de String
Elabore um script que leia o nome completo de uma pessoa e imprima o prenome e o sobrenome


----

prenome
substantivo masculino
nome de um indivíduo, que antecede o nome de família; nome de batismo, antenome.
"Rui é prenome de Rui Barbosa"

'''


nome =input('Escreva seu nome: ')
lname = nome.split(' ')

print('Nome: ',lname[0],'\nSobrenome: ',' '.join(lname[1:]))
