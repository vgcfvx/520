#!/usr/bin/python3
numeros = [1,2,3,4,5,6,7,8,9,10,11,98989]
par =[]
impar=[]
for x in numeros:
    
    controle = x%2
    if(controle == 0):
        par.append(x)
    else:
        impar.append(x)

print(numeros)
print(par)
print(impar)        