#Exercício 8 e 9

#Escreva um programa que leia 3 números e calcule a média ponderada entre eles.
#Considere que o maior número recebe peso 5 e os outros dois recebem peso 2,5.


x = float(input("Digite um numero x: "))
y = float(input("Digite um numero y: "))
z = float(input("Digite um numero z: "))

peso1 = 5
peso2 = 2.5
peso3 = 2.5

maior = x 
segunda = y
terceira = z

if (y > maior):
    maior = y
    segunda = x
    terceira = z
if (z > maior):
    maior = z
    segunda = x
    terceira = y




media = ((maior*peso1) + (peso2*segunda) + (peso3*terceira)) / (peso1+peso2+peso3)
 
print("A média ponderada é: ",media)
