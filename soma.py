#!/usr/bin/python3
nome = input("Nome do aluno: ")
soma = int(input("Digite nota 1: "))
soma += int(input("Digite nota 2: "))
print("O Aluno {} tem a media {}".format(nome.title(),soma/2))