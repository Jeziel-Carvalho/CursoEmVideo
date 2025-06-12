#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

ladoa = float(input('Qual o comprimento do segmento A? '))
ladob = float(input('Qual o comprimento do segmento B? '))
ladoc = float(input('Qual o comprimento do segmento C? '))
if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladob + ladoa:
    print('Os segmentos ABC podem formar um triângulo!!')
else:
    print('Os segmentos ABC não podem formar um triângulo!!')
