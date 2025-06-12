#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celc = float(input('Qual a atual temperatura? C°'))
print(f'A temperatura é {celc:.1f}C°\ne sua conversão é {celc*1.8+32:.1f}F°.')
