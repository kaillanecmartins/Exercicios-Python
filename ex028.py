import random
num = random.randint(0, 5)
adv = int(input('Digite um número de 0 a 5: '))
if adv == num:
    print('Parabéns! Você acertou!')
else:
    print('que pena, você errou')