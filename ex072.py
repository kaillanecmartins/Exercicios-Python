nums = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']

n = int(input('Digite um número: '))
if(n < len(nums)):
    print('O número {} por extenso é {}'.format(n, nums[n]))
else:
    print('O número não existe na lista')