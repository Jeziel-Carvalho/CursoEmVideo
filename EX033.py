#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = input('Insira um número: ')
n2 = input('Digite outro número: ')
n3 = input('Digite mais um número: ')
numeros = [n1,n2,n3]
acerto = sorted(numeros)
print(f'Do menor para o maior: {acerto}')
