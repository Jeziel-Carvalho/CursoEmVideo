#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase = str(input('Escreva uma frase/palavra: ')).lower().strip()
print (f'A letra A aparece {frase.count('a')} vezes.\n'
       f'A primeira letra A aparece na posição {frase.find('a')+1}.\n'
       f'A ultima letra A aparece na posição {frase.rfind('a')+1}.')
