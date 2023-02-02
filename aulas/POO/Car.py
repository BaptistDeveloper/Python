class Car:
    def __init__(self, name) :
        self.name = name

    def acelerar(self):
        print(f'{self.name} esta acelerando... ')

    def conserto(self):
        print(f'mandei o(a) {self.name} consertar...')

    def alugar(self):
        print(f'estou alugando {self.name} ...')

    def km(self, kilometros):
        return f'{self.name} esta andando a {kilometros} km '


ferrari = Car('Ferrari')
ferrari.acelerar()
ferrari.conserto()


fusca = Car('Fusca')
fusca.acelerar()
fusca.alugar()
print(fusca.km(15))