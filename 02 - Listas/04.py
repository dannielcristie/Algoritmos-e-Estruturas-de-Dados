#coding=utf-8
'''
4) Dada uma lista L de números inteiros, escreva uma função que imprima os itens de L de trás para frente,
sem utilizar reverse().
'''

p = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

def listainversa(lista):
  L=[lista[::-1]]
  return(L)

print(listainversa(p))

