from rich.traceback import install
install()
from rich import print

# Crie uma classe caneta que simule o funcionamento de uma caneta colorida, podendo escrever na cor relativa

# print("[blue]Olá[/] [red]mundo[/]")  imprime "olá" em azul e "mundo" em vermelho

class Caneta():
    def __init__(self, cor, usar = False):
        self.cor = cor
        self.usar = usar
        
    def destampar(self):
        self.usar = True

    def Escrever(self, texto):
        if self.usar == False:
            print(f"A [{self.cor}]caneta[/] está tampada")
        else:
            print(f"[{self.cor}]{texto}[/]")

c1 = Caneta("blue")
c1.destampar()
c1.Escrever("Olá mundo")

c2 = Caneta("red")
c2.destampar()
c2.Escrever("Essa é a caneta vermelha")