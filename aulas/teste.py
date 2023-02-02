entrada = input("[E]ntrar [S]air: ")
senha_perm = '123456'
senha = ''

if entrada == 'E' or entrada == 'e':
    senha = input('Digite a senha: ')
    if senha == senha_perm:
        print("Voce entrou")
    elif senha != senha_perm:
        senha_inc = print("Senha incorreta!")
    
elif entrada == 'S' or entrada == 's':
    print("Voce saiu!")
else:
    print("Voce nao digitou nenhuma das opções!")
    