# Controle de Produtos

# Descrição:
# Classe Produto com preço e estoque.
# A classe deve ter: encapsulamento, impedir valores inválidos, lógica condicional

class Produtos():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco # "_" encapsula o atributo
        self._estoque = estoque

    def AlterarPreco(self, novo_preco):
        if novo_preco <= 0:
            return "Preço inválido"
        self._preco = novo_preco
        return f"Preço atualizado: {self._preco}"
        
    def AumentarEstoque(self, quantidade):
        if quantidade <= 0:
            return "Quantidade inválida"
        else:
            self._estoque += quantidade
            return f"Estoque atualizado: {self._estoque}"
        
    def TirarEstoque(self, quantidade):
        if quantidade > self._estoque:
            return "Estoque insuficiente"
        else:
            self._estoque -= quantidade
            return f"Estoque atualizado: {self._estoque}"

    def __str__(self):
        return f"Produto: {self.nome}, preço: R$ {self._preco}, quantidade em estoque: {self._estoque}"

produto1 = Produtos("Bolacha", 4, 50)
print(produto1)

# usa a função de alterar preço 
produto1.AlterarPreco(1)
print(produto1)

# usa a função de aumentar estoque
produto1.AumentarEstoque(1)
print(produto1)

# usa a função de tirar estoque
produto1.TirarEstoque(52)
print(produto1)

