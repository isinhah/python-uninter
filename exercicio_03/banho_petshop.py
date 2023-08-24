# Exercicio 3 da atividade prática: Sistema de cobrança de banho para um petshop


# funções
def cachorro_peso():
    while True:
        try:
            cachorro_peso = float(input("Entre com o peso do cachorro (kg): "))

            if cachorro_peso < 3:
                return 40
            elif 3 <= cachorro_peso < 10:
                return 50
            elif 10 <= cachorro_peso < 30:
                return 60
            elif 30 <= cachorro_peso < 50:
                return 70
            else:
                print("Não aceitamos cachorros tão grandes.")
                print("Por favor entre com o peso do cachorro novamente.")
                continue  # volta para o inicio da pergunta (laço)

        except ValueError:  # caso o usuário não digite um valor númerico
            print("Você digitou um valor não numérico")
            print("Por favor entre com o peso do cachorro novamente.")


def cachorro_pelo():
    while True:
        cachorro_pelo = input(
            "Entre com o pelo do cachorro\n"
            + "c - Pelo Curto\n"
            + "m - Pelo Médio\n"
            + "l - Pelo Longo\n"
            + ">> "
        )

        if (
            cachorro_pelo.lower().strip() == "c"
        ):  # o lower() vai converter o 'S' para 's'
            return 1.00  # valor do multiplicador
        elif cachorro_pelo.lower().strip() == "m":
            return 1.5
        elif cachorro_pelo.lower().strip() == "l":
            return 2.00
        else:
            print("Por favor entre com o pelo do cachorro novamente.")
            continue  # volta para o inicio da pergunta (laço)


def cachorro_extra():
    acumulador = 0
    while True:
        cachorro_extra = input(
            "Deseja adicionar mais algum serviço?\n"
            + "1 - Corte de Unhas - R$ 10,00\n"
            + "2 - Escovar Dentes - R$ 12,00\n"
            + "3 - Limpeza de Orelhas - R$ 15,00\n"
            + "0 - Não desejo mais nada\n"
            + ">> "
        )

        if cachorro_extra == "0":
            return acumulador  # não vai adicionar mais nenhum valor
        elif cachorro_extra == "1":
            acumulador = acumulador + 10
            continue  # volta para o inicio do laço
        elif cachorro_extra == "2":
            acumulador = acumulador + 12
            continue
        elif cachorro_extra == "3":
            acumulador = acumulador + 15
            continue
        else:
            print("Pare de digitar opções diferentes de 0, 1, 2 e 3!")


# inicio do main
print("Bem vindo ao Petshop da Isabel Henrique")
peso = cachorro_peso()
pelo = cachorro_pelo()
extra = cachorro_extra()
total = peso * pelo + extra
print(
    f"Total a pagar (R$): {total:.2f} (peso: {peso} * pelo: {pelo} + adicional(is): {extra})"
)
