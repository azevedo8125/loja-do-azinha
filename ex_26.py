from random import randint
from time import sleep

vel = randint(30, 220)

texto = f'MULTA DE VELOCIDADE \nData: 21 de fevereiro de 2024 \nLocal: Rua Principal Da zona, Cidade Favela \nVeículo: Fiat Punto \nPlaca: WG-12-DF \nCondutor: Mabululu dos Santos \nVelocidade Registrada: {vel} km/h em uma zona de 80 km/h'

def print_devagar(texto, atraso=0.05):
    for car in texto:
        print(car, end='', flush=True)
        sleep(atraso)
    print()

multa = vel - 80

preco = multa * 8

if vel <= 80:
    print('passou numa velocidade adequado')
else:
    print_devagar(texto)
    print(f'A multa é de {preco} €')
