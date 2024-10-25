nome, idade, sobrenome = "João", 20, "Silva"

print(nome, sobrenome, idade)

print("Olá, ", nome, sobrenome, "sua idade é", idade)
print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

nome2 = input("Digite o seu nome: ")
idade2 = int(input("Digite a sua idade: "))
sobrenome2 = input("Digite o seu sobrenome: ")

print(type(idade2))

print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")