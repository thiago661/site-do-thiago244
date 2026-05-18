class Veiculo:
    def __init__(self, nome, preco_km):
        self.nome = nome
        self.preco_km = preco_km

    def calcular_frete(self, distancia):
        return self.preco_km * distancia


def main():
    print("=== ENTREGA COM DRONE ===")

    # Drone
    drone = Veiculo("Drone", 2.5)

    # Distância fixa
    distancia = 93

    # Calculando frete
    valor = drone.calcular_frete(distancia)

    print(f"Veículo: {drone.nome}")
    print(f"Distância: {distancia} km")
    print(f"Valor do frete: R$ {valor:.2f}")

    # Pagamento
    pago = float(input("Digite o valor pago: R$ "))

    if pago >= valor:
        print("Entrega realizada com sucesso! ✅")
        print(f"Troco: R$ {pago - valor:.2f}")
    else:
        print("Pagamento insuficiente ❌")


if __name__ == "__main__":
    main()