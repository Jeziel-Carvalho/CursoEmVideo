#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

#Titulo do programa:
print ('='*24)
print ('\033[1;33mSIMULADOR DE EMPRESTIMO\033[0m')
print ('='*24)

#Entrada de dados à simular:
valor = float(input('Qual o valor da casa? R$'))
anos = int(input('Em quantos anos pretende pagar? Insira apenas números: '))
salario = float(input('Qual é seu salário atual? R$'))


#Calculo da prestação mensal:
prestacao = anos*12
mensal = (valor/prestacao)
porcento = salario*(30/100)

print('Calculando...')
sleep(3)
print('Gerando resultado...')
sleep(3)

#Condição de aprovação
if mensal<porcento:
    print('Emprestimo recusado, parcela excede 30%.')
else:
    print('Emprestimo aprovado, parcela em conforme.')
