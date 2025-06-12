#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
aluno=input('insira o nome do aluno:')
t1=float(input('Nota 1Trimestre:'))
t2=float(input('Nota 2Trimestre:'))
print(f'A média de {aluno} é {(t1+t2)/2:.2f} ')
