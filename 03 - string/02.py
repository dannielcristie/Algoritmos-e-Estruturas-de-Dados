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

name = input('Digite seu nome:\t').lower()
cont = 0
l = []
for i in name:
    if i ==' ':
        cont+=1
        l.append(name[i])
        i = cont
        
print(cont)
print(name)
print(type(i))
print(l)