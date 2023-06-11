import sqlite3

conexao = sqlite3.connect('cinevault.db')
cursor = conexao.cursor()

def adicionar_filme():
    nome = input("Digite o nome do filme: ")
    nota = float(input("Digite a nota do filme: "))
    cursor.execute("INSERT INTO filmes (nome, nota) VALUES (?, ?)", (nome, nota))
    conexao.commit()
    print("Filme adicionado com sucesso!")

def adicionar_serie():
    nome = input("Digite o nome da série: ")
    nota = float(input("Digite a nota da série: "))
    cursor.execute("INSERT INTO series (nome, nota) VALUES (?, ?)", (nome, nota))
    conexao.commit()
    print("Série adicionada com sucesso!")

def atualizar_dado():
    tabela = input("Digite a tabela (1 para Série ou 2 para Filme): ")
    item_id = int(input("Digite o ID do item a ser atualizado: "))

    if tabela == '1':
        nome = input("Digite o novo nome da série: ")
        nota = float(input("Digite a nova nota da série: "))
        cursor.execute("UPDATE series SET nome = ?, nota = ? WHERE id = ?", (nome, nota, item_id))
        conexao.commit()
        print("Dado da série atualizado com sucesso!")
    elif tabela == '2':
        nome = input("Digite o novo nome do filme: ")
        nota = float(input("Digite a nova nota do filme: "))
        cursor.execute("UPDATE filmes SET nome = ?, nota = ? WHERE id = ?", (nome, nota, item_id))
        conexao.commit()
        print("Dado do filme atualizado com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")


def remover_item():
    tabela = input("Digite a tabela (1 para Série ou 2 para Filme): ")
    item_id = int(input("Digite o ID do item a ser removido: "))

    if tabela == '1':
        cursor.execute("DELETE FROM series WHERE id = ?", (item_id,))
        conexao.commit()
        print("Série removida com sucesso!")
    elif tabela == '2':
        cursor.execute("DELETE FROM filmes WHERE id = ?", (item_id,))
        conexao.commit()
        print("Filme removido com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")

def exibir_dados():
    cursor.execute("SELECT * FROM series")
    series = cursor.fetchall()

    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()

    print("Séries:")
    for serie in series:
        print(f"ID: {serie[0]}, Nome: {serie[1]}, Nota: {serie[2]}")

    print("\nFilmes:")
    for filme in filmes:
        print(f"ID: {filme[0]}, Nome: {filme[1]}, Nota: {filme[2]}")

while True:
    print("Opções:")
    print("1. Adicionar série")
    print("2. Adicionar filme")
    print("3. Remover item")
    print("4. Atualizar dados")
    print("5. Exibir dados")
    print("6. Sair")

    opcao = input("Digite o número correspondente à opção desejada: ")

    if opcao == '1':
        adicionar_serie()
    elif opcao == '2':
        adicionar_filme()
    elif opcao == '3':
        remover_item()
    elif opcao == '4':
        atualizar_dado()
    elif opcao == '5':
        exibir_dados()
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")

    continuar = input("Deseja realizar outra operação? (Digite 'S' para Sim ou 'N' para Não): ")
    if continuar.upper() != 'S':
        break

conexao.close()
