#Faça um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade do veiculo: KM/H'))
limite = float(80)
excesso = velocidade - limite
multa = excesso * 7
if velocidade > limite:
    print(f'Você está em {velocidade:.0f}Km/h acima do limite de velocidade e foi multado!')
    print(f'O valor da multa é de R${multa:.2f}')
else:
    print('Você está dentro do limite da via, prossiga.')
