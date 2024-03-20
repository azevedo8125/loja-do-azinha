import random

print("Bem-vindo ao jogo Par ou Ímpar!")
print('+' * 50)

vitorias_jogador = 0
vitorias_computador = 0

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
        print("Parabéns, você ganhou esta rodada!")
        vitorias_jogador += 1
    else:
        print("Você perdeu esta rodada. O computador ganhou!")
        vitorias_computador += 1

    print(f"Pontuação atual: Jogador {vitorias_jogador} - {vitorias_computador} Computador")

    if vitorias_jogador == 10 or vitorias_computador == 10:
        vencedor = "Jogador" if vitorias_jogador == 10 else "Computador"
        print(f"{vencedor} venceu! Parabéns!")
        break


        print("Obrigado por ter jogado. Até a próxima!")
        break
