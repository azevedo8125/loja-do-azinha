num = int(input('Introduza um número entre 0 e 9999: '))

#verifica se ta no intrevalo0-9999
if 0 <= num <= 9999:

    num_str = str(num).zfill(4)

    uni = list(num_str)

    # Apresentar o resultado
    print('Número original:', num)
    print('Milhar:', uni[0])
    print('Centena:', uni[1])
    print('Dezena:', uni[2])
    print('Unidade:', uni[3])
    print('Número com todas as unidades:', ''.join(uni))
else:
    print('O número está fora do intervalo.')