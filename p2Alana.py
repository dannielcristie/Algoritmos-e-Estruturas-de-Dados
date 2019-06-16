from EstruturasDeDados import Fila
def atendimento():
	N = Fila()
	P = Fila()
	contN = 0
	contP = 0
	while  True:
		
		opc = int(input('''
			Retirada de senha:
			[1] Para prioridade
			[2] Para Normal
			[3] Para chamar atedimento
			==========================
			Digite a opção desejada: '''))

		if opc == 1:
			contP+=1
			P.enfileirar(contP)
			print('\t\tSua senha é {} P'.format(contP))
			print('\t\texistem {} Prioridade e {} Normal'.format(contP,contN))
		elif opc == 2:
			contN+=1
			N.enfileirar(contN)
			print('\t\tSua senha é {} N'.format(contN))
			print('\t\texistem {} Prioridade e {} Normal'.format(contP,contN))
		elif opc == 3:
			if P.vazia() and (not N.vazia()):
				print('\t\tatedimento a senha {} N'.format(N.desenfileirar()))
			elif not P.vazia():
				print('\t\tatedimento a senha {} P'.format(P.desenfileirar()))
			else:
				print('\t\tsem senha a ser chamada')
		else:
			print('\t\topção invalida.')


atendimento()