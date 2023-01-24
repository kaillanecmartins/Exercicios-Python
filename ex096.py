def area(lar, comp):
    a = lar * comp
    print(f'A área do terreno é de {a:.2f}m²')


area(float(input('Informe a largura do terreno: ')), float(input('Informe o comprimento do terreno: ')))
