#O professor quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
alunos= str(input('Insira o nome dos alunos: '))
embar= (f'{alunos}'.split())
shuffle(embar)
print (f'A ordem de apresentação é:\n'
       f'{embar}')
