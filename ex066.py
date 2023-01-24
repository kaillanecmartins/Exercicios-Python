num, soma = 0, 0

while(num != 999):
    num = int(input('Digite um número: '))
    print('Para parar digite 999')
    if(num == 999):
        break
    soma += num
print('A soma dos números é {}'.format(soma))