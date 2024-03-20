soma_imp = 0
tent = -1

while True:
    try:
        num = int(input('Introduza um numero de 0 a 998\n(introduza 999 para finalizar o programa): '))
        tent += 1
        if num == 999:
            print(f'O resultado final é: {soma_imp}')
            print(f'Você introduziu {tent} numeros.')
            break
        elif 1 <= num <= 998:
            soma_imp += num
            print(f'O resultado é: {soma_imp}')
        else:
            print('Número fora do intervalo.')
    except ValueError:
        print('Por favor, insira um número válido.')

