nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
sep = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(sep[0])))



