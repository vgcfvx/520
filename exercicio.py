#!/usr/bin/python3
total=0   
frutas = [
    {'nome':'Uva','preco':11,'qtd':12},
    {'nome':'Pera','preco':12,'qtd':13},
    {'nome':'Melao','preco':13,'qtd':14},
    {'nome':'Maca','preco':14,'qtd':15}
]
for x in (frutas) :       
       valor = x['qtd']*x['preco']
       print('Você ganhará',valor,'com a venda de',x['nome'])
       total += valor
print('Total de vendas =',total)       
