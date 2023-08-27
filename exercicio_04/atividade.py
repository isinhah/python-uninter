# Exercicio 4 da atividade prática:

# inicio das variáveis globais
lista_colaboradores = []
id_global = 0

# fim da variáveis globais


# inicio de cadastrar_colaborador()
def cadastrar_colaborador(id):
    print("*" * 74)
    print(24 * "-" + "MENU CADASTRAR COLABORADOR" + 24 * "-")
    print(f"id do colaborador: {id}")
    nome = input("Por favor entre com o nome: ")
    setor = input("Por favor entre com o setor: ")
    salario = float(input("Por favor entre com o pagamento (R$): "))
    dicionario_colaboradores = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "pagamento": salario,
    }
    lista_colaboradores.append(dicionario_colaboradores.copy())
    return


# fim de cadastrar_colaborador()


# inicio de consultar_colaborador()
def consultar_colaborador():
    print("*" * 74)
    print(22 * "-" + "MENU CONSULTAR COLABORADOR" + 22 * "-")
    while True:
        opcao_consultar = input(
            "Escolha a opção desejada:\n"
            + "1-Consultar todos os colaboradores\n"
            + "2-Consultar colaborador por id\n"
            + "3-Consultar colaborador(es) por setor\n"
            + "4-Retornar\n"
            + ">> "
        )

        print("-----------------------------")

        if opcao_consultar == "1":
            for (
                colaborador
            ) in (
                lista_colaboradores
            ):  # colaborador vai varrer toda a lista de colaboradores
                for (
                    key,
                    value,
                ) in (
                    colaborador.items()
                ):  # varrer todos os conjuntos chave e valor do dicionario colaboradores
                    print(f"{key}: {value}")
            print("-----------------------------")

        elif opcao_consultar == "2":
            id_desejado = int(input("Digite o id do colaborador: "))
            print("-----------------------------")
            for colaborador in lista_colaboradores:
                if (
                    colaborador["id"] == id_desejado
                ):  # o valor do campo id desse dicionário é igual o id desejado?
                    for (
                        key,
                        value,
                    ) in (
                        colaborador.items()
                    ):  # varrer todos os conjuntos chave e valor do dicionario colaboradores
                        print(f"{key}: {value}")
            print("-----------------------------")

        elif opcao_consultar == "3":
            id_desejado = input("Digite o setor do(s) colaborador(es): ")
            for colaborador in lista_colaboradores:
                print("-----------------------------")
                if (
                    colaborador["setor"] == id_desejado
                ):  # o valor do campo setor desse dicionário é igual o id desejado?
                    for (
                        key,
                        value,
                    ) in (
                        colaborador.items()
                    ):  # varrer todos os conjuntos chave e valor do dicionario colaboradores
                        print(f"{key}: {value}")
                print("-----------------------------")
        elif opcao_consultar == "4":
            return  # sai da função consultar_colaborador e volta para main
        else:
            print("Opção inválida. Tente novamente.")
            continue  # volta para o inicio do laço


# fim de consultar_colaborador()


# inicio de remover_colaborador()
def remover_colaborador():
    print("*" * 74)
    print(25 * "-" + "MENU REMOVER COLABORADOR" + 25 * "-")
    id_desejado = int(input("Digite o id do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_desejado:
            lista_colaboradores.remove(colaborador)


# fim de remover_colaborador()

# inicio de Main
print("Bem-vindo ao Controle de Colaboradores da Isabel Henrique")
while True:
    print(74 * "*")
    print(30 * "-" + "MENU PRINCIPAL" + 30 * "-")
    opcao_principal = input(
        "Escolha a opção desejada:\n"
        + "1-Cadastrar Colaborador\n"
        + "2-Consultar Colaborador(es)\n"
        + "3-Remover Colaborador\n"
        + "4-Sair\n"
        + ">> "
    )

    if opcao_principal == "1":
        id_global = id_global + 1
        cadastrar_colaborador(id_global)
    elif opcao_principal == "2":
        consultar_colaborador()
    elif opcao_principal == "3":
        remover_colaborador()
    elif opcao_principal == "4":
        break  # encerra o laço principal, o programa acaba
    else:
        print("Opção inválida. Tente novamente.")
        continue  # volta para o inicio do laço

# fim de Main
