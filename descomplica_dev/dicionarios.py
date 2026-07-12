aluno = {
    "nome": "Jariane",
    "idade": 46,
    "curso": "Contabilidade",
    "notas": [8, 9.0, 8.8]
}

print(aluno["nome"])

aluno["cidade"] = "Palmas"

#print(aluno)

aluno.pop("notas")

print(aluno)

del aluno ["curso"]

print(aluno)

print(aluno.keys()) #traz todas as chaves que o dicionario tem
print(aluno.values()) #traz todos os valores 
print(aluno.items()) #separa as chaves e os valores em pares

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

    # EXEMPLO


produtos = {
    "maça": 3.50,
    "banana": 4.88,
    "laranja": 2.99
}

carrinho = ["maça", "banana", "laranja", "banana"]

total = 0

for item in carrinho:
    total += produtos[item]

print("Carrinho: ", carrinho)
print("Total da compra: ", total)