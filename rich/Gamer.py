from rich.traceback import install
install()

# Crie a classe Gamer, onde podemos cadastrar "nome", "nick" e "jogos favoritos" de uma pessoa
# Crie um método que permite mostrar a "ficha" do usuário

class Gamer():
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogo_favorito = []
    
    def AdicionarFavorito(self, jogo):
        self.jogo_favorito.append(jogo)

    def __str__(self):
        return f"Nome: {self.nome}, nickname: {self.nick}, jogos favoritos: {self.jogo_favorito}"
    
j1 = Gamer("Guilherme", "Guih2020")
j1.AdicionarFavorito("GOW")
j1.AdicionarFavorito("FIFA")
j1.AdicionarFavorito("TLOF")

print(j1)