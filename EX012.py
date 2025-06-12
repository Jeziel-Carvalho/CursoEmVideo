#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
# mas com 5% de desconto.
pp=float(input('Insira o preço do produto:'))
desc= pp*(5/100)
print(f'O valor com 5% de desconto será R${pp-desc:.2f}')
