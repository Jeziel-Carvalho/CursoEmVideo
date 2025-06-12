#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
entrada = int(input('Insira um número de 0 a 9999: '))
U= entrada // 1 % 10
D= entrada // 10 % 10
C= entrada // 100 % 10
M= entrada // 1000 % 10
print (f'Unidade {U}\n'
       f'Dezena {D}\n'
       f'centena {C}\n'
       f'Milhar {M}')