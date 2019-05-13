#coding=utf-8

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







	