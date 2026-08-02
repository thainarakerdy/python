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
    mostrar_estado(letras_descorbertas, erros, max_erros )