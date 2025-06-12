#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nomecompleto = str(input('Insira seu nome completo: ')).strip()
nomemaiusculo = nomecompleto.upper()
nomeminusculo = nomecompleto.lower()
espaco = nomecompleto.strip()
separado = nomecompleto.split()
print (f'Nome em maiusculo: {nomemaiusculo}\n'
       f'Nome em minusculo: {nomeminusculo}\n'
       f'Quantidade de letras: {len(espaco)-espaco.count(' ')}\n'
       f'Quantidade de letras do 1°nome: {len(separado[0])}')
