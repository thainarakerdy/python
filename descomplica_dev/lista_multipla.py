equipamentos = []
valores = []
numero_de_serie = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valores: ")))
    numero_de_serie.append(int(input("Número de série: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..:", valores[indice])
        print("Número de série.: ", numero_de_serie[indice])