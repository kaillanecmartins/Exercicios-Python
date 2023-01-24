dados = {'nome': input('Digite seu nome: '), 'media': float(input('digite sua média: '))}
if dados['media'] >= 7:
    dados['situacao'] = 'aprovado'
else:
    dados['situacao'] = 'reprovado'

print(f'{dados}')
