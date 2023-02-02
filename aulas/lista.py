import os 

lista = []

while True:
    print('Seleciona uma opção')
    opcao = input('[I]nserir [A]pagar [L]istar: ')

    if opcao == 'I' or opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
       

    elif opcao == 'a' or opcao == 'A':
        indice = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice)
            del lista[indice]
            print(f'O indice {indice} Foi apagado! ')

        except:
             print('Nao foi possivel apagar este indice! ')


    elif opcao == 'l' or opcao == 'L':
        os.system('cls')

        if len(lista) == 0: 
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)




