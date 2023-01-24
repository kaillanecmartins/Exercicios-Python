import math
ag = int(input('Digite um ângulo: '))
se = math.sin(ag)
co = math.cos(ag)
tg = math.tan(ag)
print('O seno de {} é {:.2f}'.format(ag, se))
print('O cosseno de {} é {:.2f}'.format(ag, co))
print('A tangente de {} é {:.2f}'.format(ag, tg))