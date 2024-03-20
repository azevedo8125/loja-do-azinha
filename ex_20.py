nome_comp = input('Digite o nome completo: ')#pede o nome completo

#separa os nomes e metem em lista
pala = nome_comp.split()

#seleciona o primeiro nome
pri_nome = pala[0]
#seleciona o ultimo nome
ult_nome = pala[-1]

#apresenta o resultado
print('primeiro nome:',pri_nome)
print('ultimo nome:',ult_nome)