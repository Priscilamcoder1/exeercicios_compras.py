valor_compra = float(input(" Digite o valor da compra:"))
if valor_compra < 200:
    print("Desconto de 5%")
elif valor_compra >= 200 and valor_compra < 300:
    print("Desconto de 10%")
elif valor_compra >= 300:
    print("Desconto de 15%")