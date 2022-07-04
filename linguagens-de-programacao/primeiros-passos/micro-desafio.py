# Equações de segundo grau
# Formula Y = a * x**2 + b * x + c

# Considerando os valores de  a = 2, b = 0.5 e c = 1,  
# solicitar para o usuário um valor de x e retornar o valor de y
#  correspondente ao x que ele digitou

a, b, c = 2, 0.5, 1

x = input("Digite o valor de x: ")

#conversão
x = float(x)

y = a * x**2 + b * x + c

print(f"O resultado de Y para X = {x} é {y}")

# em caso de erro retornado:
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

#Solução: verificar tipos de variáveis:

# print(type(a)) <class 'int'>
# print(type(b)) <class 'float'>
# print(type(c)) <class 'int'>
# print(type(x)) <class 'str'>

# no input entrou como string. É necessário venver ter para float usando
# x = float(x)







