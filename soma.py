#!/usr/bin/python3
nome = input("Nome do aluno: ")
soma = int(input("Digite nota 1: "))
soma += int(input("Digite nota 2: "))
print("{} tem a media {}".format(nome.title(),soma/2))
if soma >= 14 :
     print("{} foi aprovado".format(nome.title()))
elif soma>8 and soma <14:
     print("{} foi retido".format(nome.title()))
else:
     print("{} foi reprovado".format(nome.title()))     
