"""
Um generator em Python é um tipo especial de função que pode ser usado para gerar uma sequência de valores, um de cada vez, em tempo real.
Eles são semelhantes aos iteradores, mas são definidos usando a yieldinstrução em vez da returninstrução. Os geradores são úteis para 
criar grandes sequências de dados que seriam impraticáveis ​​para armazenar na memória de uma só vez, bem como para criar sequências infinitas.
Eles também podem ser usados ​​para implementar avaliação preguiçosa, onde o próximo valor na sequência não é computado até que seja necessário.
"""


# def generator(n=0):
#     yield n

# gen = generator(n=0)
# for n in range(1000):
#     print(n)



def generator(n=0):
    yield 1 #PAUSAR
    print('continuando...')
    yield 2 #PAUSAR
    print('Mais uma...')
    
gen = generator(n=0)
for n in gen:
    print(n)

    