from random import sample
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
print('Ordem de apresentação: {}'.format(sample([a1, a2, a3, a4], k=4)))