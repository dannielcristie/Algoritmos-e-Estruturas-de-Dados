#coding=utf-8

class pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura =altura
    
    def envelhecer(self):
        if self.idade <21:
            self.altura = self.altura+0,05
        self.idade+=1
   
  def __str__(self):
      return '{}tem {}anos {} mede '
      
      
p1 = pessoa('Danniel',22,68,1.81)
print(p1)