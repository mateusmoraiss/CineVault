import sqlite3


conexao = sqlite3.connect('cinevault.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()

cursor.execute("SELECT * FROM series")
series = cursor.fetchall()

with open("dados_cinevault.txt", "w") as arquivo:
    arquivo.write("CineVault - Dados dos Filmes e Séries\n")
    arquivo.write("-------------------------------------------------------------\n\n")

    if filmes:
        arquivo.write("Filmes:\n")
        for filme in filmes:
            arquivo.write(f"Nome: {filme[1]}\n")
            arquivo.write(f"Nota: {filme[2]}\n")
            arquivo.write("\n")
    else:
        arquivo.write("Não há filmes cadastrados.\n\n")

    if series:
        arquivo.write("Séries:\n")
        for serie in series:
            arquivo.write(f"Nome: {serie[1]}\n")
            arquivo.write(f"Nota: {serie[2]}\n")
            arquivo.write("\n")
    else:
        arquivo.write("Não há séries cadastradas.\n\n")

print("Arquivo de texto criado com sucesso!")