#Exercício 3

#Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perímetro.


base = int(input("Digite o tamanho da base do retângulo: "))
altura = int(input("Digite o tamanho da altura do retângulo: "))

area = base*altura

perimetro = base + base + altura + altura

print("A área do retângulo é: " + str(area))
print("O perímetro do retângulo é: " + str(perimetro))

