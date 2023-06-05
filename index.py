import sqlite3

conexao = sqlite3.connect('cinevault.db') 
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    nota REAL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS series (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    nota REAL
                )''')

conexao.commit()
print("Olá! Bem-vindo ao CineVault - o seu app para gerenciar séries e filmes e visualizá-los em um gráfico.")
print("Copyright - Mateus Morais 2023")
print("GitHub: https://github.com/mateusmoraiss")
input("\nPressione Enter para fechar...")




# Fechando a conexão 
conexao.close()
