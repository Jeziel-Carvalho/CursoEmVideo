#Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

#Seletor de conversor
num = int(input('Escreva um número inteiro: '))
print ('''Escolha uma das opções abaixo
       [1]Binário
       [2]Octal
       [3]Hexadecimal''')
opção = int(input('Sua opção: '))

#Condição aninhada (binário)
if opção == 1:
    binario = ''
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2
print(f'O número {num} em binário é: {binario}')

elif opção == 2:
    octal = ''
