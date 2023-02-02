"""
Este código d
efine uma função decoradora chamada criar_funcao() que recebe uma função como argumento e retorna uma nova função, chamada interna(). A função interna() tem dois argumentos especiais: *args e **kwargs, que permitem a passagem de uma quantidade variável de argumentos não-nomeados e nomeados, respectivamente.

A função interna tem uma estrutura de loop que percorre todos os argumentos passados para a função usando *args, e chama a função is_string para cada elemento, essa função verifica se o argumento é uma string, se não for, ele gera um erro de tipo TypeError.

Depois de verificar todos os argumentos, a função interna() chama a função original passada como argumento, usando os argumentos *args e **kwargs, e armazena o resultado em uma variável chamada resultado. Por fim, a função interna() retorna o resultado.
A função decoradora criar_funcao é usada na linha @criar_funcao antes de definir a função invert_strings(). Isso significa que, a cada vez que a função invert_strings() é chamada, ela é automaticamente envolta pela função interna() criada pela decoradora.

A função invert_strings() é uma função simples que inverte a ordem dos caracteres de uma string passada como argumento.

Por fim, a variável invertida é atribuída o valor retornado pela função invert_strings('123') e imprimi o valor na tela.
"""


def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

@criar_funcao
def invert_strings(string):
    return string[::-1]



invertida= (invert_strings('432'))
print(invertida)

