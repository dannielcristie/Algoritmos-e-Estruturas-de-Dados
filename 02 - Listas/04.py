#coding=utf-8
'''
4) Dada uma lista L de números inteiros, escreva uma função que imprima os itens de L de trás para frente,
sem utilizar reverse().

'''
def listainversa(lista):
    l=[x for x in range(-1,-int(len(lista))) ]
    return(l)
    
print(listainversa([1,2,3,4,5,6,7,8,9]))    