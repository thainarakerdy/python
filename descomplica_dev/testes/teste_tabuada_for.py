tabuada = int(input("Digite um número para a tabuada: "))
print("Tabuada do número: ", tabuada)

for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str(tabuada*valor))


# É necessário colocar esse str(tabuada) se não dá erro de sintaxe, tentei colocar o int no lugar porém da erro do mesmo jeito