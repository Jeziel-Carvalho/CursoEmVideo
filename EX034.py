#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários acima de R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é seu atual salário? R$'))
print('-=-'*15)
if salario > 1250:
    print(f'Com aumento, seu novo salário será R${salario*10/100+salario:.2f}!!')
else:
    print(f'Com aumento, seu novo salário será R${salario*15/100+salario:.2f}!!')
