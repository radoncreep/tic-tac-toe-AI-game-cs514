**TIC-TAC-TOE USING MINMAX WITH ALPHA-BETA**

This project uses python programming language to build a tic tac toe game supporting 2 players, HUMAN vs AI
The graphical user interface was built with tkinter python library which enables users to play as much outside the terminal or console

The class TicTacToe is used 
It has attributes such as player1 (Human) with player mark 'X' and player2 (AI) with player mark 'O'
The board_state attribute is a list that initially consist of 9 "None" items
It is used as the structure of the board, which contains 9 buttons set on specific rows and columns on a grid, after the "create_board" and grid function have been invoked.

The class also possess certain methods such as
i. check_for_win: which takes in a player marker and checks the board state for the current player's win on every possible path
(check_for_win_in_minimax does the same but for the minimax algorithm)
ii. display_win: when invoked, it highlights the win path green, prompts a message box and disables all buttons on the board
ii. play_as_human: This is invoked when there is a click event on the board interface by a human player
iii. play_ai: Invokes right after the human's turn and places the AI's marker on the cell that has been selected by the minimax alogrithm
iv. get_empty_cell: Is a method for returning a list containing the indices of every empty or unmarked cell on the board
v. use_minimax: This method favours the AI player using the minimax algorithm with alpha-beta pruning search for the best move to make right after the human's turn.

Since, this game's main focus is on the minimax algorithm with alpha-beta pruning, following will give an overview on how this AI algorithm was used in this implementation

**STEP BY STEP OVERVIEW OF THE MINIMAX ALOGRITHM APPROACH USED HERE**
1. First of all, a list of all available cells (cells that are empty) on the current board state are obtained.
2. The conditionals check if the HUMAN OR AI player wins doing the current iteration, else if there are no available spaces it returns 0, indicating a tie
3. best_score, best_score_minimizing, best_score_cell are initialized, so as to, store the most optimal score for AI(maximizer), store the same for HUMAN(minizer) and of the cell the best moved should be made respectively
4. A for loop is used to iterate the list of available cells 
    - The first available cell is obtained and marked by the current player
    - conditionals exist to check if maximizing player(AI) or minimizing player(HUMAN)
    - in the conditionals, a recursive call is made to actualize the brute force approach of the minimax algorithm
    - a terminal state is returned down the call stack if there occurs a win for HUMAN or AI, or even a tie 
    - terminal state returned for AI win is 1, HUMAN win -1, and tie 0
    - the result from the recursive call is used to check if it is less than or greater than the current best score depending on the player
    - when the best score is obtained it means the current index in the iteration can be used to select the cell where the optimal move was made
    - after this, we revert the changes made on the board and return the best score and best score cell
    
ALPHA-BETA PRUNING
Before the code walkthrough of this concept, let us briefly discuss what alpha-beta pruning is 
Alpha-Beta Pruning itself is not an algorithm, but an augmentation of the minimax algorithm in this case. Simply, meaning that it is used to improve the performance of our algorithm, making it more optimal.
Because there are cases where we need not search or explore the branches of a node(board state), because we obtained a value which is possibly a better option than any other value 
we are going to get from the yet explored branch. We just prune that branch and carry on with the traversal.
By doing this, the minimax algorithm is able to produce a result quicker than without the alpha-beta pruning.


