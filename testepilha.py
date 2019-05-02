#coding=utf-8
from estruturas import *
 
pilha1 = pilha()
pilha2 = pilha()


pilha1.empilhar(2)
pilha1.empilhar(3)
pilha1.empilhar(4)
pilha1.empilhar(4)

print(pilha1)

while not pilha1.vazia():
    print(pilha.topo())
    pilha2.empilhar(pilha1.desempilhar())


print(pilha1)