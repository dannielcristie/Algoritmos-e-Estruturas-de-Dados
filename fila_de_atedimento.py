from EstruturasDeDados import Fila

def Menu():
	N = Fila()
	P = Fila()
	contN = 0
	contP = 0
	while True:
		opc = int(input('''
			1 - Senha Normal
			2 - Senha Prioridade
			3 - Atedimento
			Digite a opção desejada:\t'''))
		
		if opc == 1:
			contN += 1
			N.enfileirar(contN)
			print('Sua senha é a {}N'.format(contN))


		elif opc == 2:
			contP +=1
			P.enfileirar(contP)
			print('Sua senha é a {}P'.format(contP))
			
		
		elif opc == 3:
			if (P.vazia()) and (not N.vazia()):
				print('Atedimento á senha`{}N'.format(N.desenfileirar()))
				

			elif not P.vazia():
				print('Atedimento à senha{}N'.format(P.desenfileirar()))
				
			
			else:
				print('Sem senha a serem chamadas')
				
		else:
			print('Opção inválida') 

			


Menu()









