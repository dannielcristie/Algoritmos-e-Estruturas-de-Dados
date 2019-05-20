	#coding=utf-8
from random import *
from EstruturasDeDados import *

#Implemente uma o jogo de baralho 21 usando uma fila para o baralho


def menu():
	opc_m = int(input('''
			Bem-vindo ao 21 do Danniel!
		1 - Novo jogo


		Digite a opcão correspondente:\t'''))
	if opc_m == 1:
		Novo_Jogo()




def cartas():
	baralho = []
	card = ['Rei de ','Dama de ', 'Valete de ']
	naipe = ['Ouro','Pau','Copa','Espada']
	
	for i in range(1,11):	
		baralho.append('Pau '+str(i))
	for i in range(1,11):	
		baralho.append('Ouro '+str(i))
	for i in range(1,11):	
		baralho.append('Copa '+str(i))
	for i in range(1,11):	
		baralho.append('Espada '+str(i))
	for i in card:
		for j in naipe:
			baralho.append(i+j)





def Novo_Jogo():
	opc_j = int(input('''
		1 - Pega uma carta
		2 - Para

		Digite :'''))
	if opc_j == 1:
		print('\tbaralho\n'*20)
	elif opc_j == 2:
		menu()
	else:
		print('\topcão invalida.')



while True:
	menu()



