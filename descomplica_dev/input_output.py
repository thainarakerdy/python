nome1 = "Nágila"
nome2 = "Caio"

#print(nome1, nome2)

#print(f"O nome 1 é {nome1} e o nome 2 é {nome2}.") #desse jeito dá pra misturar as strings na variável

#print("O nome 1 é {} e o nome 2 é {}." .format(nome1, nome2))

#o Scanner sc = new Scanner() do java é "input()" aqui no python
nome_usuario = input("Digite o seu nome: ")
print(f"Bem vindo(a) {nome_usuario}!") #Pelo o que eu entendi é necessário colocar esse f antes das aspas quando quer colocar um texto e uma variável, pode colocar também o '.format(variável)' e ccolocar a chaves no texto onde você quer a variável

#se não converter o input para outro tipo de variável, ele sempre vai dá o valor como 'String', ou seja, se quiser que um valor seja um número inteiro vai ter que colocar 'int(input())'
#para umm número quebrado, ou seja, o float vai ficar 