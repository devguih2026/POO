from rich.traceback import install
install()

# Crie uma classe Livro que simula a passagem de páginas de um livro e mostre se chegar no fim do livro

class Livro():
    def __init__(self, nome, paginas, pagina = 1):
        self.nome = nome
        self.paginas = paginas
        self.pagina = pagina
        print(f"Você está na página {self.pagina} do livro {self.nome}")

    def Avancar(self, avancar):
        if self.pagina + avancar < self.paginas:
            self.pagina += avancar
            print(f"Você leu {avancar} páginas, agora está na página {self.pagina}")
        elif self.pagina + avancar == self.paginas:
            avancar += self.pagina
            self.pagina = self.paginas 
            print(f"Você leu {avancar} páginas, fim do livro")
        else:
            print(f"Não tem mais páginas para ler")


livro1 = Livro(nome="Harry Potter", paginas=150)
livro1.Avancar(1)
livro1.Avancar(5)
livro1.Avancar(143)

    