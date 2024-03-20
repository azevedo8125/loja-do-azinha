notas = float(input('Insira a nota do seu aluno:'))

if notas > 20:
    print('A sua nota está inválida!')
elif 0 < notas <= 4 :
    print('A nota do seu aluno é muito baixa')
elif 4 < notas <= 9:
    print('A nota do seu aluno é negativa')
elif 9.5 < notas <= 13:
    print('A nota do seu aluno é positiva')
elif 13 < notas <= 16:
    print('A nota do seu aluno é boa')
elif notas < 0:
    print('A sua nota está inválida!')
else:
    print('A nota do seu aluno está excelente')
