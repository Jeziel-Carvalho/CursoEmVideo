#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
N1=float(input('Digite um número:'))
print(f'O número escolhido é {N1}, e seu inteiro será {trunc(N1)}')
