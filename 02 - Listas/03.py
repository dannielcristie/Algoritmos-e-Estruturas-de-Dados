#coding=utf-8
'''
3) Dada uma lista L de números inteiros, escreva uma função retorne uma lista P contendo todos os itens de
L acrescidos em 10%

'''
def dezporc(lista):
    l=[ x+(x*0.10) for x in lista]
    return(l)
p =[10,20,30,40,50,60,70]
print(p,dezporc(p))