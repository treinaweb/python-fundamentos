nome, idade, sobrenome = "João", 20, "Silva"

print(nome, sobrenome, idade)

print("Olá, ", nome, sobrenome, "sua idade é", idade)
print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

nome2 = input("Digite o seu nome: ")
idade2 = int(input("Digite a sua idade: "))
sobrenome2 = input("Digite o seu sobrenome: ")

print(type(idade2))

print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")

soma_idades = idade + idade2
print(f"A soma das idades é: {soma_idades}")

subtracao_idades = idade - idade2
print(f"A subtração das idades é: {subtracao_idades}")

multiplicacao_idades = idade * idade2
print(f"A multiplicação das idades é: {multiplicacao_idades}")

media_idades = (idade + idade2) / 2
print(f"A média das idades é: {media_idades}")