#coding=utf-8
'''
7) Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P com os valores ordenados de P,
agrupados em números pares primeiro e ímpares depois.
'''
def impar_par(lista):
	L=[]
	for index, valor in enumerate(lista):
		if valor%2==0:
			L.insert(0,valor)
		else:
			L.append(valor)
			
	return(L)
		
l = [1,3,5,7,9,2,4,6,8,0]
print(impar_par(l))
		
