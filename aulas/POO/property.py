class Caneta:

    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None


    @property
    def cor (self):
        print('Estou no GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
       
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor    
     



c1 = Caneta('Verde')
c1.cor = 'Pink'
c1.cor_tampa = 'Azul'
print(c1.cor)
print(c1.cor_tampa)