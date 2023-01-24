r1 = float(input('Informe o comprimento da reta: '))
r2 = float(input('Informe o comprimento da reta: '))
r3 = float(input('Informe o comprimento da reta: '))

if r1 > (r2 - r3) and r1 < (r2 + r3):
    print('As retas formam um triângulo')
else:
    print('As retas não podem formar um triângulo')

