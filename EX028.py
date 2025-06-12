#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
numero = randrange(0,5) #Computador escolhe um número
print ('Estou pensando em um número entre 0 e 5.\n Consegue adivinhar?')
resposta = int(input('Eu acho que o número é... ')) #Jogador adivinha o número
if numero == resposta:
    print(f'Você acertou, o número era {numero} PARABÉNS!!')
else:
    print(f'Você errou, o número era {numero}.')
