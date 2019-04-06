#coding=utf-8
'''
6) Dada uma lista L de números inteiros, escreva uma função que imprima os índices de todas as
ocorrências de um número especificado.

'''
def indice_especifico(lista,n):
	for indice, valor in enumerate(lista):
		lista[indice]+=1
		if valor == n:
			print ("O numero: %d ocorre no indice = %d" % (valor, indice))
	return('\n')	
			
l = [0,1,3,3,3,3,4,8,44,3,3]
print(indice_especifico(l,3))
