from random import randint
from time import sleep

print('#'*300)
print('Gerando um número entre 0 e 5')
print('#'*300)

nralea = randint(0, 5)
tent = 0

nr1 = int(input('Introduza o número que você pensa que é:'))
tent += 1

print('Pensando......')

if nr1 == nralea:
    print(f'Parabéns, você acertou em {tent}!!')

while nralea != nr1:
    try:
        nr2 = int(input('Introduza outro número, você errou:'))
        tent += 1
        print('Pensando......')
        sleep(2)
        if nr2 == nralea:
            print(f'Parabéns, você acertou em {tent}!!')
            break
    except ValueError:
        print('Por favor, insira um número válido.')
