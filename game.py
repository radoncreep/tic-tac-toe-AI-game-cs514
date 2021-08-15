from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Tic-Tac-Toe-CS514-AI')
clicked_on_start_game = False


class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board_state = [None] * 9

    # create a button and grid for every index/position of the board_state
    def create_board(self):
        for empty_space in range(len(self.board_state)):
            self.board_state[empty_space] = Button(root, text=" ", font=("Helvetica", 20),
                                                   height=3, width=6, bg="SystemButtonFace")
        self.create_grid()

    def create_grid(self):
        row = 0
        for pos in range(len(self.board_state)):
            # print('pos, ' + str(pos))

            if pos == 3 or pos == 6:
                row += 1
            if pos == 0 or pos == 1 or pos == 2:
                # print('pos, ' + str(pos) + ' row ' + str(row))
                self.board_state[pos].grid(row=row, column=(pos - row*3))
            elif pos == 3 or pos == 4 or pos == 5:
                self.board_state[pos].grid(row=row, column=(pos - row*3))
            elif pos == 6 or pos == 7 or pos == 8:
                self.board_state[pos].grid(row=row, column=(pos - row*3))
        root.mainloop()

    # def play_as_human(self):


gameInit = TicTacToe("X", "O")
gameInit.create_board()

game_menu = Menu(root)
root.config(menu=game_menu)

menu_options = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=menu_options)
menu_options.add_command(label="Start Game", command=gameInit.start_game(True))
