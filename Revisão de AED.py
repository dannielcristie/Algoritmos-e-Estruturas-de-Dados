#coding=utf-8
from random import *
from EstruturasDeDados import *

class Pilha:
	def __init__(self):
		self.items = [] 
	def empilhar(self,valor):
		self.items.append(valor)
	def desempilhar(self):
		return self.items.pop()
	def tamanho(self):
		return len(self.items)
	def vazia(self):
		return self.items == []
	def topo(self):
		return self.items[-1]
	def buscar(self, valor):
		for i in self.items:
			if self.items[i] == valor:
				print(i)
	def __str__(self):
		pilha = ''
		for item in self.items:
			pilha += str(item)  + ','    
		return pilha

'''

p1 = Pilha()

p1.empilhar(1)
p1.empilhar(2)
p1.empilhar(3)
p1.empilhar(4)
p1.empilhar(5)
p1.empilhar(0)

p1.buscar(0)



print(p1.tamanho())

print(p1.topo())


p1.desempilhar()
p1.desempilhar()
p1.desempilhar()
p1.desempilhar()

print(p1.tamanho())

print(p1.topo())
'''


#Escreva uma função em Python que receba uma sequência
# de parênteses e colchetes e retorne True se ela está 
# bem formada ou False, caso contrário.
'''

def sequencia(lista):
	p_aux = Pilha()
	for i in lista:
		if i == '(' or '[' or '{':
			p_aux.empilhar(i)
		elif i == ')' or ']' or '}':
			p_aux.desempilhar()
	if p_aux.vazia():
		return print('Bem formada')
	else:
		return print('Mal formada')

l = ['(){[]']
print(sequencia(l))
'''
'''
def formacao(lista):
	p_aux = Pilha()
	valida = True
	for i in lista:
		if i == '(' or '[' or '{':
			p_aux.empilhar(i)
		elif i == ')' or ']' or '}':
			top = p_aux.desempilhar()
			if not (top == '(' and i ==')' or top== '[' and i ==']' or top== '{' and i =='}') == True:
				valida = False
				break 
				
	if p_aux.vazia():
		return print('Bem formada')
	else:
		return print('Mal formada')


l = ['()[{}]']
print(formacao(l))

'''

'''
#aula do dia 16/05/2019
class nListaNaoOrdenada:
	def  MediaValorAcima(self):
		atual = self.inicio
		soma = 0 
		while atual.getProximo() != None:
			soma = soma + atual.getValor()
			atual = atual.getProximo()
		
		if not self.vazia():
			media  = (soma/self.tamanho())
		
		
		return media
		
		
l1 = nListaNaoOrdenada()

l1.Inserir(20)
l1.Inserir(20)
l1.Inserir(20)
l1.Inserir(10)
l1.Inserir(10)

print(l1.MediaValorAcima())

'''
'''
#Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha. 

def maior_da_pilha(p1):
	maior = p1.topo()

	while not p1.vazia():
		num =  p1.desempilhar()
		if num > maior:
			maior = num

	return maior

p1 = Pilha()

p1.empilhar(2)
p1.empilhar(150)
p1.empilhar(20)
p1.empilhar(100)
p1.empilhar(26)

print(maior_da_pilha(p1))
'''

'''
#Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem. 

def pilhas_iguais(p1,p2):
	if p1.tamanho() != p2.tamanho():
		return False
	while not p1.vazia():
		num1 = p1.desempilhar()
		num2 = p2.desempilhar()
		if num1 != num2:
			return False
		else:
			return True


p1 = Pilha()
p2 = Pilha()

p1.empilhar(2)
p1.empilhar(150)
p1.empilhar(20)
p1.empilhar(100)
p1.empilhar(26)


p2.empilhar(2)
p2.empilhar(150)
p2.empilhar(20)
p2.empilhar(100)
p2.empilhar(265)



print(pilhas_iguais(p1,p2))
'''
'''

#Construa um programa utilizando uma pilha que resolva o seguinte problema: Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. Dado uma placa verifique se o carro está estacionado na rua. Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair. 


def Rua():
	placas = Pilha()
	n = int(input('Digite a quantidade de carros que cabem na rua: '))
	
	for i in range(0,n):
		placa = int(input('Digite a placa do carro: '))
		placas.empilhar(placa)

	print('\n\tCarros estacionados:', placas)
	return placas	


def estaciomento(p1):
	print('#'*40)
	placa = int(input('Digite a placa a buscar '))
	p_aux = Pilha()


	while not p1.vazia():
		num = p1.desempilhar()	
		if num != placa:
			p_aux.empilhar(num)
			if p1.vazia() == True:
				print('\n\tplaca não encontrada.')
		else:
			break
			if p_aux.vazia() == False:
				print('\n\tCarros que precisam sair:', p_aux)
			else:
				print('\n\tnão precisa tira nenhum carro.')


estaciomento(Rua())
'''

'''
# Implemente uma função chamada TPilha, que receba uma lista de inteiros com 15 elementos.

#Para cada um deles, como segue:

    #se o número for par, insira-o na pilha;
    #se o número lido for ímpar, retire um número da pilha;
    #Ao final, esvazie a pilha imprimindo os elementos.


def TPilha(lista):
	p1 = Pilha()
	for i in lista:
		if i % 2 == 0: 
			p1.empilhar(i)
		
		else:
			if p1.vazia() == True:
				continue
			else:
				p1.desempilhar()
	while not p1.vazia():
		print(p1.desempilhar())
	return 

l = [2,4,6,8,1]

print(TPilha(l))

'''

'''
#Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um:

    #se positivo, inserir na pilha P;
    #se negativo, inserir na pilha N;
    #se zero, retirar um elemento de cada pilha

def TPilha2(p,n,vec):
	P = Pilha()
	N = Pilha()
	for i in vec:
		if i > 0:
			P.empilhar(i)
		
		if i < 0:
			N.empilhar(i)

		if i == 0:
			if P.vazia() == True:
				N.desempilhar()
			elif N.vazia == True:
				P.desempilhar()
			elif N.vazia() and P.vazia() == True:
				break
				continue
			else:
				P.desempilhar()
				N.desempilhar()
	print('\n',P)
	print('\n',N)
	return print(' ')

p1 = Pilha()
p2 = Pilha()

p1.empilhar(1)
p1.empilhar(11)
p1.empilhar(111)

p2.empilhar(2)
p2.empilhar(22)
p2.empilhar(222)

v = [-1,-2,-3,-4,-5,-6,1,2,3,0,4,5,6,0]

print(TPilha2(p1,p2,v))

'''

#Implemente uma o jogo de baralho 21 usando uma fila para o baralho


def menu():
	opc_m = int(input('''
			Bem-vindo ao 21 do Danniel!
		1 - Novo jogo


		Digite a opcão correspondente:\t'''))


def carta():
ouros = []
paus = []
copas = []
espadas []
for i in range(1,11):	
	paus.append('Pau '+str(i))
for i in range(1,11):	
	ouros.append('Ouro '+str(i))
for i in range(1,11):	
	copas.append('Copa '+str(i))
for i in range(1,11):	
	espadas.append('Espada '+str(i))



def Jogo():
	opc_j = int(input('''
		1 - Pega uma carta
		2 - Para

		Digite :'''))
	if 



while True:
	menu()






