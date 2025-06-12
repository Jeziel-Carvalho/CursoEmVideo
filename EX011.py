#Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta, pinta uma área de 2m²
altura=float(input('Insira a Altura:'))
largura=float(input('Insira a largura:'))
area= altura*largura
print(f'A quantidade de tinta necessária é {area/2:.1f}L')
