# ==============================
# SUPERMERCADO ALARCON
# ==============================

produtos = {
    101: {"nome": "Arroz", "preco": 25.90},
    102: {"nome": "Feijão", "preco": 8.50},
    103: {"nome": "Macarrão", "preco": 6.99},
    104: {"nome": "Refrigerante", "preco": 9.99},
    105: {"nome": "Óleo", "preco": 7.89},
    106: {"nome": "Café", "preco": 18.40},
    107: {"nome": "Leite", "preco": 5.99}
}

carrinho = {}

# ==============================
def mostrar_menu():#e meio para quir ar uma fumcao
    print("\n==============================")
    print("   SUPERMERCADO ALARCON")
    print("==============================")
    print("1 - Ver produtos")
    print("2 - Ver carrinho")
    print("3 - Remover item")
    print("4 - Finalizar compra")
    print("5 - Cancelar compra")
    print("6 - Sair")

# ==============================
def mostrar_produtos():
    print("\nPRODUTOS DISPONÍVEIS:")
    print ("colocar pordutos colocou 101 102 103 assim por diante")
    for codigo, p in produtos.items():
        print(f"{codigo} - {p['nome']} (R$ {p['preco']})")

# ==============================
def registrar_produto():
    mostrar_produtos()
    
    print("\nDigite os produtos separados por espaço e aperte ENTER.")
    print("Para voltar, digite 0.")
    
    entrada = input("Códigos: ")

    if not entrada.strip():#e para quiar de sisao no codigo
        print("Você não digitou nada!")
        return

    if entrada.strip() == "0":
        return

    try:
        codigos = entrada.split()

        for c in codigos:
            codigo = int(c)

            if codigo not in produtos:
                print(f"Código {codigo} inválido!")
                continue

            qtd = int(input(f"Quantidade para {produtos[codigo]['nome']}: "))

            if qtd <= 0:
                print("Quantidade inválida!")
                continue

            if codigo in carrinho:
                carrinho[codigo]["qtd"] += qtd
            else:
                carrinho[codigo] = {
                    "nome": produtos[codigo]["nome"],
                    "preco": produtos[codigo]["preco"],
                    "qtd": qtd
                }

            print(f"{produtos[codigo]['nome']} adicionado!")

    except:e #para quando quebra para nao dar ero
    print("Erro! Digite corretamente.")

# ==============================
def mostrar_carrinho():
    if not carrinho:
        print("\nCarrinho vazio!")
        return
    
    total = 0
    
    print("\n======= CARRINHO =======")#mensagem
    
    for item in carrinho.values():
        subtotal = item["preco"] * item["qtd"]
        total += subtotal
        
        print(f"{item['nome']}")
        print(f"{item['qtd']} x R$ {item['preco']:.2f}")
        print(f"Subtotal: R$ {subtotal:.2f}\n")
    
    print(f"TOTAL: R$ {total:.2f}")

# ==============================
def remover_item():
    if not carrinho:
        print("Carrinho vazio!")
        return

    try:
        codigo = int(input("Código para remover: "))
        
        if codigo in carrinho:
            del carrinho[codigo]
            print("Removido!")
        else:#mostra a mensagem que nao ta no carinho
            print("Produto não está no carrinho!")
    
    except:
        print("Erro!")

# ==============================
def calcular_total():
    total = 0
    for item in carrinho.values():
        total += item["preco"] * item["qtd"]
    return total

# ==============================
def finalizar_compra():
    if not carrinho:
        print("Carrinho vazio!")
        return
    
    total = calcular_total()
    
    print(f"\nTOTAL: R$ {total:.2f}")
    print("1 - Dinheiro (10% desconto)")
    print("2 - PIX (5% desconto)")
    print("3 - Cartão")
    
    forma = input("Escolha pagamento: ")
    
    desconto = 0
    
    if forma == "1":
        desconto = total * 0.10
        forma_nome = "DINHEIRO"
    elif forma == "2":
        desconto = total * 0.05
        forma_nome = "PIX"
    elif forma == "3":
        forma_nome = "CARTÃO"
    else:
        print("Forma inválida!")
        return
    
    total_final = total - desconto
    
    troco = 0
    
    if forma == "1":
        try:
            valor = float(input("Valor recebido: "))
            
            if valor < total_final:
                print("Valor insuficiente!")
                return
            
            troco = valor - total_final
        except:
            print("Erro!")
            return
    
    emitir_cupom(total, desconto, total_final, forma_nome, troco)
    carrinho.clear()

# ==============================
def emitir_cupom(total, desconto, total_final, forma, troco):
    print("\n==============================")
    print("        CUPOM FISCAL")
    print("==============================")
    
    for item in carrinho.values():
        subtotal = item["preco"] * item["qtd"]
        print(f"{item['nome']} x{item['qtd']} = R$ {subtotal:.2f}")
    
    print("------------------------------")
    print(f"TOTAL: R$ {total:.2f}")
    print(f"DESCONTO: R$ {desconto:.2f}")
    print(f"FINAL: R$ {total_final:.2f}")
    print(f"PAGAMENTO: {forma}")
    
    if forma == "DINHEIRO":
        print(f"TROCO: R$ {troco:.2f}")
    
    print("==============================")
    print("Obrigado por comprar no Supermercado Alarcon!")
    print("==============================")

# ==============================
# LOOP PRINCIPAL
while True:
    mostrar_menu()
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        registrar_produto()
    elif opcao == "2":
        mostrar_carrinho()
    elif opcao == "3":
        remover_item()
    elif opcao == "4":
        finalizar_compra()
    elif opcao == "5":
        carrinho.clear()
        print("Compra cancelada!")
    elif opcao == "6":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida!")