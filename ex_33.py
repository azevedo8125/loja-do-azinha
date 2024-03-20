def estatisticas_pessoas():
    total_pessoas = 0
    m_18 = 0
    mulheres = 0
    h_20 = 0
    dif = 0

    while True:
        idade = int(input("Digite a idade da pessoa: "))
        sexo = input("Digite o sexo da pessoa (M/F/D): ").upper()

        total_pessoas += 1

        if idade > 18:
            m_18 += 1

        if sexo == 'F':
            mulheres += 1

        if sexo == 'M' and idade < 20:
            h_20 += 1

        if sexo == 'D':
            dif += 1

        continuar = input("Deseja continuar introduzindo dados? (S/N): ").upper()
        if continuar != 'S':
            break

    print("\nEstatísticas:")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Pessoas com mais de 18 anos: {m_18}")
    print(f"Total de mulheres: {mulheres}")
    print(f"Homens com menos de 20 anos: {h_20}")
    print(f"Total de diferenciados: {dif}")

if __name__ == "__main__":
    estatisticas_pessoas()
