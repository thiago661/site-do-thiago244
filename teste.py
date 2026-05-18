# Sistema simples de supermercado

produtos = {
    1: {"nome": "Arroz", "preco": 20},
    2: {"nome": "Feijão", "preco": 10},
    3: {"nome": "Macarrão", "preco": 6},
    4: {"nome": "Refrigerante", "preco": 8},
    5: {"nome": "Óleo", "preco": 7},
    6: {"nome": "Café", "preco": 12},
    7: {"nome": "Leite", "preco": 5}
}

carrinho = []
total = 0

while True:
    print("\n=== SUPERMERCADO ===")
    
    for codigo, item in produtos.items():
        print(f"{codigo} - {item['nome']} (R$ {item['preco']})")
    
    print("0 - Finalizar compra")
    
    try:
        escolha = int(input("Escolha um produto: "))
        
        if escolha == 0:
            break
        
        if escolha in produtos:
            carrinho.append(produtos[escolha])
            total += produtos[escolha]["preco"]
            print(f"{produtos[escolha]['nome']} adicionado ao carrinho!")
        else:
            print("Produto inválido!")
    
    except:
        print("Digite um número válido!")

# Nota fiscal
print("\n=== NOTA FISCAL ===")
for item in carrinho:
    print(f"- {item['nome']} (R$ {item['preco']})")

print(f"\nTotal: R$ {total}")
print("Obrigado pela compra!")