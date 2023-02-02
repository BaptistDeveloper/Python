
class Carro:
    def __init__(self, nome):

        #FAZENDO A LIGAÇÃO DO MOTOR E FABRICANTE COM A CLASS CARRO...
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor


    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('volkswagen')
motor_1 = Motor('5.0')
fusca.motor = motor_1
fusca.fabricante = volkswagen
print(fusca.fabricante.nome, fusca.nome, fusca.motor.nome)

Pulse = Carro('Pulse')
fiat = Fabricante('fiat')
motor_1 = Motor('3.0')
Pulse.motor = motor_1
Pulse.fabricante = fiat
print(Pulse.fabricante.nome, Pulse.nome, Pulse.motor.nome)