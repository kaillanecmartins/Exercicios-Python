cidade = str(input('Digite o nome da sua cidade: ')).strip()
sep = cidade.split()
print('Cidade com o nome Santo? {}'.format('Santo' in sep[0]))
