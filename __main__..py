class Veiculo:
    def __init__(self, nome, preco_km):
        self.nome = nome
        self.preco_km = preco_km

    def calcular_frete(self, distancia):
        return self.preco_km * distancia


def escolher_veiculo():
    print("=== ESCOLHA O VEÍCULO ===")
    print("1 - Moto")
    print("2 - Drone")
    print("3 - Caminhão")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        return Veiculo("Moto", 1.0)
    elif opcao == 2:
        return Veiculo("Drone", 2.5)
    elif opcao == 3:
        return Veiculo("Caminhão", 3.5)
    else:
        print("Opção inválida!")
        return None


def main():
    print("=== SISTEMA DE FRETE ===")

    veiculo = escolher_veiculo()
    if veiculo is None:
        return

    # Aqui você controla a distância
    distancia = float(input("Digite a distância (km): "))

    valor = veiculo.calcular_frete(distancia)

    print(f"\nVeículo: {veiculo.nome}")
    print(f"Distância: {distancia} km")
    print(f"Frete: R$ {valor:.2f}")

    # Pagamento
    pago = float(input("Digite o valor pago: R$ "))

    if pago >= valor:
        print("Entrega realizada com sucesso! ✅")
        print(f"Troco: R$ {pago - valor:.2f}")
    else:
        print("Pagamento insuficiente ❌")


# Executa o sistema
if __name__ == "__main__":
    main()