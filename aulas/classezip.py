

from itertools import zip_longest


citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA' , 'SP', 'MG', 'RJ'] 

#USANDO A LISTA MENOR
print(list(zip(citys, states)))

#USANDO A LISTA MAIOR, 'Fillvalue' serve para substiuir o 'NONE' que iria ficar no 'RJ' ja que estamos usando a lista maior nesse caso!
print(list(zip_longest(citys, states, fillvalue='SEM CIDADE')))
