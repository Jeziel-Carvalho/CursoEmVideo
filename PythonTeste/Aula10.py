tri1 = float(input('Qual a 1°Nota? '))
tri2 = float(input('Qual a 2°Nota? '))
tri3 = float(input('Qual a 3°Nota? '))
media = (tri1+tri2+tri3)/3
if media >= 60:
    print(f'Parabéns sua média é {media:.0f}\n'
          'Você está aprovado!!')
else:
    print(f'Sua média é {media:.0f}.\n'
          f'Você está reprovado.')
print('Tenha um Bom dia!')