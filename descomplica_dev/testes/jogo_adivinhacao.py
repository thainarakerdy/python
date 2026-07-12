import random

numero_secreto = random.randint(1, 100)
tentativas_max = 7

print("Bem vindo(a) ao Jogo de Adivinhação!")
print("Tente adivinhar um número entre 1 a 100")
print(f"Você tem {tentativas_max} tentativas.\n")

for tentativa in range(1, tentativas_max + 1):
    palpite = int(input(f"Você está na tentativa {tentativa}, digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativa} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR do que o seu palpite!\n")
    else:
        print("O número secreto é MENOR do que o seu palpite!\n")

    if tentativa == tentativas_max:
        print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}!")

print("\n Fim do jogo. Obrigado por jogar!")        