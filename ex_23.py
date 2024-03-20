from random import randint
from time import sleep
print('#'*300)
print('gerando um numero de 0 entre 5')
print('#'*300)
nralea = randint(0, 5)
nr1 = int(input('Introduz o numero que voce pensa que é:'))
print('pensando......')
sleep(2)
if nr1 == nralea:
    print('Parabens voce acertou!!')
else:
    print(f'O meu numero era \033[31m{nralea}\033[m o teu era \033[32m{nr1}\033[m erraste')