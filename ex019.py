import random
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')
sorteado = random.choice([a1, a2, a3, a4])
print('O aluno sorteado foi {}'.format(sorteado))
