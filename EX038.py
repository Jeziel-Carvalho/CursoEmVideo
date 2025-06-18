#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela:
#O maior número
#Se os dois são iguais
#Ou se o segundo é maior

from time import sleep

#Entrada de dados
n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
print (f'Os número inseridos foram {n1} e {n2}.')
print ('='*24)
print('Analisando...')
print ('='*24)

sleep(3)

#Condição
if n1 > n2: print (f'O maior número é {n1}')
elif n2 > n1: print (f'O maior número é {n2}')
else: print ('os dois são iguais.')
