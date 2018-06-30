#!/usr/bin/python3
nome = input("Nome do aluno: ")
soma = 0
provas = int(input("Quantas provas? "))
for x in range(provas):
    nota = int(input("Digite a nota {} =".format(x+1)))
    soma+=nota    
media = soma/provas    
if media >= 7 :
     res = 'Aprovado'
elif media >4 and media <7:
     res = 'Retido'
else:
     res = 'Reprovado'

print("{} tem a media {} e foi {}".format(nome.title(),media,res.title()))     

#for x in range(65,65+26): print(chr(x))