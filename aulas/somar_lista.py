lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


#MANEIRA 1
# def somar_lista(lista_a, lista_b):
#     tamanho = min (len(lista_a), len(lista_b))
#     return [
#         lista_a[i]+lista_b[i] for i in range(tamanho)
#     ]
# print(somar_lista(lista_a, lista_b))




# MANEIRA 2
# lista_soma = [x + y for x,y in zip(lista_a, lista_b)]
# print(lista_soma)