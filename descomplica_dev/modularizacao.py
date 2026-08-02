# A MODULARIZAÇÃO serve para dividir um programa em partes menores (funções e módulos)
# Vantagens:   - Organização de códigos
#              - Reutilização de funções
#              - Facilitar a manutenção
#              - Melhor colaboração em equipe


# EXEMPLO SEM MODULARIZAÇÃO:

# 1 - Código sem modularização

print("=== Cálculo de Áreas ===")
base = 10
altura = 5 
area_retangulo = base * altura
print("Área do retângulo:", area_retangulo)

raio = 7 
area_circulo = 3.14 * (raio ** 2)
print("Área do Círculo:", area_circulo)

# 2 - Código com modularização

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_circulo(raio):
    return 3.14 * (raio ** 2)

print("Área do retângulo:", calcular_area_retangulo(15,6))
print("Área do Círculo:", calcular_area_circulo(8))

