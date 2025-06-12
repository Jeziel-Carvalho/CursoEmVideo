#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? KM'))
pass1 = 0.50
pass2 = 0.45
if distancia <= 200:
    print(f'A passagem custará R${distancia * pass1:.2f}')
else:
    print(f'A passagem custará R${distancia * pass2:.2f}')
