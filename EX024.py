#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Qual o nome da cidade? '))
separacao = cidade.lower().split()
corte = separacao[0]
print (f'O nome da cidade começa com SANTO? {'santo' in corte}')
