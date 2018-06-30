#!/usr/bin/python3

with open('frutas.txt','r') as arquivo: 
    mud = arquivo.readlines()

with open('frutas2.txt','w') as arquivo:
    cont = 1
    for linha in mud:
        linha =linha.replace( '\n','-{}\n'.format(cont))
        arquivo.write(linha) 
        cont +=1   
            
         