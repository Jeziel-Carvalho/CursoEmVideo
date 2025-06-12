#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang=float(input('Me informe um ângulo:'))
rad= radians(ang)
calc1= sin(rad)
calc2= cos(rad)
calc3= tan(rad)
print(f'O ângulo é {ang} e seus dados são:\n'
      f'Seno= {calc1:.3f}\n'
      f'Cosseno= {calc2:.3f}\n'
      f'Tangente= {calc3:.3f}')
