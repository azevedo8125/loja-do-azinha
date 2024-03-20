def log_admin():
    username = input("Digite o nome de utilizador: ")
    password = input("Digite a senha: ")

    if username == "Mario" and password == "Balotelli":
        return True
    else:
        return False

def mostrar_prod():
    try:
        with open("produtos.txt", "r") as file:
            print("Produtos:")
            for line in file:
                produto, preco = line.strip().split(", ")
                print(f"{produto} - {preco}€")
    except FileNotFoundError:
        print("O arquivo de produtos ainda não foi criado.")

def adicionar_produtos():
    try:
        with open("produtos.txt", "a") as file:
            while True:
                produto_nome = input('Digite o nome do produto ou "sair" para sair: ')
                if produto_nome.lower() == "sair":
                    break
                produto_preco = input('Digite o preço do produto: ')
                file.write(f'{produto_nome}, {produto_preco}\n')
            print('Produtos adicionados com sucesso!')
    except IOError:
        print('Erro ao acessar o arquivo de produtos.')



def main():
    store = input('É cliente ou admin:').lower()
    if store == 'cliente':
        print('Bem-vindo ao supermercado do Azinha (modo cliente)!!!')
        mostrar_prod()
    elif store == 'admin':
        if not log_admin():
            print("Aonde é que ja querias ir Bandido!!")
            return
        print('Bem-vindo ao supermercado do Azinha (modo admin)!!!')
        adicionar_produtos()
        mostrar_prod()
    else:
        print('Opção inválida. Por favor, escolha entre cliente ou admin.')


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()