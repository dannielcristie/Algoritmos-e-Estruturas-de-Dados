#coding=utf-8
'''
1) Exercício - Contagem de Ocorrências
A partir de um texto fornecido pelo usuário, conte o número de caracteres e quantos deles são vogais.
'''

text = (input('Digite um texto:\t')).lower()
n = len(text)
cont = 0
vogais = ['a','e','i','o','u']
for i in text:
    if i in vogais: 
        cont+=1
print('A quantidade de caracteres é:\t',n)
print('A quantidade de vogais é:\t',cont)
