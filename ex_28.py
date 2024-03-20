#Faz um programa que mostre a soma de todos os 1) numeros impares que sao 2)
#Multiplos de 3 e que se 3)Encontrem num de 1 ate 500

soma_imp = 0
while True:
    num = int(input('Introduza um numero ímpar de 0 a 500\n(introduza 0 para finalizar o programa):'))
    if num == 0:
        print(f'O resultado final é:{soma_imp}')
        break
    if  1 <= num <= 500:
        if num % 2 == 1:
            soma_imp += num
            print(f'O resultado é: {soma_imp}')
        else: print('numero par')
    else: print('numero fora do intervalo')


'''while True:
    num = int(input('Introduza um numero ímpar de 0 a 500:'))
    num2 = int(input('Introduza outro numero (0 a 500)'))
    conta = num + num2
    if 500 > num < 0:
            print('numero invalida')
    elif num % 2 == 0:
            print("número ivalido")
    if 500 > num2 < 0:
            print('numero invalida')
    elif num2 % 2 == 0:
            print("número invalido")
    else:
            print("O Resultado é:",conta)
    break'''