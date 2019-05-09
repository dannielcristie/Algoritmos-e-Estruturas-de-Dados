from EstruturasDeDados import *


                #pilha
'''
p1 = Pilha()

p1.empilhar('danniel')
p1.empilhar('cristie')
p1.empilhar('matos')
p1.empilhar('da')
p1.empilhar('silva')

print(p1)
print(p1.tamanho())

print('quem ta no topo é: {} ' .format(p1.topo()))


p1.desempilhar()
p1.desempilhar()
p1.desempilhar()
p1.desempilhar()
p1.desempilhar()

print(p1.vazia())

'''

###########################################
                 #fila


f1=Fila()

f1.enfileirar(1)
f1.enfileirar(2)
f1.enfileirar(3)
f1.enfileirar(4)
f1.enfileirar(5)
f1.enfileirar(6)

print(f1)
print(f1.tamanho())
f1.inverte()
print('inversão 1 : {}'.format(f1))
f1.inverte()
print('inversão 2 : {}'.format(f1))

f1.desenfileirar()
f1.desenfileirar()
f1.desenfileirar()
f1.desenfileirar()
f1.desenfileirar()
f1.desenfileirar()

f1.vazia()
print(f1.tamanho())

f1.reduz_para_n(3)
print(f1)

























