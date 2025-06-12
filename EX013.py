#Faça um algoritmo que leia o salário de um funcionário e mostre
#seu novo salário com 15% de aumento.
salario = float(input('Qual o salário atual?'))
aumento = salario*(15/100)
print(f'Com o aumento o salário irá de {salario:.2f} para {salario+aumento:.2f}')
