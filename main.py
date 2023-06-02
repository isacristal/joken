import random
import time
import tkinter as tk

def play_game():
    global pontuacao
    jogador = player_entry.get()

    if jogador.lower() == "sair":
        window.destroy()
        return

    lista = ("pedra", "papel", "tesoura")
    computador = random.choice(lista)

    escolha = escolha_var.get()

    if (escolha < 0 or escolha > 2):
        result_label.config(text="Essa opção não existe")
        return

    result_label.config(text="")

    for i in range(3, 0, -1):
        countdown_label.config(text=i)
        window.update()
        time.sleep(1)

    computador_label.config(text="Computador jogou: " + computador)
    jogador_label.config(text=jogador + " jogou: " + lista[escolha])

    if (computador == "pedra" and escolha == 0) or (computador == "papel" and escolha == 1) or (
            computador == "tesoura" and escolha == 2):
        result_label.config(text="Empate", fg="#005C8A", font=("Arial", 12, "bold"))
    elif (computador == "pedra" and escolha == 1) or (computador == "papel" and escolha == 2) or (
            computador == "tesoura" and escolha == 0):
        result_label.config(text=jogador + " venceu! " + lista[escolha].capitalize() + " ganha de " + computador,
                            fg="#005C8A", font=("Arial", 12, "bold"))
        pontuacao += 1
    else:
        result_label.config(text=jogador + " perdeu! " + computador.capitalize() + " ganha de " + lista[escolha],
                            fg="#005C8A", font=("Arial", 12, "bold"))
        pontuacao -= 1

    pontuacao_label.config(text="Pontuação atual: " + str(pontuacao))

    # Resetar cor de fundo de todos os botões
    for button in option_buttons:
        button.config(bg="#0087C9")

    # Destacar a opção selecionada
    option_buttons[escolha].config(bg="#005C8A")

def restart_game():
    global pontuacao
    pontuacao = 0
    pontuacao_label.config(text="Pontuação atual: " + str(pontuacao))
    player_entry.delete(0, tk.END)
    escolha_var.set(0)
    countdown_label.config(text="")
    computador_label.config(text="")
    jogador_label.config(text="")
    result_label.config(text="", fg="#005C8A", font=("Arial", 12, "normal"))

window = tk.Tk()
window.title("Jokempoooo")
window.configure(bg="#005C8A")

# Centralizar o quadro na janela
window_width = 400
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

frame = tk.Frame(window, bg="#FFFFFF", padx=20, pady=20)
frame.pack(expand=True)

# Título
fonte_titulo = ("Arial", 16, "italic")  # Fonte "Arial" com tamanho 16 e estilo "italic"
title_label = tk.Label(frame, text="Bem-vindos ao jogo Jokempoooo", font=fonte_titulo, bg="#FFFFFF", fg="#005C8A")
title_label.pack(pady=10)

# Campo de entrada para o nome do jogador
fonte = ("Arial", 12, "italic")  # Fonte "Arial" com tamanho 12 e estilo "italic"
player_label = tk.Label(frame, text="Nome do jogador:", font=fonte, bg="#FFFFFF", fg="#005C8A")
player_label.pack(pady=10)
player_entry = tk.Entry(frame, font=fonte, bg="#AFAFAF")
player_entry.pack()

# Opções de escolha
escolha_var = tk.IntVar()

options_frame = tk.Frame(frame, bg="#FFFFFF")
options_frame.pack(pady=10)

opcoes_label = tk.Label(options_frame, text="Escolha uma opção:", font=fonte, bg="#FFFFFF", fg="#005C8A")
opcoes_label.pack()

option_buttons = []

def select_option(index):
    escolha_var.set(index)
    # Resetar cor de fundo de todos os botões
    for button in option_buttons:
        button.config(bg="#0087C9")
    # Destacar a opção selecionada
    option_buttons[index].config(bg="#005C8A")

for i, opcao in enumerate(["Pedra", "Papel", "Tesoura"]):
    option_button = tk.Button(options_frame, text=opcao, font=fonte, bg="#0087C9", fg="white",
                              activebackground="#005C8A", activeforeground="white",
                              width=10, height=1, relief=tk.SOLID, bd=2, command=lambda index=i: select_option(index))

    option_button.pack(pady=5)
    option_buttons.append(option_button)

    # Destacar a opção selecionada
    if i == 0:
        option_button.config(bg="#005C8A")

# Botão de jogar
play_button = tk.Button(frame, text="Jogar", command=play_game, font=fonte, bg="#0087C9", fg="white")
play_button.pack(pady=10)

# Resultado
countdown_label = tk.Label(frame, text="", font=fonte, bg="#FFFFFF", fg="#005C8A")
countdown_label.pack()

computador_label = tk.Label(frame, text="", font=fonte, bg="#FFFFFF", fg="#005C8A")
computador_label.pack()

jogador_label = tk.Label(frame, text="", font=fonte, bg="#FFFFFF", fg="#005C8A")
jogador_label.pack()

result_label = tk.Label(frame, text="", font=fonte, bg="#FFFFFF", fg="#005C8A")
result_label.pack()

# Pontuação
pontuacao = 0
pontuacao_label = tk.Label(frame, text="Pontuação atual: " + str(pontuacao), font=fonte, bg="#FFFFFF",
                           fg="#005C8A")
pontuacao_label.pack(pady=10)

# Botão de reiniciar
restart_button = tk.Button(frame, text="Reiniciar Jogo", command=restart_game, font=fonte, bg="#0087C9",
                           fg="white", relief=tk.RAISED)
restart_button.pack(pady=10)

window.mainloop()
