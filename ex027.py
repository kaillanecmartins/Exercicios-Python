nome = str(input('Digite seu nome completo: ')).strip()
sep = nome.split()
print('Seu nome completo é {}'.format(nome))
print('Seu primeiro nome é {}'.format(sep[0]))
n = nome.count(' ')
print('Seu último nome é {}'.format(sep[n]))