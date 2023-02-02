
#CRIANDO A CLASSE CARRINHO
class Carrinho:
    def __init__(self):
        self._produtos = []

    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)


    def total(self):
        print(f'O total dos produtos foi {sum([produto.preco for produto in self._produtos])}')
        return sum([produto.preco for produto in self._produtos])
        

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

#CRIANDO A CLASSE PRODUTOS, QUE É AGREGADA AO CARRINHO.
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1 = Produtos('Caneta', 1.20)
p2 = Produtos('Lapis', 2.0)
p3 = Produtos('camisa', 20.0)
carrinho.inserir_produtos(p1, p2, p3)
carrinho.listar_produtos()
print(carrinho.total())