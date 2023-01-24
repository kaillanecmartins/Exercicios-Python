v = int(input('Informe sua velocidade atual: '))
if v > 80:
    print('Você foi multado por estar acima da velocidade permitida')
    multa = (v - 80) * 7
    print('Terá que pagar {} reais'.format(multa))
else:
    print('Sua velocidade é aceitável')