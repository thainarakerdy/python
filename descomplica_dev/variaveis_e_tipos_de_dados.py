# idade = 23 # inteiro
# print(idade)
# print(type(idade))

# altura = 1.75 # float
# print(altura)
# print(type(altura))

#nos float quando queremos que a casa decimal fique apenas em 2 usamos dentro das chaves os dois pontos, ponto final, dois e f ({:.2f})

# nome = "Maria" # String (str)
# print(nome)
# print(type(nome))

# estudando = False
# print("Está estudando?, estudando, "| Tipo:", type(estudando))

# frutas = ["maçã", "banana", "laranja"] # List = podemos mudar a ordem e mudar os valores, retirar e adicionar
# print(frutas)
# print(type(frutas))

# cores = ("vermelho", "azul", "marsala") # Tupla (tuple) é parecido com o "List" pórem não pode ser alterado, ou seja, não pode adicionar e muito menos mudar o que foi colocadoo até o final do código
# print(cores)
# print(type(cores))

# aluno = {"nome": "Maria", "idade": 25, "curso": "Engenharia"} # Dicionário (dict) é uma variável com várias outras variáveis dentro
# print(aluno)
# print(type(aluno))

# numeros = {1, 2, 3, 3, 2, 1} # conjunto (set) é uma coleção não ordenada de itens únicos, ou seja, não repete os números que foram ccolocados mais de uma vez
# print(numeros)
# print(type(numeros))

#quando eu quero uma quebra de linha é usado \n e quando eu quero uma tabulação eu uso \t, vou da exemplo abaixo

texto = "quero uma quebra de linha depois daqui \n e quero uma tabulação na ultima \tpalavra\n"
print(texto)

# .capitalize() 
    #serve para deixar apenas a primeira letra em maiusculo e o resto em minusculo // só funciona se não tiver espaço na frente

# .upper()
    #serve para deixar todo o texto em maiusculo

# .lower()
    #serve para deixar tudo em minusculo

texto2 = "exemplo na PRATICA"

print(texto2.capitalize())

print(texto2.upper())

# .startswith("")
    #serve para verificar se o meu texto começa com uma determinada letra, ele vai responder com verdadeiro ou falso

# .endswifth("")
    #é para verificar se o meu texto termina com algum caractere especial ou com alguma letra em especifico, TAMBÉM vai me dizer apenas true or false

# .count("")
    # serve pra contar quantas vezes aquele caracter ou letra se repitiu no sistema

# Tem também a possibilidade de saber se uma palavra ou caracter em especifico está em algum texto ou em algum lugar no sistema EXEMMPLO: print("palavra" in variavel) isso quer dizer que está perguntando se a palavra que desejamos está na variavel que queremos saber

# .replace("", "")
    # é usada para quando queremos modificar uma palavra ou caracter na nossa variavel só que só na saida e não no sistema inteiro. OBS: primeiro colocamos dentro da primeira aspas a palavra que queremos substituir e na segunda aspas colocamos a palavra que queremos que apareça 

# .append()
    #é para inserir o dado que foi digitado 'input', na lista que está sendo feita

# .insert("")
    #é para inserir o dado que foi digitado 'input', escolhendo a posição exata (o índice) onde deseja colocar o elemento.

# .extend("", "")
    #é para adicionar elementos a uma lista que já existe, ou seja, colocar uma nova lista dentro de uma lista já existente

# .remove("")
    #é para eliminar um elemento de uma lista, ou seja um dado, pelo nome dele

# del 'variável' []
    #deleta da variavel identificando qual é a posição do item que você quer remover

# .pop()
    #é para remover com base na posição do dado. Se não colocar a posição, ele remove o último

# .clear()
    #é para deletar toda a lista 

# .strip()
    #é para remover todos os espaços em branco que aparecem no início e no fim de uma string. Ele não mexe nos espaços que estão no meio do texto

# .split()
    #é para dividir ou partir uma string em várias partes, transformando-a numa lista de strings

# .join()
    #é para juntar os elementos de uma lista de volta em uma única string
    
# len()
    #é para descobrir quantos itens eu tenha na minha lista.                            EXEMPLO: print("tamanho da lista: ", len(numeros))

# max()
    #é utilizado para saber qual é o MAIOR valor que eu tenho dentro da minha lista

# min()
    #é usado para saber qual é o MENOR valor que tem dentro da minha lista

# sum()
    #é para quando eu quiser SOMAR todos os valores da minha lista 

# .sort()
    #é para ordernar a lista do menor para o maior

# .reverse()
    #é para quando eu quero uma lista invertida, ou seja, do maior para o menor