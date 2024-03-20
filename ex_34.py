def main():
    numbers = []

    while True:
        nr = input("Insira um número (ou '0' para terminar): ")

        if nr == '0':
            break
        try:
            num = int(nr)
            numbers.append((num, len(numbers)))
        except ValueError:
            print("Por favor, insira um número válido.")

    total = sum(num[0] for num in numbers)

    print("Números inseridos:")
    for num in numbers:
        print("Número:", num[0], "Posição:", num[1])
    print("Soma dos números:", total)

if __name__ == "__main__":
    main()
