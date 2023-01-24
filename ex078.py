li = list()
pm = int()
pn = int()
maior = int()
mn = int() 

for c in range(0, 5):
    li.append(int(input('Digite um número: ')))
    if c == 0:
        maior = mn = li[c]
    else:
        if li[c] > maior:
            maior = li[c]
            pm = c
        if li[c] < mn:
            mn = li[c]
            pn = c
print(f'O maior número digitado foi {maior} na posição {pm}')
print(f'O menor número digitado foi {mn} na posição {pn}')
print(li)

