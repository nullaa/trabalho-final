# Cliente
cliente_username = []
cliente_cpf = []
cliente_ender = []
cliente_senha = []
cliente_email = []
cliente_tel = []
cliente_limitecredito = []
carrinho_compras = []
carrinho_compras_valor = []
carrinho_total = []


# itens disponiveis
estoque = (
        "0-Campari", # estoque[0]
        45.90,  # estoque[0]
        "1-Limoncello", # estoque[2] 1*2
        207.79,
        "2-Jägermeister",
        99.90,
        "3-Soju",
        31.50,
        "5-Sidra de Astúrias",
        75.80,
        "6-Whisky",
        1029.90,
        "7-Gin",
        159.90,
        "8-Vodka",
        79.90,
        "9-Vinho",
        74.90,
        "10-Cachaça",
        89.90,
        "11-Cerveja",
        77.50,
        "12-Champanhe",
        499.90,
        "13-Tequila",
        349.90,
        "14-Conhaque",
        117.78,
        "15-Rum",
        215.00,
        "16-Pisco",
        289.90,
        "17-Sakê",
        39.48,
        "18-Amarula",
        89.90,
        "19-Raki",
        99.90,
        "20-Absinto",
        199.90,
    )
	
def mostrar_produto(estoque):#função para apresentar os prudtos em uma tabela
    print("-" * 30)
    print("Produtos disponiveis")
    print("-" * 30)
    for i in range(0, len(estoque)):
        if i % 2 == 0:
            print(f"{estoque[i]:.<30}", end="")#se a posição ocupada for par sera alianhado a esquerda
        else:
            print(f"R${estoque[i]:>7.2f}")#se a posição ocupada for impar sera alianhado a diretita
    return estoque


def valida_cpf(cpf):#validação do cpf de acordo com os difitos para saber se é um cpf valido
    if len(cpf) < 11:
        return False
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]


# cadastro cliente
def cadastrar():

    cpf = input("Digite o cpf do cliente:\n")
    validar = valida_cpf(cpf)
    if validar == True:
        cliente_cpf.append(cpf)
        cliente_username.append(input("Digite o nome do cliente:\n"))
        cliente_email.append(input("Digite o email do cliente:\n"))
        for i in range(6):
          senha=(input("Digite sua senha"))
          cliente_senha.append(senha)
        cliente_limitecredito.append(input("Digite o limite de credito do cliente:\n"))
    else:
        print("CPF inválido, tente novamente!")


# mostra um cliente a partir do cpf
# mostra um cliente a partir do cpf
# mostra um cliente a partir do cpf
def consulta_cliente():
    print("Qual o cpf que deseja consultar? ")
    cpf = input("Digite o cpf: ")
    if cpf in cliente_cpf:
        index = cliente_cpf.index(cpf)
        print(cliente_username[index])
        print(cliente_email[index])
    else:
        print("Cliente não encontrado")
        menu()


def comprar(estoque,carrinho_compras,carrinho_compras_valor):#addicinanco produtos no carrinho
   
        print("Selecione o que você quer comprar : ")
        #while  carrinho_total>cliente_limitecredito:#ele so pode addicionar produtos no carrinho apenas no valor do seu crediario, não podendopassar deste valor
        index = int(input("Digite o codico do produto: "))*2#multiplicando por dois a posiçao sempre podera escolher o produto pelo codigo 
        produto=(estoque[index])
        carrinho_compras_valor=(estoque[index+1])
        carrinho=(carrinho_compras_valor)
        carrinho_compras.append(carrinho)
        print(produto)
        print(carrinho_compras)
        qtd=int(input("Digite a quantidade de produto a adicionar no carrinho:\n"))
        preco=carrinho*qtd
        carrinho_total.append(preco)
        print(carrinho_total)
    
    



# menu principal

index = 0


def menu():
    opcao = "-1"

    while opcao != "0":
        print(
            """Menu:
1 - Cadastro
2 - Comprar
3 - Mostrar carrinho
4 - Pagar conta
5 - Consultar cliente
6 - Mostrar produtos
0 - Sair"""
        )
        opcao = input()

        if opcao == "1":
            print("Opção selecionada: Cadastro")
            index = cadastrar()
            

        elif opcao == "2":
            print("Opção selecionada: Comprar")
            consulta_cliente()
            print("Vamos as compras")
            mostrar_produto(estoque)
            comprar(estoque,carrinho_compras,carrinho_compras_valor)
        
        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")
            cliente_limitecredito==1500
            print("pagamento efetuado com sucesso")

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")
            consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")
            mostrar_produto(estoque)

        elif opcao == "0":
            print("Saindo...")

        else:
            print("Opção inválida! Tente novamente.")


menu()