nome = str(input('Introduza o seu nome completo:')).strip()

nome_lit = nome.split()

pri_nome = nome_lit[0]
ult_nome = nome_lit[-1]4bn

print(f'O seu primeiro nome é {nome_lit[0]}')
print(f'O seu ultimo nome é {nome_lit[-1]}')