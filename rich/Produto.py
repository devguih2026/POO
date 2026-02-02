from rich.table import Table
from rich.traceback import install
install()
from rich.console import Console

# Crie a classe Produto, onde podemos cadastrar nome e preço 
# Crie também um método que mostre a etiqueta do preço

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def Etiqueta(self):
        tabela =Table(title = "Produtos")
        tabela.add_column("nome")
        tabela.add_column("preco")
        tabela.add_row(self.nome, str(f"R$ {self.preco}"))
        return tabela

produto1 = Produto("Moto g100", 2000)
produto2 = Produto("Iphone15", 8000)
console = Console()
console.print(produto1.Etiqueta(), produto2.Etiqueta())

