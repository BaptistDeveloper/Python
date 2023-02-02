
lista = [numero * 2 for numero in range(10)]
#print(lista)

# MAPEAMENTO DE DADOS LIST COMPREHENSION

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [

    {**produto, 'preço':produto['preco']* 1.5}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos      
]

print(*novos_produtos, sep='\n')    