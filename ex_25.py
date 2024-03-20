from random import randint
from time import sleep

print('#' * 100)
print('Gerando um número entre 0 e 100')
print('#' * 100)

nralea = randint(0, 100)
tent = 0

print('Pensando......')

while True:
    try:
        nr1 = int(input('Introduza um número: '))
        tent += 1

        if nr1 == nralea:
            print(f'Parabéns, você acertou em {tent} tentativas!!')
            break
        elif nr1 < nralea:
            print(f'O número é maior que {nr1}')
        elif nr1 > nralea:
            print(f'O número é menor que {nr1}')

        print('Pensando......')
        sleep(2)
    except ValueError:
        print('Por favor, insira um número inteiro válido.')
