#coding=utf-8


class Pilha:
    def __init__(self):
        self.items = []
    def empilhar(self, valor):
        self.items.append(valor)
    def desempilhar(self):
        return self.items.pop()
    def tamanho(self):
        return len(self.items)
    def vazia(self):
        return self.items == []
    def topo(self):
        return self.items[-1]
   

class Fila:
    def __init__(self):
        self.items = []
    def enfileirar(self, item):
        self.items.insert(0, item)
    def desenfileirar(self):
        return self.items.pop()
    def tamanho(self):
        return len(self.items)
    def vazia(self):
        return self.items == []
    def frente(self):
        return self.items[-1]
    def inverter(self):
        pilha = Pilha()
        while not self.vazia():
            pilha.empilhar(self.desenfileirar())
        
        while not pilha.vazia():
            self.enfileirar(pilha.desempilhar())
    def reduz_para_n(self,n):
        if self.tamanho() >+n:
            while(self.tamanho()!= n)
        
        
            
    def __str__(self):
        return self.items

        
    