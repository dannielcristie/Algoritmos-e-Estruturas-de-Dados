from EstruturasDeDados import Pilha

p1 = Pilha()
p2 = Pilha()


p1.empilhar(3)
p1.empilhar(4)
p1.empilhar(4)
p1.empilhar(4)
p1.empilhar(5)
p1.empilhar(10)

p2.empilhar(3)
p2.empilhar(4)
p2.empilhar(4)
p2.empilhar(4)
p2.empilhar(5)
p2.empilhar(100)


'''
def maior_de_pilha(p1):
	maior = p1.topo()

	while not p1.vazia():
		num = p1.desempilhar()
		if num > maior:
			maior = num
	return maior



print(maior_de_pilha(p1))
'''

'''

def Pilhas_iguais(p1,p2):
	if p1.tamanho()!= p2.tamanho():
		return False	

	while not p1.vazia():
		num1 = p1.desempilhar()
		num2 = p2.desempilhar()
		if num1 != num2:
			return False
		else:
			return True



print(Pilhas_iguais(p1,p2))
'''

'''
def TPilha(lista):
	 
	p1 = Pilha()
	if len(lista) != 15:
		print('sem itens suficiente!')

	else:
		for item in lista:
			if item % 2 == 0:
				 
				p1.empilhar(item)
			else:
				if not p1.vazia():
					p1.desempilhar()
	
	while not p1.vazia():
		print(p1.desempilhar())



	
l = [ i for i in range(0,15)]

print(TPilha(l))
'''



class Aviao:
	def __init__(self,cia,modelo,ano):
		self.cia = cia
		self.modelo = modelo
		self.ano = ano
	def __str__(self):
		return '{}-{}-{}'.format(self.cia,self.modelo,self.ano)

av1 = Aviao()
av2 = Aviao()



















