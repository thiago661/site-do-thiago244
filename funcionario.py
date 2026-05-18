from pessoa import pessoa 

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print("Ponto registrado!")
