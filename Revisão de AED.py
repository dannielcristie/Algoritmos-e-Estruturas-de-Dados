#coding=utf-8

class Pilha:
	def __init__(self):
		self.items = []
	def __str__(self):
		return ','.join([str(i) for i in self.items])
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
	

class Fila:
	def __init__(self):
		self.items = []
	def __str__(self):
		return ','.join([str(i) for i in self.items])
	def enfileirar(self,item):
		self.items.insert(0,item)
	def desenfileirar(self):
		return self.items.pop()
	def vazia(self):
		return self.items == []
	def frente(self):
		return self.items[0]
	def tamanho(self):
		return len(self.items)
	def inverte(self):
		pilha = Pilha()
		while not self.vazia():
			pilha.empilhar(self.desenfileirar())
		while not pilha.vazia():
			self.enfileirar(pilha.desempilhar())
	def inverter(self):
		p = Pilha()
		while not self.vazia():
			p.empilhar(self.desenfileirar())
		while not p.vazia():
			self.enfileirar(p.desempilhar())

class No:
	def __init__(self,valor):
		self.valor = valor
		self.proximo = None
	def setValor(self,novo_valor):
		self.valor = novo_valor
	def setProximo(self, proximo):
		self.proximo = proximo
	def getValor(self):
		return self.valor
	def getProximo(self):
		return self.proximo

class ListaNaoordenada:
	def __init__(self):
		self.inicio = None
	def vazia(self):
		return self.inicio == None
	def Inserir(self,item):
		temp = No(item)
		temp.getProximo(self.inicio)
		self.inicio = temp
	def Buscar(self,item):
		atual = self.inicio
		encontrou =  False
		while atual != None and not encontrou:
			if atual.getValor() == item:
				encontrou =  True
			else:
				atual = atual.getProximo()
		return encontrou
	def Tamanho(self):
		atual = self.inicio
		contador = 0
		while atual != None:
			contador +=1
			atual = atual.getProximo()
		return contador
	def Imprimir(self,item):
		atual = self.inicio
		while atual != None:
			print(atual.getValor())
			atual = atual.getProximo()
		return

    def Remover(self,item):
    	if self.inicio.getValor() == item:
    		self.inicio = self.inicio.getProximo()







l1 =  ListaNaoordenada()

l1.Inserir(3)
l1.Inserir(5)
l1.Inserir(6)
l1.Inserir(9)
l1.Inserir(7)

print(l1)











'''
n1 = No(1)
n2 = No(2)

n1.setProximo(n2)


print(n1.getProximo())

'''

'''
f1 = Fila()

f1.enfileirar(1)
f1.enfileirar(2)
f1.enfileirar(3)
f1.enfileirar(4)
f1.enfileirar(5)

print(f1,'\n')

f1.inverter()

print(f1) 

'''

'''

f1.desenfileirar()
f1.desenfileirar()
f1.desenfileirar()
f1.desenfileirar()


print(f1.tamanho())

print(f1.vazia())

print(f1.frente())
'''




'''

p1 = Pilha()

p1.empilhar(1)
p1.empilhar(2)
p1.empilhar(3)
p1.empilhar(4)
p1.empilhar(5)
p1.empilhar(0)

print(p1)  


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




