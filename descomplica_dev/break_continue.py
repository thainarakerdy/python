for numero in range (1, 11):
    if numero == 5:
        print("Numero 5 encontrado! encerrando loop com break!")
        break
    print("Numero:", numero)


for numero in range (1, 6):
    if numero == 3:
        print("PULANDO O NUMERO 3 COM CONTINUE")
        continue
    print("Numero:", numero)


#contador = 1 

#while True:
  #  print("Contador:", contador)
   # if contador == 10:
     #   print("Contador chegou a 10, saindo do looop com break")
     #   break
   # contador += 1

    conta2 = 0
    
    while conta2 < 30:
        conta2 += 1
        if conta2 == 25:
            print("Ignorando o numero 25 com o continue")
            continue
        print("Contador:", conta2)

##tô achando complicador colocar dois while com numeros 