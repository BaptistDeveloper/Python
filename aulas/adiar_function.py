def somar(x, y):
    return x + y

def multiplica(x, y):
    return x * y

#ADIANTANDO UMA FUNCAO COM CLOSURE(FUNCAO QUE RETORNA OUTRA FUNCAO)
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


somar_numero = criar_funcao(somar, 5)
multiplicar_numero = criar_funcao(multiplica, 10)


somar_multiplicar = input('APERTE [S] para Somar com 5 ou [M] para multiplicar com 10: ' )

if somar_multiplicar == 'S' :
    num_digitado = int(input('Digite um numero: '))
    if num_digitado:
        print(somar_numero(num_digitado))  

if somar_multiplicar == 'M':
    num_digitado = int(input('Digite um numero: '))
    if num_digitado:
        print(multiplicar_numero(num_digitado))