def saudacao():
    print("Olá! Seja bem vindo")

saudacao()

def apresentar(nome, idade):
    print(f"Meu nome é {nome} e eu tenho {idade} anos")

apresentar("Thainara", 23)
apresentar("Eduardo", 23)

def soma(n1, n2):
   return n1 + n2
resultado = soma(5,3)
print(f"O resultado é {resultado}")

def cumprimentar(nome = "Visitante"):
    return f"Olá, {nome}!"

print(cumprimentar("Thainara"))
print(cumprimentar())

def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

notas = [8.0, 8.9, 6.4, 5.9]
media = calcular_media(notas)
print("Notas: ", notas)
print("Média: ", media)