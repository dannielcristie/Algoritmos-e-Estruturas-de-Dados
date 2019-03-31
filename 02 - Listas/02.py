#coding=utf-8
'''
2) Dada uma lista L de números inteiros, escreva uma função que imprima todos os números de índices múltiplos de 3.
'''

def indicesmult3(lista):
    l = [ item for item in range(len(lista)) if (int(lista[item])%3==0)]
    return(l)
    
indicesmult3([0,2,5,3,4,8])