# Cliente
cliente_username = []
cliente_cpf = []
cliente_ender = []
cliente_senha = []
cliente_email = []
cliente_tel = []
cliente_limitecredito = []
carrinho_compras = []
carrinho_total = []

# itens disponiveis
def mostrar_produto():
    estoque = (
        "1-Campari",
        45.90,
        "2-Limoncello",
        207.79,
        "3-Jägermeister",
        99.90,
        "4-Soju",
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
    print("-" * 30)
    print("Produtos disponiveis")
    print("-" * 30)
    for i in range(0, len(estoque)):
        if i % 2 == 0:
            print(f"{estoque[i]:.<30}", end="")
        else:
            print(f"R${estoque[i]:>7.2f}")
    return estoque


def valida_cpf(cpf):
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
        cliente_ender.append(input("Digite o endereço do cliente:\n"))
        cliente_email.append(input("Digite o email do cliente:\n"))
        cliente_senha.append(input("Digite sua senha"))
        cliente_tel.append(input("Digite o telefone do cliente:\n"))
        cliente_limitecredito.append(input("Digite o limite de credito do cliente:\n"))
    else:
        print("CPF inválido, tente novamente!")


# mostra um cliente a partir do cpf
# mostra um cliente a partir do cpf
def consulta_cliente():
    for i in cliente_username:
        print("Qual o cpf que deseja consultar? ")
        cpf = input("Digite o cpf: ")
        if cpf in cliente_cpf:
            index = cliente_cpf.index(cpf)
            print(cliente_username[index])
            print(cliente_email[index])


def comprar(cpf, senha):
    print("implementar com o cpf e a senha", cpf, " ", senha)


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
            cpf = input("Digite  o cpf: ")
            senha = input("Digite  a senha: ")
            comprar(cpf, senha)
            print("Vamos as compras")
        elif opcao == "3":
            print("Opção selecionada: Mostrar carrinho")

        elif opcao == "4":
            print("Opção selecionada: Pagar conta")

        elif opcao == "5":
            print("Opção selecionada: Consultar cliente")
            consulta_cliente()

        elif opcao == "6":
            print("Opção selecionada: Mostrar produtos na prateleira")
            mostrar_produto()

        elif opcao == "0":
            print("Saindo...")

        else:
            print("Opção inválida! Tente novamente.")


menu()
