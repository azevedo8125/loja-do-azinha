while True:
    nr = int(input('Introduza o numero que deseja saber a tabuada (insira um numero negativo para sair):'))
    if nr < 0:
        print('Programa fechado')
        break
    print(f'Tabuada do {nr}')

    max_length = len(str(nr * 10))

    for tab in range(1, 11):
        resultado = nr * tab
        print(f'{nr} X {str(tab).rjust(2)} = {str(resultado).rjust(max_length)}')
