si = 0
for c in range(1, 500):
    if c%2 != 0 and c%3 == 0:
        si += c
print('A soma dos impares múltiplos de 3 é', si)