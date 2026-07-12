#Para fazer listas é melhor definir uma variável que seja multidirecional, ou seja, que dê para fazer o input de vários valores em uma única variável

#Exemplo de lista abaixo

inventario = [] #o colchete é usado para dizer que a variável está aberta e que vai adicionar os valores depois
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número de série: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

    # .append() está inserindo os dados digitados na lista do inventário
    # .upper() está sendo usado para mesmoo que digitar-mos em minusculo, o sistema vai ler ele como maiusculo

for elemento in inventario:
    print(elemento)

    #A lista simples é para poucas entradas, se tiver mais do que 5, é melhor usar a lista múltiplas