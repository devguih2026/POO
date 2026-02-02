from rich.traceback import install
install()

# Crie a classe Funcionário onde podemos cadastrar nome, setor e cargo
# Crie também um método que permite ao funcionário se apresentar

class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def Apresentar(self):
        return f"Meu nome é {self.nome}, eu sou {self.cargo} do setor de {self.setor}"
    
f1 = Funcionario("Guilherme", "TI", "Engenheiro de Software")
print(f1.Apresentar())

