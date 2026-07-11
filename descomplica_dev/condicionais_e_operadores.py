idade = 19

if idade >= 18:
    print("já pode ser preso")
else: 
    print("tá save")
#parece que da pra colocar tanto >= quanto >- para falar que é maior ou igual 
#o 'if else' de java aqui em python é 'elif', ou seja toda vez que eu quiser usar o if e depois o else porém quero colocar um if else no meio, tenho que usar o elif

#para fazer duas condicionais juntas usasse o 'and' vou fazer um exemplo abaixo

idade2 = 15
tem_identidade = True

if idade >= 12 and tem_identidade:
    print("Adolescente com identidade")
elif idade >= 18 and tem_identidade:
    print("jovem com identidade")
else:
    print("sem idade confirmada e sem identidade")

# É necessário tambem colocar dois pontos (:) no if else e elif para poder funcionar

# ou se quiser que qualquer uma das duas condições seja atendida a gente usa o 'or' vou fazer um exemplo abaixo

cachorro = True
gato = False
peixe = True

if cachorro or gato:
    print("Você tem ambos")
elif peixe: 
    print("Você não tem gato e nem cachorro")
else:
    print ("não tem nenhum")

