'''
	Crie um programa que, usando agendaionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. Leia os dados (nome, telefone) de todos os contatos do usuário de forma que a agenda fique completa e permita imprimir todos os contatos. Por fim, faça uma pesquisa pelo nome e apresente o telefone.
'''




agenda = {}

def addctt():
	n = int(input('Deseja adicionar quantos contatos:\t'))
	for i in range(n):
		name_add = input('Digite o nome:')
		phone = int(input('Digite o nome:'))
		agenda[name_add] = phone
	return()

def seachctt():
	name_seach = input('Digite o nome quem deseja procura:\t')
	print(agenda[name_seach])		
	return()

def showctt():
	for i in agenda:
		if i in agenda:
			print(i,agenda[i])
		elif agenda == 0:
			print('Agenda vazia')
		else:
			print("Contato não encontrado!")
	return()
def menu():
	print('''
		Agenda:
	Menu:
	1 - Adicionar contato
	2 - Procura contato
	3 - Mostra agenda
	''')

while True:
	menu()
	opc = int(input('Digite o numero correspodente:\t'))
	if opc == 1:
		addctt()
	elif opc ==2:
		seachctt()
	elif opc ==3:
		showctt()
	elif opc>=4 or opc<=0:
		print('Opcão invalida')


