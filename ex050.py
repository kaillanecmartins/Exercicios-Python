sp = 0

for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n%2 == 0:
        sp += n
print('Soma dos pares:', sp)
