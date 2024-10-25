from usuario import Usuario

usuario = Usuario("João", 10, "Silva")

for x in range(1, 10):

    print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")
    if x == 2:
        continue
    if x == 8:
        break

    print(x)
    if usuario.idade >= 18:
        print(f"{usuario.nome} é maior de idade")
    else:
        print(f"{usuario.nome} é menor de idade")
else:
    print("O loop entrou no else")

idade2 = 1
while idade2 != 0:
    nome2 = input("Digite o seu nome: ")
    idade2 = int(input("Digite a sua idade: "))
    sobrenome2 = input("Digite o seu sobrenome: ")
    usuario2 = Usuario(nome2, idade2, sobrenome2)

    if idade2 == 99:
        break

    if idade2 == 98:
        continue

    print(f"Olá, {usuario2.nome} {usuario2.sobrenome}, sua idade é {usuario2.idade}")

    media_idades = (usuario.idade + usuario2.idade) / 2
    print(f"A média das idades é: {media_idades}")

    if idade2 <= 17:
        print(f"{usuario2.nome} é adolescente")
    elif idade2 >= 18 and idade2 <= 50:
        print(f"{usuario2.nome} é adulto")
    else:
        print(f"{usuario2.nome} é idoso")
else:
    print("O loop entrou no else")