import random

def escolher_palavra(): 
    """Escolhe e retorna uma palavra secreta aleatória"""
    palavras = ["energetico", "suco", "grafite", "garimpo"]
    return random.choice(palavras)

def mostrar_estado(letras_descorbertas, erros, max_erros):
    """Mostra na tela o estado atual do jogo"""
    print("n\Palavra:", " ".join(letras_descorbertas))
    print("Erros:", ", ".join(erros))
    print(f"Tentativas restantes: {max_erros - len(erros)}")

def verificar_vitoria(letras_descobertas):
    """Retorna True se o jogador descobriu todas as letras"""
    return "_" not in letras_descobertas

def jogar():
    """Executa o loop principal do jogo"""
    palavra_secreta = escolher_palavra()
    letras_descobertas = ["_"] * len(palavra_secreta)
    erros = []
    max_erros = 6

    print("Bem-vindo ao Jogo da Forca") 
    print("Tente adivinhar a palavra secreta")

while True:
    mostrar_estado(letras_descobertas, erros, max_erros)
    letra = input("\nDigite uma letra: ").lower()

    if letra in letras_descobertas or letra in erros:
        print("Você já digitou essa letra!")

    if letra in palavra_secreta:
        print(f"Boa! Você acertou a letra {letra} está na palavra")
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_descobertas[i] = letra
    else:
        print(f"A letra {letra} não está na palavra")
        erros.append(letra)

    if verificar_vitoria(letras_descobertas):
        print("\nParabéns! Você acertou. A palavra era: ", palavra_secreta)
        break

    if len(erros) >= max_erros:
        print("\n Game Over! Obrigado por jogar")
        print("A palavra secreta era: ", palavra_secreta)

if __name__ == "__jogo_forca_atualizado__":
    jogar()       
