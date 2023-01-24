from random import randint
num = randint(1, 10)
nj = int(input('Tente adivinhar o número: '))
cont = 1

while(nj != num):
    print('Você errou, tente novamente')
    nj = int(input('digite um número: '))
    cont += 1
print('Você acertou com {} tentativas'.format(cont))