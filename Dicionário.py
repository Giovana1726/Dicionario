estoque = {
    "Prego": [8000, 1.0],
    "Chave de fenda": [400, 5.0],   #Dionário serve para armazenar dados
    "Martelo": [600, 12.50],
}

total = 0
print('Vendas: \n')
while True:
    produto = input('Nome do produto (Fim para sair): ')  #Digitar fim para sair do programa
    if produto == "Fim":
        break #Se não tiver o código quebra
    if produto in estoque:
        quantidade = int(input('Quantidade: '))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade    #Calculando os preços
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível")
    else:
        print("Nome de produto inválido")
print(f"custo total: {total:21.2f} \n")
print('Estoque: \n')
for chave, dados in estoque.items():
    print("Descrição: ", chave)  #Cadastrando as chaves
    print('Quantidade: ', dados[0])
    print(f'Preço: {dados[1]:6.2f} \n')