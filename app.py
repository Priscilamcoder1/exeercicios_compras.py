# Solicita o valor da compra do usuário
valor_compra = float(input(" Digite o valor da compra:"))
#verifica se a compra é menor que R$ 200.
if valor_compra < 200:
    print("Desconto de 5%")
# Verifica se a compra está entre R$ 200 e R$ 299,99.
elif valor_compra >= 200 and valor_compra < 300:
    print("Desconto de 10%")
# Para compras de R$ 300 ou mais.
elif valor_compra >= 300:
    print("Desconto de 15%")
