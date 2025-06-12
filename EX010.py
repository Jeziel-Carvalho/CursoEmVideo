#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar. (CONSIDERE O VALOR ATUAL DO DÓLAR)
Vdolar=float(input('Qual o valor atual do $?'))
carteira=float(input('Quantos R$ você tem?'))
print(f'Com R${carteira}, você pode adquirir US${carteira/Vdolar:.2f}')
