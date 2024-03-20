nome_cid = str(input('Introduza o nome da cidade:'))

#confirma se começa com vila
if(nome_cid.lower().startswith('vila')):
    print('A sua cidade começa com Vila')
else:
    print('A sua cidade nao começa com vila')