from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe-CS514-AI')

clicked_on_start_game = False

class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board_state = [None] * 9

    total_moves = 0
    is_there_winner = False
    player_win = None

    # create a button and grid for every index/position of the board_state
    def create_board(self):
        global b0, b1, b2, b3, b4, b5, b6, b7, b8, b9
        b0 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b0))
        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b3))
        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b6))
        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: self.play_as_human(b8))
        self.board_state[0] = b0
        self.board_state[1] = b1
        self.board_state[2] = b2
        self.board_state[3] = b3
        self.board_state[4] = b4
        self.board_state[5] = b5
        self.board_state[6] = b6
        self.board_state[7] = b7
        self.board_state[8] = b8
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

    def check_for_win(self, player):
        board = self.board_state
        # row check
        if board[0]["text"] == player and board[1]["text"] == player and board[2]["text"] == player:
            self.display_win([0, 1, 2], player)
            return True
        elif board[3]["text"] == player and board[4]["text"] == player and board[5]["text"] == player:
            self.display_win([3, 4, 5], player)
            return True
        elif board[6]["text"] == player and board[7]["text"] == player and board[8]["text"] == player:
            self.display_win([6, 7, 8], player)
            return True

        # column check
        elif board[0]["text"] == player and board[3]["text"] == player and board[6]["text"] == player:
            self.display_win([0, 3, 6], player)
            return True
        elif board[1]["text"] == player and board[4]["text"] == player and board[7]["text"] == player:
            self.display_win([1, 4, 7], player)
            return True
        elif board[2]["text"] == player and board[5]["text"] == player and board[8]["text"] == player:
            self.display_win([2, 5, 8], player)
            return True

        # possible diagonal wins
        elif board[0]["text"] == player and board[4]["text"] == player and board[8]["text"] == player:
            self.display_win([0, 4, 8], player)
            return True

        elif board[2]["text"] == player and board[4]["text"] == player and board[6]["text"] == player:
            self.display_win([2, 4, 6], player)
            return True

        if self.total_moves == 9 and self.is_there_winner is False:
            messagebox.showinfo("TicTacToe", "This round is a tie!")
            self.player_win = None
            self.disable_buttons()
            return True
        return False

    def check_for_win_in_minimax(self, board_state, player):
        board = board_state
        # row check
        if board[0] == player and board[1] == player and board[2] == player:
            return True
        elif board[3] == player and board[4] == player and board[5] == player:
            return True
        elif board[6] == player and board[7] == player and board[8] == player:
            return True

        # column check
        elif board[0] == player and board[3] == player and board[6] == player:
            return True
        elif board[1] == player and board[4] == player and board[7] == player:
            return True
        elif board[2] == player and board[5] == player and board[8] == player:
            return True

        # possible diagonal wins
        elif board[0] == player and board[4] == player and board[8] == player:
            return True
        elif board[2] == player and board[4] == player and board[6] == player:
            return True

        return False

    def display_win(self, win_positions, player):
        self.player_win = player
        for i in range(len(win_positions)):
            self.board_state[win_positions[i]].config(bg="green")

        self.is_there_winner = True
        messagebox.showinfo("TicTacToe", "player " + player + " wins")
        self.disable_buttons()

    def disable_buttons(self):
        for i in range(len(self.board_state)):
            self.board_state[i].config(state=DISABLED)

    def play_as_human(self, btn):
        # can_make_move = lambda: selected_position == " "
        if btn["text"] == " ":
            btn["text"] = self.player1
            self.total_moves += 1
            is_game_over = self.check_for_win(self.player1)
            # if not winner after human plays then we play ai
            if not is_game_over:
                self.play_ai(self.player2)

    def play_ai(self, player_ai):
        current_board_state = list(map(lambda x: x["text"], self.board_state))

        best_score, best_score_cell = self.use_minimax(current_board_state, player_ai, True)

        btn = self.board_state[best_score_cell]

        btn["text"] = player_ai
        self.total_moves += 1
        self.check_for_win(player_ai)


    def get_empty_cells(self, current_board_state, minimax_flag):
        empty_cells_list = []

        for i in range(len(current_board_state)):
            if minimax_flag:
                if current_board_state[i] == " ":
                    empty_cells_list.append(i)
            else:
                if current_board_state[i]["text"] == " ":
                    empty_cells_list.append(i)

        return empty_cells_list


    def use_minimax(self, current_board_state, current_player_mark, maximizing_player):
        available_cells_on_board = self.get_empty_cells(current_board_state, True)

        if self.check_for_win_in_minimax(current_board_state, self.player1):
            return -1, None
        elif self.check_for_win_in_minimax(current_board_state, self.player2):
            return 1, None
        elif len(available_cells_on_board) == 0:
            return 0, None


        best_score = float("-inf")
        best_score_minimizing = float("inf")
        best_score_cell = None
        for i in range(len(available_cells_on_board)):
            current_board_state[available_cells_on_board[i]] = current_player_mark
            if maximizing_player:
                result, _ = self.use_minimax(current_board_state, self.player1, False)
                if result > best_score:
                    best_score = result
                    best_score_cell = available_cells_on_board[i]

            else:
                result, _ = self.use_minimax(current_board_state, self.player2, True)
                if result < best_score_minimizing:
                    best_score_minimizing = result
                    best_score_cell = available_cells_on_board[i]

            current_board_state[available_cells_on_board[i]] = " "

        return best_score if maximizing_player else best_score_minimizing, best_score_cell



game_init = TicTacToe("X", "O")


def start_game():
    game_init.create_board()


game_menu = Menu(root)
root.config(menu=game_menu)
menu_options = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=menu_options)
menu_options.add_command(label="Start Game", command=game_init.create_board())

start_game()
root.mainloop()
