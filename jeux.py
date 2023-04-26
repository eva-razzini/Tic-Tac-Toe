from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import ia
import random

root = Tk()
root.title("Tic Tac Toe")

# Frame pour le menu principal
frm_menu = ttk.Frame(root, padding=100)
frm_menu.grid()

ttk.Label(frm_menu, text="Tic Tac Toe", font=("Times New Roman", 50, "italic"), padding=20).grid(column=1, row=0)
ttk.Button(frm_menu, text="Joueur contre Joueur", command=lambda: switch_frame(frm_joueur_joueur)).grid(column=1, row=2)
ttk.Button(frm_menu, text="Joueur contre IA", command=lambda: switch_frame(frm_joueur_ia)).grid(column=1, row=3)
ttk.Button(frm_menu, text="Quit", command=root.destroy).grid(column=1, row=4)

# Frame pour le bloc "Joueur contre joueur"
frm_joueur_joueur = ttk.Frame(root, padding=100)

joueur1 = StringVar(value="")
joueur2 = StringVar(value="")

ttk.Label(frm_joueur_joueur, text="Saisir les surnoms", font=("Times New Roman", 20), padding=20).grid(column=1, row=1)
ttk.Entry(frm_joueur_joueur, textvariable=joueur1).grid(column=1, row=3)
ttk.Entry(frm_joueur_joueur, textvariable=joueur2).grid(column=1, row=4)
ttk.Label(frm_joueur_joueur, text="Joueur 1").grid(column=0, row=3)
ttk.Label(frm_joueur_joueur, text="Joueur 2").grid(column=0, row=4)
ttk.Button(frm_joueur_joueur, text="Jouer", command=lambda: switch_frame(frm_jeu)).grid(column=1, row=5)

# Frame pour le bloc "Joueur contre IA"
frm_joueur_ia = ttk.Frame(root, padding=100)

level1 = 0  # Initialisation de la variable level

joueur1ia = StringVar(value="")

ttk.Label(frm_joueur_ia, text="Saisir le surnom", font=("Times New Roman", 20), padding=20).grid(column=1, row=1)
ttk.Entry(frm_joueur_ia, textvariable=joueur1ia).grid(column=1, row=2)
ttk.Entry(frm_joueur_ia).grid(column=1, row=2)
ttk.Label(frm_joueur_ia, text="Joueur 1").grid(column=0, row=2)

ttk.Button(frm_joueur_ia, text="Niveau1", command=lambda: set_level(1)).grid(column=1, row=4)
ttk.Button(frm_joueur_ia, text="Niveau2", command=lambda: set_level(2)).grid(column=1, row=5)
ttk.Button(frm_joueur_ia, text="Niveau3", command=lambda: set_level(3)).grid(column=1, row=6)

def set_level(level1):
    global selected_level
    selected_level = level1
    switch_frame(frm_jeu_ia)

def get_level():
    return level1
# Frame pour le bloc "Jeu"
frm_jeu = ttk.Frame(root, padding=100)

joueur1_name = joueur1
joueur2_name = joueur2

ttk.Label(frm_jeu, text="Tic-tac-toe Game", font=("Times New Roman", 20)).grid(row=0, column=0)
ttk.Label(frm_jeu, textvariable=joueur1_name, font=("Times New Roman", 20)).grid(row=2, column=0)
ttk.Label(frm_jeu, textvariable=joueur2_name, font=("Times New Roman", 20)).grid(row=3, column=0)

btn1 = ttk.Button(frm_jeu, text="", command=lambda: clicked1(btn1))


turn = 1  # For first person turn.

def clickedproccessing():
    global turn
    if turn == 1:
        turn = 2
        return "X"
    elif turn == 2:
        turn = 1
        return "O"


def clicked1():
    global turn
    if btn1["text"] == " ":  # For getting the text of a button
        btn1["text"] = clickedproccessing()
        check()


def clicked2():
    global turn
    if btn2["text"] == " ":
        btn2["text"] = clickedproccessing()
        check()


def clicked3():
    global turn
    if btn3["text"] == " ":
        btn3["text"] = clickedproccessing()
        check()


