from math import sqrt, pow
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = sqrt(pow(co,2) + pow(ca,2))
print('A hipotenusa do triangulo é: {:.2f}'.format(hp))
