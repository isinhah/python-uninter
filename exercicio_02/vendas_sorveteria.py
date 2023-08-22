# Exercicio 2 da atividade prática

# mensagem de boas-vindas e a tabela de sabores com preços
print("Bem-vindo à Sorveteria da Isabel Henrique")
print(37 * "-" + "Cardápio" + 37 * "-")
print(
    "| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)"
)
print(
    "|      1      |         R$ 6,00        |      R$ 7,00       |      R$ 8,00      "
)
print(
    "|      2      |         R$ 10,00       |      R$ 12,00      |      R$ 14,00      "
)
print(
    "|      3      |         R$ 14,00       |      R$ 17,00      |      R$ 20,00      "
)
print(82 * "-")

acumulador = 0  # inicialização do acumulador

# controle de fluxo
while True:
    sabor = input("Entre com o valor desejado (tr/pr/es): ").lower()
    if sabor not in [
        "tr",
        "pr",
        "es",
    ]:  # operador not in, uma alternativa para sabor != "tr" or "pr" or "es"
        print("Sabor inválido. Tente novamente!")
        continue  # se o usuário digitar algo incorreto, o programa volta para o while
    bolas = input("Entre com o número de bolas de sorvete desejado ( 1 / 2 / 3): ")
    if bolas not in [
        "1",
        "2",
        "3",
    ]:  # operador not in, uma alternativa para sabor != "tr" or "pr" or "es"
        print("Número de bolas inválido. Tente novamente!")
        continue  # se o usuário digitar algo incorreto, o programa volta para o while

    # controle de fluxo
    if sabor == "tr" and bolas == "1":
        print(f"Você pediu {bolas} de sorvete no sabor TRADICIONAL: R$ 6.00")
        acumulador = acumulador + 6.00
    elif sabor == "tr" and bolas == "2":
        print(f"Você pediu {bolas} de sorvete no sabor TRADICIONAL: R$ 10.00")
        acumulador = acumulador + 10.00
    elif sabor == "tr" and bolas == "3":
        print(f"Você pediu {bolas} de sorvete no sabor TRADICIONAL: R$ 14.00")
        acumulador = acumulador + 14.00
    elif sabor == "pr" and bolas == "1":
        print(f"Você pediu {bolas} de sorvete no sabor PREMIUM: R$ 7.00")
        acumulador = acumulador + 7.00
    elif sabor == "pr" and bolas == "2":
        print(f"Você pediu {bolas} de sorvete no sabor PREMIUM: R$ 12.00")
        acumulador = acumulador + 12.00
    elif sabor == "pr" and bolas == "3":
        print(f"Você pediu {bolas} de sorvete no sabor PREMIUM: R$ 17.00")
        acumulador = acumulador + 17.00
    elif sabor == "es" and bolas == "1":
        print(f"Você pediu {bolas} de sorvete no sabor ESPECIAL: R$ 8.00")
        acumulador = acumulador + 8.00
    elif sabor == "es" and bolas == "2":
        print(f"Você pediu {bolas} de sorvete no sabor ESPECIAL: R$ 14.00")
        acumulador = acumulador + 14.00
    else:
        print(f"Você pediu {bolas} de sorvete no sabor ESPECIAL: R$ 20.00")
        acumulador = acumulador + 20.00

    # verificar se o usuário que fazer outro pedido
    outro_pedido = input(
        "Deseja pedir mais alguma coisa? (S / digite outra tecla) "
    ).lower()
    if (
        outro_pedido == "s"
    ):  # resolve o problema das letras 'S' e 's', uma vez que o caractere 's' digitado pelo usuário permanecerá sempre em minúsculo
        continue
    else:
        print(f"O valor total a ser pago é: R$ {acumulador:.2f}")
        break
