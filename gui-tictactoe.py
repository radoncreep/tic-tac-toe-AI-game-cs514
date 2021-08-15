from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Tic-Tac-Toe-CS514-AI')
# root.geometry("480x480")

clicked = True
count = 0
board_positions = []


def start():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    # we need 9 buttons for the tictactoe grid
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b9))

    # Grid buttons to screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def restart():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    global clicked, count
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: btn_click(b9))

    # Grid buttons to screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def check_for_win():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player X wins")
        disable_all_buttons()

    #   for Player O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', "Player O wins")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("TicTacToe", "This round is a tie!")
        disable_all_buttons()


# btn is a widget
def btn_click(btn):
    global clicked, count

    # btn.config(text="abc")
    if btn["text"] == " " and clicked is True:
        btn["text"] = "X"
        count += 1  # keeps track of moves must not be greater than 9
        check_for_win()
        if not winner:
            clicked = False
            play_ai(btn)
    else:
        messagebox.showerror("Tic-Tac-Toe", "Move made on this box already")


def play_ai(btn):
    global clicked, count
    board_positions = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    while clicked is False and count != 9:
        random_position = random.randint(1, 9)
        print(random_position)
        if board_positions[random_position - 1]["text"] == " ":
            board_positions[random_position - 1]["text"] = "O"
            clicked = True
            count += 1
            check_for_win()


game_menu = Menu(root)
root.config(menu=game_menu)

menu_options = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=menu_options)
menu_options.add_command(label="Restart Game", command=restart)

start()
root.mainloop()

# if empty_space == 0:
#     self.board_state[empty_space].grid(row=0, column=0)
# elif empty_space == 1:
#     self.board_state[empty_space].grid(row=0, column=1)
# elif empty_space == 2:
#     self.board_state[empty_space].grid(row=0, column=2)
# elif empty_space == 3:
#     self.board_state[empty_space].grid(row=0, column=3)
# elif empty_space == 4:
#     self.board_state[empty_space].grid(row=0, column=4)
# elif empty_space == 5:
#     self.board_state[empty_space].grid(row=0, column=5)
# elif empty_space == 1:
#     self.board_state[empty_space].grid(row=0, column=0)
# elif empty_space == 1:
#     self.board_state[empty_space].grid(row=0, column=0)
# elif empty_space == 1:
#     self.board_state[empty_space].grid(row=0, column=0)
