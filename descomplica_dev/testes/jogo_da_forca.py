import random # é uma biblioteca aleatoria

palavras = ["python", "programacao", "computador", "algoritmo", "forca"]

palavra_secreta = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra_secreta)

erros = []

max_erros = 6

print("Bem-vindo ao Jogo da Forca!")
print("Adivinhe a palavra secreta")
print(" ".join(letras_descobertas))

while True:
    letra = input("\nDigite uma letra:").lower()

    if letra in letras_descobertas or letra in erros:
        print("Você já tentou essa letra")
        continue
    if letra in palavra_secreta:
        print(f"Boa! A letra '{letra}' está na palavra.")
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_descobertas[i] = letra
    else:
        print(f"A letra '{letra}' NÃO está na palavra")
        erros.append(letra)

    print("Palavras:", " ".join(letras_descobertas))
    print("Erros:", ", ".join(erros))
    print(f"Tentativas restantes: {max_erros - len(erros)}")

    if "_" not in letras_descobertas:
        print("Parabéns! Você vence! A palavra era",  palavra_secreta)
        break
    if len(erros) >= max_erros:
        print("\nGame over!")
        print("A palavra secreta era:", palavra_secreta)
        break