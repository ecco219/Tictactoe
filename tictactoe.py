import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # Player 1 starts (X)
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == 0 and not self.game_over:
            self.board[row][col] = self.current_player
            self.check_winner()
            self.current_player = 3 - self.current_player  # Switch players (1 -> 2, 2 -> 1)
        else:
            print("Invalid move!")

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or \
               np.all(self.board[:, i] == self.current_player):
                self.game_over = True
                self.winner = self.current_player
                return

        # Check diagonals
        if np.all(np.diag(self.board) == self.current_player) or \
           np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            self.game_over = True
            self.winner = self.current_player
            return

        # Check for draw
        if np.all(self.board != 0):
            self.game_over = True

    def print_board(self):
        symbols = {0: ' ', 1: 'X', 2: 'O'}
        for row in self.board:
            print('|'.join(symbols[cell] for cell in row))
            print('-' * 5)

def main():
    game = TicTacToe()
    
    while not game.game_over:
        game.print_board()
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            game.make_move(row, col)
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    game.print_board()
    if game.winner:
        print(f"Player {game.winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
