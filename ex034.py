salario = float(input('Informe seu salário: '))

if salario > 1250.0:
    aumento = salario + (salario * 0.10)
    print('Seu novo salário é {:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('Seu novo salário é {:.2f}'.format(aumento))