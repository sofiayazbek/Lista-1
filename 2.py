#Exercício 2

#Escreva um programa que leia três números inteiros. E apresente qual foi o maior.


x = int(input("Digite um numero x: "))
y = int(input("Digite um numero y: "))
z = int(input("Digite um numero z: "))

maior = x

if (y > maior):
    maior = y
if (z > maior):
    maior = z

print('O maior número é: ',maior)