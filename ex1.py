#!/usr/bin/python3
x='oi'
while(x!='sair'):
    x= input('Nome: ')
    if(x=='sair'):
        break
    
    x=x+'\n'
    with open('nomes.txt','a') as arquivo:
        arquivo.write(x)
           

