#coding=utf-8
'''
8) Faça um programa que leia duas listas com 10 elementos cada.
Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados das duas outras listas

'''

def listaintercalada(lista1,lista2):
	L = []
	for i in range(len(lista1)):
	  L.append(lista1[i])
	  L.append(lista2[i])
	return(L)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [11,22,33,44,55,66,77,88,99,1010]
print(listaintercalada(l1,l2))
