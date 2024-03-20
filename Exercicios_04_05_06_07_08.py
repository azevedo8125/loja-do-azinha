import math

num = int(input('numero:'))
asuc = num - 1 # antecessor
suc = num + 1  #sucessor
print('O antecessor é:',asuc,'O sucessor é:',suc) #apresenta o resultado
print('='*500)#separações de programa

num2 = int(input('numero:'))
dobro = num2 * 2
triplo = num2 * 3
rq = math.sqrt(num2) #raiz quadrada
print('O dobro é=',dobro,
      '  O triplo é=',triplo,
      '  A raiz quadrada é', rq) #apresenta o resultado
print('='*500)#separações de programa

nota1 = int(input('Introduza a primeira nota:'))
nota2 = int(input('Introduza a segunda nota:'))

soma = nota1 + nota2
media = soma / 2 # calcula a media das duas notas
print('A media dos dois testes é:',media)#apresenta o resultado
print('='*500)#separações de programa

metros = int(input('Diga me quantos metros quer converter:'))
#conversão
con = metros / 1000
print('O resultado da conversão é:',con)#apresenta o resultado
print('='*500)#separações de programa

numt = int(input('introduza o numero que quer saber o numero:'))

x1 = numt * 1 #tabuada
x2 = numt * 2
x3 = numt * 3
x4 = numt * 4
x5 = numt * 5
x6 = numt * 6
x7 = numt * 7
x8 = numt * 8
x9 = numt * 9
x10 = numt * 10

print(numt,'x 1=',x1)
print(numt,'x 2=',x2) #apresenta a tabuada com resultado
print(numt,'x 3=',x3)
print(numt,'x 4=',x4)
print(numt,'x 5=',x5)
print(numt,'x 6=',x6)
print(numt,'x 7=',x7)
print(numt,'x 8=',x8)
print(numt,'x 9=',x9)
print(numt,'x 10=',x10)