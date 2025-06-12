#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as possíveis informações sobre ele.
enter=input('Insira uma frase ou número:')
print('O tipo é:', type(enter))
print('É alfabético?', enter.isalpha())
print('É númerico?', enter.isnumeric())
print('É alfanumérico?', enter.isalnum())
print('Está em maiusculo?', enter.isupper())
print('Está em minusculo?', enter.islower())
print('Está capitalizada?', enter.istitle())
