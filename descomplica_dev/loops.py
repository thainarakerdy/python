contador = 1

while contador >= 5:
    print("Contador: ",contador )
    contador += 1

print("Fim do loop while. \n") #o '\n' é usado para pular uma linha 

for i in range(1, 6):                   # Para cada valor dentro do range 
    print("Valor de i:", i)             #entre 1 e 6 vou imprimir o valor

print("Fim do loop for com range\n")


texto = "Thainara"

for letra in texto:
    print("Letra:", letra)

print("Fim do loop for com texto\n")

senha_correta = "304050"
senha = ""

while senha != senha_correta:
    senha = input("Digite a sua senha: ")

print("Acesso permitido")