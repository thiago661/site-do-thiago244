import inspect

class Jogo:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano
   
    def atacar(self, inimigo):
        inimigo.vida -= self.dano
        print(f"{self.nome} atacou {inimigo.nome}! Vida de {inimigo.nome}: {inimigo.vida}") 

personagem1 = Jogo("Guerreiro", 100, 20)     
personagem2 = Jogo("Mago", 80, 25)

print("\n⚔️ BATALHA COMEÇOU!\n")

personagem1.atacar(personagem2)

# jeito certo
print(vars(personagem1))
print(vars(personagem2))