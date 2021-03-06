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
            while(self.tamanho()!= n):
                self.desenfileirar()
        
    def __str__(self):
        return self.items


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    def setValor(self, novo_valor):
        self.valor = novo_valor
    def setProximo(self, proximo):
        self.proximo = proximo
    def getValor(self):
        return self.valor
    def getProximo(self):
        return self.proximo
        

class ListaNaoOrdenada:
    def __init__(self):
        self.inicio = None
        
    def vazia(self):
        return self.inicio == None
        
    def Inserir(self, item):
        temp = No(item)
        temp.setProximo(self.inicio)
        self.inicio = temp 
        
    def Buscar(self, item):
        atual = self.inicio
        encontrou = False
        while atual != None and not encontrou:
            if atual.getValor() == item:
                encontrou = True
            else:
                atual = atual.getProximo()
        return encontrou
        
    def Remover(self,item):
        # se o item a ser removido for o primeiro
        if self.inicio.getValor() = item:
            self.inicio = self.inicio.getProximo()
        else:
            atual = self.inicio
            previo = None
            removido = False
            while atual != None:
                if atual.getValor() =  item:
                    previo = atual
                    atual = atual.getProximo()
                else:
                    previo.setProximo() = atual.getProximo()
                    removido = True
    
class ListaOrdenada:
    def __init__(self):
        self.inicio = 
    
    def Inserir(self, item):
        atual = self.inicio
        previo = None
        parar = False
        while atual != None and not parar:
            if atual.getValor() > item:
                parar = True
            else:
                previo = atual
                atual = atual.getProximo()
        
        temp = No(item)
 

        
def separa(lista, n):
    atual = self.inicio
    temp  = ListaNaoOrdenada()
    separou = False
    
    while atual.getProximo() != None and not separou:
        if atual.getProximo() == n:
            temp.inicio = atual.getProximo()
            atual.setProximo(None)
            separou = True
        else:
            atual = atual.getProximo()
        
    
    return lista, temp