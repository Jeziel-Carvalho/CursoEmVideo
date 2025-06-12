#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Insira seu nome completo: '))
corte = nome.lower()
print (f'Contém SILVA no nome? {'silva' in corte}')
