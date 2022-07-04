#Formatadores de caracteres

#Exemplos:

#modelo 1: usando formatadores
nome = input("Digite seu nome: ")
print("Ola %s, bem vindo(a). Parabéns"%(nome))

#modelo 2: usando funcao format()
nome = input("Digite seu nome: ")
print("Ola {}, bem vindo(a). Parabéns".format(nome))

#modelo 3: usando strings formatadas (f-strings)
nome = input("Digite seu nome: ")
print(f"Ola {nome}, bem vindo(a). Parabéns")

#f-strings é o modelo recomendado PEP-498
