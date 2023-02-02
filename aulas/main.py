import copy
from dados.produtos import produtos

# FAZ UMA COPIA E ADICIONA NOVOS PRODUTOS COM 10% DE AUMENTO
novos_produtos =[
    {**p, 'preco': round(p['preco'] * 1.1, 2) }
    for p in copy.deepcopy(produtos)
]

#FAZ UMA COPIA E ORDENA O PRODUTO POR ORDEM DECRESCENTE
produtos_ord_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'], 
    reverse=True
)


print(*produtos, sep= '\n' )
print()
print(*produtos_ord_nome, sep='\n')






   

