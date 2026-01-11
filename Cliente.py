# simulação de uma classe para clientes 

class Cliente():
    def __init__(self, username, idade, cpf, plano):
        self.nome = username
        self.idade = idade
        self.cpf = cpf
        self.lista_planos = ["Básico", "Intermediário", "Premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception ("Plano inválido") # gera erro no terminal 
        
        
     # Método para alterar o plano do cliente   
    def AlterarPlano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            return "Plano inválido"
        
    def __str__(self):
        return f"Cliente: nome= {self.nome}, idade= {self.idade}, plano= {self.plano}"


cliente1 = Cliente("Guilherme", 23, 100, "Básico")
print(cliente1)