def clicked4():
    global turn
    if btn4["text"] == " ":
        btn4["text"] = clickedproccessing()
        check()


def clicked5():
    global turn
    if btn5["text"] == " ":
        btn5["text"] = clickedproccessing()
        check()


def clicked6():
    global turn
    if btn6["text"] == " ":
        btn6["text"] = clickedproccessing()
        check()


def clicked7():
    global turn
    if btn7["text"] == " ":
        btn7["text"] = clickedproccessing()
        check()


def clicked8():
    global turn
    if btn8["text"] == " ":
        btn8["text"] = clickedproccessing()
        check()


def clicked9():
    global turn
    if btn9["text"] == " ":
        btn9["text"] = clickedproccessing()
        check()


def check():
    global flag
    b1 = btn1["text"] # Getting value from each button,
    b2 = btn2["text"] # to check for any possible win event
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag += 1
    # Check every possible win on map
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(b1)
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(b4)
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(b7)
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(b1)
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(b2)
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(b3)
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(b1)
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(b7)
    elif flag == 9:
        messagebox.showinfo("Match Nul")
        effacer_donnees()
        switch_frame(frm_menu)


def win(player):
    ans = "Partie Gagner, Joueur " + player + " à Gagner !!!"
    messagebox.showinfo("Gagner !! ", ans,)
    effacer_donnees()
    switch_frame(frm_menu)  # is used to close the program


btn1 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(frm_jeu, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked9)
btn9.grid(column=3, row=3)

def effacer_donnees():
    global turn, flag
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    turn = 1
    flag = 0

flag = 0  # Flag used to apeend (1) in every turn is occurred

# Frame pour le bloc "Jeu"
frm_jeu_ia = ttk.Frame(root, padding=100)
frm_jeu_ia.grid()

joueur1_name_ia = joueur1ia
joueur2_name_ia = "Ordinateur"

ttk.Label(frm_jeu_ia, text="Tic-tac-toe Game", font=("Times New Roman", 20)).grid(row=0, column=0)
ttk.Label(frm_jeu_ia, textvariable=joueur1_name_ia, font=("Times New Roman", 20)).grid(row=2, column=0)
ttk.Label(frm_jeu_ia, textvariable=joueur2_name_ia, font=("Times New Roman", 20)).grid(row=3, column=0)

btn1 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn1, 0, 0))
btn1.grid(column=1, row=1)
btn2 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn2, 0, 1))
btn2.grid(column=2, row=1)
btn3 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn3, 0, 2))
btn3.grid(column=3, row=1)
btn4 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn4, 1, 0))
btn4.grid(column=1, row=2)
btn5 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn5, 1, 1))
btn5.grid(column=2, row=2)
btn6 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn6, 1, 2))
btn6.grid(column=3, row=2)
btn7 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn7, 2, 0))
btn7.grid(column=1, row=3)
btn8 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn8, 2, 1))
btn8.grid(column=2, row=3)
btn9 = ttk.Button(frm_jeu_ia, text="", command=lambda: clicked(btn9, 2, 2))
btn9.grid(column=3, row=3)

btn_list = [[btn1, btn2, btn3], [btn4, btn5, btn6], [btn7, btn8, btn9]]

turn = 1  # For first person turn.
player_mark = "X"
ai_mark = "O"

def clicked(btn, row, column):
    global player_turn
    global board

    if btn["text"] == "" and player_turn == "X":
        btn["text"] = "X"
        board[row][column] = "X"
        player_turn = "O"
    elif btn["text"] == "" and player_turn == "O":
        btn["text"] = "O"
        board[row][column] = "O"
        player_turn = "X"
    
    if check_win():
        messagebox.showinfo("Winner!", f"{player_turn} wins!")
        reset_board()
    elif check_tie(board):
        messagebox.showinfo("Tie game!", "It's a tie!")
        reset_board()

