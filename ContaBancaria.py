class Conta():
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def Depositar(self):
        valor = int(input("Quer depositar quanto? "))
        self.saldo += valor
        return f"Saldo atualizado, valor de R$ {self.saldo}"

    def Sacar(self):
        valor = int(input("Quer sacar quanto? "))
        if valor > self.saldo:
            print(f"Não é possível sacar mais que R$ {self.saldo}")
        else:
            self.saldo -= valor
            print(f"Saldo atualizado, valor de R$ {self.saldo}")

    def __str__(self):
        return f"Na conta de {self.nome} tem R$ {self.saldo}\n"

conta1 = Conta("Guilherme", 100)
print(conta1)

conta1.Depositar()
print(conta1)

conta1.Sacar()
print(conta1)