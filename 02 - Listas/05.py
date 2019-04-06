#coding=utf-8
'''
5) 
Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P contendo os itens de L sem repetição
'''
def removerepetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

print('lista:\n',lista)

print('Sem os repetidos:\n',removerepetidos(lista))
