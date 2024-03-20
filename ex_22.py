while True:
    try:
        nota1 = float(input('Insira a primeira nota do seu aluno:'))
        if 20 > nota1 < 0:
            print('Nota invalida')
        break
    except:
        print('Mete numeros!!')

while True:
    try:
        nota2 = float(input('Insira a segunda nota do seu aluno:'))
        if 20 > nota2 < 0:
            print('Nota invalida')
        break
    except:
        print('Mete numeros!!')
notas = (nota1 + nota2) / 2
# notas = media / 2

print('A sua média é:',notas)

'''if notas > 20:
    print('A sua nota está inválida!')'''
if notas <= 4 :
    print('A nota do seu aluno é muito baixa')
elif 4 < notas <= 9.5:
    print('A nota do seu aluno é negativa')
elif 9.5 < notas <= 13:
    print('A nota do seu aluno é positiva')
elif 13 < notas <= 16:
    print('A nota do seu aluno é boa')
else:
    print('A nota do seu aluno está excelente')
