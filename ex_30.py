import random

print("Bem-vindo ao jogo Par ou Ímpar!")
print('+' * 50)

vitorias = 0

while True:
    esc_jogador = input('Escolha Par[P] ou Ímpar[I]: ').upper()

    if esc_jogador not in ['P', 'I']:
        print('Introduza uma letra válida (P ou I)')
        continue

    try:
        nr_jogador = int(input('Escolha um número [0-10]: '))
    except ValueError:
        print('Introduza um número válido')
        continue

    nr_pc = random.randint(0, 10)
    print(f'O computador escolheu o número: {nr_pc}')

    soma = nr_pc + nr_jogador
    print(f"A soma dos números é {soma}.")

    resultado = "P" if soma % 2 == 0 else "I"

    if resultado == esc_jogador:
        print("Parabéns, você ganhou!")
        vitorias += 1
    else:
        print("Tu perdeste. Tente novamente.")

    if vitorias == 0:
        print("O computador diz: 'Fogo, tu perdeste mais uma vez mesmo fraco.'")
    elif vitorias == 1:
        print("Tu disseste: 'Ok, ok, você ganhou uma vez. Mas na próxima vez eu ganho!'")
    else:
        print(f"Tu ganhaste {vitorias} vezes!")

    jogar_dnv = input("Deseja jogar novamente? (S/N): ").upper()

    if jogar_dnv != 'S':
        print("Obrigado por ter jogado. Até a próxima!")
        break
