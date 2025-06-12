#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).upper().strip()
nomec = nome.split()
check = int(len(nomec))
print (f'O nome completo é: {nome}\n'
       f'O primeiro nome seria: {nomec[0]}\n'
       f'O ultimo nome seria: {nomec[check-1]}. Correto?')
