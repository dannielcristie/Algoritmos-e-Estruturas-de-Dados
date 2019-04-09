#coding=utf-8
print('''
5) Exercício - Nome na vertical em escada.
Modifique o programa anterior de forma a mostrar o nome em formato de escada.
Digite seu nome: FULANO

F
FU
FUL
FULA
FULAN
FULANO
''')
name = input('Digite o nome:\t')
cont=1
for i in range(len(name)):
	print(name[:cont])
	cont+=1
