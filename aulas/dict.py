pessoa = {}


chave = 'nome'
pessoa[chave] = 'João vitor' 
pessoa['sobrenome'] = 'Araujo'

print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']
print(pessoa)


#METODO 1
#try:
    #pessoa['sobrenome']
        
#except:
    #print('NAO PERMITIDO')  

#METODO 2
if pessoa.get('sobrenome') is None:
    print('NAO EXISTE')
else:
    print(pessoa['sobrenome'])