print("Restaurante do quilo")

preco_quilo = float(input("Informe o valor do quilo! "))
peso_prato = float(input("Informe o peso do prato do cliente (em kg) " ))

preco_prato = preco_quilo * peso_prato

print(f"O valor do prato é R${preco_prato:.2f}")

if peso_prato > 1:
    print("Como o valor do prato do cliente ultrapassou 1kg, ele deve pagar o valor fixo de R$89,99")