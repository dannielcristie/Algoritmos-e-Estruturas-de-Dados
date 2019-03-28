#coding=utf-8
'''
2) Dada uma lista L de números inteiros, escreva uma função que imprima todos os números de índices múltiplos de 3.

'''
def indicesmult3(lista):
    L = [ x for e in lista if lista[x]%3 == 0]
    return(L)

print(indicesmult3([1,2,3,4,5,6,7,8,9]))