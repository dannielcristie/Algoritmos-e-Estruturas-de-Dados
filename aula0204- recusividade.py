#coding=utf-8

'''
def S(n):
  soma=0
  for v in range(1, n+1):
    soma+=v
  return soma
n = int(input('Informe um valor positivo'))
if n >0: print(S(n))
'''
'''
def S(n):
  if n!=1: return n+S(n-1)
  else: return n

n = int(input('Informe um valor positivo'))
if n >0: print(S(n))
'''

