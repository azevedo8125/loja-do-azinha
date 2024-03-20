count = 0
soma = 0
for c in range(0, 501, ):
        if c % 5 == 0:
                soma = soma + c
                count += 1
                print(c, end=' ')

print(f'\n{count} foram somados')
print(f'O resultado da soma é:{soma}')