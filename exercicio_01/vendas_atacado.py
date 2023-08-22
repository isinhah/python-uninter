# Exercicio 1 da atividade prática
print("Bem-vindo à Loja da Isabel Henrique")

# entrada de dados pelo usuário
valor_produto = float(input("Entre com o valor do produto: "))
quantidade_produto = int(input("Entre com a quantidade do produto: "))
desconto_produto = 0

# controle de fluxo
if quantidade_produto <= 200:
    desconto_produto = 0.00
elif 200 <= quantidade_produto < 1000:
    desconto_produto = 0.05
elif 1000 <= quantidade_produto < 2000:
    desconto_produto = 0.1
else:
    desconto_produto = 0.15

# calculo do desconto
total_sem_desconto = valor_produto * quantidade_produto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto

print(f"O valor SEM desconto: R$ {total_sem_desconto:.2f}")
print(f"O valor COM desconto: R$ {total_com_desconto:.2f}")
