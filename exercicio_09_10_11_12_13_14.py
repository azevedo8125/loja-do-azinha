# Exercicio 09
euro = float(input('Qual é a quantidade de euros que deseja converter:'))
# Dolar americano
dol = euro * 1.09
# Zloty Polaco
zlo = euro * 4.33
print('O total de euros em Dolar é:', dol)
print('O total de euros em Zloty Polaco é:', zlo) #apresenta os resultados
print('@' * 500)

alt = float(input('Qual é a altura da parede:'))#pede a altura da parede
larg = float(input('Qual é a largura da parede:'))#pede a largura da parede
# area da parede
area = alt * larg
# Descobrir litros de tinta necessarios
tinta = area / 2
print('A area da parede é:', area)
print('A parede vai precisar de ', tinta, ('litros'))#apresenta o resultado
print('@' * 500)

prod = float(input('Qual é o valor do produto:'))#pede o valor do produto
#descobre os 5% do produto
desc = prod * 0.05
final = prod - desc

print('O valor do produto com menos 5% é:', final, '€')
print('O valor descontado é:', desc, '€')
print('@' * 500)

prodt = float(input('Qual é o valor do produto:'))
dect = float(input('Qual é o desconto que vai desejar(max.1.00):'))

disc = prodt * dect #descobre a percentagem desejada
preco = prodt - disc

if (dect > 1.00):
    print('nao é possivel adicionar esse desconto porque exede o limite.')
else:
    print(('O valor do produto com menos'), disc, ('é:'), preco, '€')
    print('O valor descontado é:', disc, '€')
print('@' * 500)
cel = float(input('Quantos graus celsius deseja converter para fahrenheit:'))
fah = cel * 1.8 + 32
print(cel, 'ºC fica', fah, 'ºF')
print('@' * 500)

alug = float(input('Quantos dias o carro foi alugado:'))
Km = float(input('Quantos Kilometros o carro percorreu:'))

dias = 60 * alug
dist = 0.32 * Km

price = dias + dist
print('O valor que tem que pagar é:{:.2f}', price, ('€'))