#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
#um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Qual o Cateto Oposto?'))
ca = float(input('e qual é o Cateto Adjacente?'))
hip = hypot(co,ca)
print(f'Cateto Oposto {co}, Cateto Adjacente {ca}, e Hipotenusa {hip:.2f}.')
