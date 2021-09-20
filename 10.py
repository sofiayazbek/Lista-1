#Exercício 10

#Escreva um programa que leia um número inteiro de 1 a 7 e informe o dia da semana correspondente, sendo domingo o dia de número 1. Se o número não corresponder a um dia da semana, mostre uma mensagem de erro.


num = int(input("Digite um número de 1 a 7: "))
if num < 1 or num > 7 : 
  raise ValueError("Entrar com valores entre 1 e 7")

if num==1 :
  print("O dia da semana é: domigo")
if num==2 :
   print("O dia da semana é: segunda")
if num==3 :
  print("O dia da semana é: terça")
if num==4 :
   print("O dia da semana é: quarta")
if num==5 :
  print("O dia da semana é: quinta")
if num==6 :
   print("O dia da semana é: sexta")
if num==7 :
  print("O dia da semana é: sábado")




