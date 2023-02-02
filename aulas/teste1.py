


pin = input('Digite o seu PIN de 6 digitos: ')
if pin.isdigit() and len(pin) == 6:
    pin_guad = pin
    print('Pin guardado chef!')
else: 
    print('fora meu chapa!')