nome = str(input('Escreva o seu nome completo:'))

#mete o nome em maiusculas
nome_ma = nome.upper()
#mete o nome em minusculas
nome_mi = nome.lower()
# mete a primeira letra em maiusculas
nome_cap = nome.capitalize()
# separa os nome
pri_nome = nome.split()[0]
#conta os caracteres do primeiro nome
tam_pri_nome = len(pri_nome)
#remove os espaços
nome_sem = nome.replace(" ", "")

print('O nome é:',nome)
print('O nome em maiúsculas é:',nome_ma)
print('O nome em minusculas é:',nome_mi)
print('O nome com as primeiras letras em maiúsculas:',nome_cap)
print('O primeiro nome tem',tam_pri_nome,'letras')
print('O nome sem espaços é:',nome_sem)