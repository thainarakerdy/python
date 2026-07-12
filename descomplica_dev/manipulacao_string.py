texto = " Aprendendo Python "

print("Texto original: ", texto)

# .strip() , para remover os espaços em branco que tem antes e depois do texto
print("strip():", texto.strip())

# .upper() , para deixar tudo maiusculo
print("upper():", texto.upper())

# .lower() , para deixar tudo minusculo
print("lower():", texto.lower())

# .capitalize() , para deixar apenas a primeira letra em maiusculo
print("capitalize():", texto.capitalize())

# .count("") , para contar quantas vezes aquele caracter ou letra se repitiu no sistema
print("count():", texto.count("n"))

# .startswith("") , para verificar se o texto começa com uma determinada letra, ele vai responder com verdadeiro ou falso
print("startswith():", texto.startswith("Py"))

# .endswith("") , para verificar se o texto termina com uma determinada letra, ele vai responder com verdadeiro ou falso
print("endswith():", texto.startswith("Py"))

# .split() , é para dividir ou partir uma string em várias partes, transformando-a numa lista de strings
print("split():", texto.split())

#.join() , é para juntar os elementos de uma lista de volta em uma única string
palavra = ["Aprendendo" "Python"]
print("join():", "  ".join(palavra))