def ai_turn():
    global turn
    global player_mark
    global btn_list
    global selected_level

    if selected_level == 1:
        # Level 1 : Random move by AI
        row, column = get_random_move()
    elif selected_level == 2:
        # Level 2 : Defensive play by AI
        row, column = get_defensive_move()
    elif selected_level == 3:
        # Level 3 : Offensive play by AI
        row, column = get_offensive_move()

    button = btn_list[row][column]

    if button["text"] == "":
        button["text"] = "O"
        btn_list[row][column] = "O"

        if check_win("O"):
            messagebox.showinfo("Winner", "L'ordinateur gagne la partie!")
            reset_board()
        elif check_tie():
            messagebox.showinfo("Tie", "Match nul!")
            reset_board()
        else:
            turn = 1

def get_random_move():
    """
    Returns a random empty cell as (row, column).
    """
    global btn_list
    empty_cells = []
    for row in range(3):
        for column in range(3):
            if btn_list[row][column] == "":
                empty_cells.append((row, column))

    return random.choice(empty_cells)

def get_defensive_move():
    """
    Returns the move to block player's win.
    If no such move exists, returns a random move.
    """
    global btn_list

    # Check rows
    for row in range(3):
        if btn_list[row].count(player_mark) == 2 and btn_list[row].count(ai_mark) == 0:
            return (row, btn_list[row].index(""))

    # Check columns
    for column in range(3):
        column_list = [btn_list[row][column] for row in range(3)]
        if column_list.count(player_mark) == 2 and column_list.count(ai_mark) == 0:
            return (column_list.index(""), column)

    # Check diagonals
    diagonal1 = [btn_list[i][i] for i in range(3)]
    diagonal2 = [btn_list[i][2-i] for i in range(3)]
    if diagonal1.count(player_mark) == 2 and diagonal1.count(ai_mark) == 0:
        return (diagonal1.index(""), diagonal1.index(""))
    if diagonal2.count(player_mark) == 2 and diagonal2.count(ai_mark) == 0:
        return (diagonal2.index(""), 2 - diagonal2.index(""))

    # If player cannot win in the next move, make a random move
    return get_random_move()

def get_offensive_move():
    """
    Returns the move to win the game.
    If no such move exists, returns a random move.
    """
    global btn_list

    # Check rows
    for row in range(3):
        if btn_list[row].count(ai_mark) == 2 and btn_list[row].count(player_mark) == 0:
            return (row, btn_list[row].index(""))

    # Check columns
    for column in range(3):
        column_list = [btn_list[row][column] for row in range(3)]
        if column_list.count(ai_mark) == 2 and column_list.count(player_mark) == 0:
            return (column_list.index(""), column)

    # Check diagonals
    diagonal1 = [btn_list[i][i] for i in range(3)]
    diagonal2 = [btn_list[i][2-i] for i in range(3)]
    if diagonal1.count(ai_mark) == 2 and diagonal1.count(player_mark) == 0:
        return (diagonal1.index(""), diagonal1.index(""))
    if diagonal2.count(ai_mark) == 2 and diagonal2.count(player_mark) == 0:
        return (diagonal2.index(""), 2 - diagonal2.index(""))

    # If AI cannot win in the next move, make a random move
    return get_random_move()

def check_win(mark):
    global btn_list

    # Check rows
    for row in range(3):
        if btn_list[row].count(mark) == 3:
            return True

    # Check columns
    for column in range(3):
        column_list = [btn_list[row][column] for row in range(3)]
        if column_list.count(mark) == 3:
            return True

    # Check diagonals
    diagonal1 = [btn_list[i][i] for i in range(3)]
    diagonal2 = [btn_list[i][2-i] for i in range(3)]
    if diagonal1.count(mark) == 3 or diagonal2.count(mark) == 3:
        return True

    return False

def check_tie(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

def reset_board():
    global turn
    global player_mark
    global btn_list
    turn = 1
    player_mark = "X"
    for row in btn_list:
        for button in row:
            button.config(text="")
            button.config(state="enabled")
        # Reactiver tous les boutons


# Fonction pour changer de frame
def switch_frame(frame):
    # Cache toutes les frames
    for child in root.winfo_children():
        child.grid_remove()

    # Affiche la frame sélectionnée
    frame.grid()

# Affiche la frame du menu principal au lancement
switch_frame(frm_menu)

root.mainloop()