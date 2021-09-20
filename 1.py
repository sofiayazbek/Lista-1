#Exercício 1

#Escreva um programa que leia três notas: p1, p2 e p3 (Entrar com valores entre 0 e 10). Calcule a média das notas, e apresente para o usuário. Caso a nota seja maior ou igual a 7, apresente que o usuário está 'Aprovado', caso contrário, apresente que o usuário está 'Reprovado'

a = float(input("Digite a sua nota da p1: "))
if not 0 <= a <= 10:
  raise ValueError("Entrar com valores entre 0 e 10")

b = float(input("Digite a sua nota da p2: "))
if not 0 <= b <= 10:
  raise ValueError("Entrar com valores entre 0 e 10")

c = float(input("Digite a sua nota da p3: "))
if not 0 <= c <= 10:
  raise ValueError("Entrar com valores entre 0 e 10")

media = (a+b+c)/3

print("A sua média é igual a: " + str(media))

if media>=7:
  print("Aprovado")

else:
  print("Reprovado")






