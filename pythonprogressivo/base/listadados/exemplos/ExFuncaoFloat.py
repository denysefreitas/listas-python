#Vamos criar um script que pede um decimal para o usuário e armazena na variável var1. Depois, imprimimos o tipo de dado dessa var1, que vai ser 'str'.

# Depois, colocamos essa var1 dentro da função float() e armazenamos o valor em uma variável var2. Em seguida, imprimimos o tipo de dado dessa variável, que vai ser 'float'.

var1 = input("Informe um número decimal: ")
print(type(var1))

var2 = float(var1)
print(type(var2))
print(var2)