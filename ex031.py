km = float(input('Informe a distância da viagem: '))

if km < 200.0:
    valor = km * 0.5
    print('O valor da passagem é {}'.format(valor))
else:
    valor = km * 0.45
    print('O valor da passagem é {}'.format(valor))