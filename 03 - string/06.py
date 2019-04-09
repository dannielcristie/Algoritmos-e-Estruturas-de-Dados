#coding=utf-8
print(
'''
6) Exercício - Nome na vertical em escada invertida
Altere o programa anterior de modo que a escada seja invertida.
Digite seu nome: FULANO
FULANO
FULAN
FULA
FUL
FU
F
''')

name = input('Digite o nome:\t')
cont=len(name)		
while(cont>=1):
	print(name[:cont])
	cont-=1
