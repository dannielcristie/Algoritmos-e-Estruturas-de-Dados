#coding=utf-8
from aula2304pilha import *

def somatodos(pilha):
    total = 0
    while pilha.tamanho() > 0:
        x  = pilha.desempilhar()
        total+=x
    return(total)
 
 
def somatodos2(pilha):
    total = 0
    while  not pilha.vazia() > 0:
        x  = pilha.desempilhar()
        total+=x
    
    return(total)


         
def somatodos3(pilha):
    elementos = []
    while not pilha.vazia() > 0:
        x  = pilha.desempilhar()
        elementos.append(x)
        
    return(sum(elementos))
    
        
        
def somapares(pilha):
    pass

p1 = Pilha()
p1.empilhar(1)
p1.empilhar(10)
p1.empilhar(20)
p1.empilhar(30)
p1.empilhar(40)
p1.empilhar(50)
p1.empilhar(60)

print(somatodos(p1))
print(somatodos2(p1))
print(somatodos3(p1))