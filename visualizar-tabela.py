import sqlite3
import tkinter as tk
from tkinter import ttk

def exibir_series_e_filmes():
    conexao = sqlite3.connect('cinevault.db')
    cursor = conexao.cursor()

    # Consulta os dados da tabela 'series'
    cursor.execute("SELECT * FROM series")
    series = cursor.fetchall()

    # Consulta os dados da tabela 'filmes'
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()

    # Fecha a conexão com o banco de dados
    conexao.close()

    # Cria uma janela utilizando o Tkinter
    janela = tk.Tk()
    janela.title("CineVault - Séries e Filmes")

    # Cria um Treeview para exibir os dados de séries
    tree_series = ttk.Treeview(janela)
    tree_series["columns"] = ("nome", "nota")
    tree_series.heading("#0", text="ID")
    tree_series.heading("nome", text="Nome")
    tree_series.heading("nota", text="Nota")

    # Adiciona os dados de séries ao Treeview
    for serie in series:
        tree_series.insert("", "end", text=serie[0], values=(serie[1], serie[2]))

    # Cria um Treeview para exibir os dados de filmes
    tree_filmes = ttk.Treeview(janela)
    tree_filmes["columns"] = ("nome", "nota")
    tree_filmes.heading("#0", text="ID")
    tree_filmes.heading("nome", text="Nome")
    tree_filmes.heading("nota", text="Nota")

    # Adiciona os dados de filmes ao Treeview
    for filme in filmes:
        tree_filmes.insert("", "end", text=filme[0], values=(filme[1], filme[2]))

    # Configura a geometria da janela
    tree_series.pack(side=tk.LEFT, padx=10, pady=10)
    tree_filmes.pack(side=tk.LEFT, padx=10, pady=10)

    # Inicia o loop principal da aplicação
    janela.mainloop()

# Chama a função para exibir as séries e filmes
exibir_series_e_filmes()
