#coding=utf-8
def pares(lista):
    p =[x for x in lista if x%2==0]
    return(p)


print(pares([1,2,3,4,5,6,7,8,9,10,11]))