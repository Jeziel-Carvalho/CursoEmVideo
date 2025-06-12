#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
#que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Quantos KM foram percorridos? '))
dia=int(input('Quantos dias ficou alugado? '))
pagar= (60*dia) + (0.15*km)
print(f'Você deve R${pagar:.2f} pelo aluguel do veiculo.')
