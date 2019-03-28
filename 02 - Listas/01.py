#coding=utf-8
'''
1) Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P contendo os números pares de L.
Observação: utilize criação implícita de listas.
'''

def pares(lista):
    p =[x for x in lista if x%2==0]
    return(p)


print(pares([1,2,3,4,5,6,7,8,9,10,11]))