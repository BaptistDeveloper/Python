
def is_leap(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input('DIGITE UM ANO?'))

if is_leap(ano):
    print(f'o {ano} é BISSEXTO')
else:
    print(f'o {ano} não é BISSEXTO')
