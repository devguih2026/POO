from rich.traceback import install
install()

# crie a classe churrasco, onde é possível informar quantas pessoas vão participar
# mostre a quantidade necessária de carne a ser comprada
# mostre o custo total do churrasco 
# mostre o custo por pessoa
# CONSIDERE: 400g de carne por pessoa e R$ 82,4 o KG da carne

class Churrasco():
    def __init__(self, quantidade_pessoas):
        self.quantidade_pessoas = quantidade_pessoas
        
    def Analisar(self):
        consumo_pessoa = 0.4
        preco_carne = 82.4
        quantidade_carne = self.quantidade_pessoas * consumo_pessoa
        valor_total = quantidade_carne * preco_carne
        valor_pessoa = valor_total / self.quantidade_pessoas
        print(f"Num churrasco com {self.quantidade_pessoas}, cada pessoa come 0.4kg de carne e o kg custa R$82.4\n")
        print(f"Recomendo comprar {quantidade_carne:.3f}kg de carne\n")
        print(f"O valor total fica R${valor_total:.2f}\n")
        print(f"Cada pessoa terá que pagar R${valor_pessoa:.2f}")

c1 = Churrasco(100)
c1.Analisar()

