print("Cadastro de doadores de sangue")
nome = input("Digite o seu nome completo: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2026 - ano_nascimento

peso_minimo = 45
idade_minimma = 16

if idade < idade_minimma:
    print("Abaixo da idade minima exigida")
elif peso < peso_minimo:
    print("Peso insuficiente para a doação")
else:
    print(f"Pode doar sangue, obrigado {nome}")