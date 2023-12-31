import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(root, text="", font=("Helvetica", 24),
                                                  height=2, width=5, command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if all(cell == "X" for cell in row) or all(cell == "O" for cell in row):
                return True
        
        for col in range(3):
            if all(self.board[row][col] == "X" for row in range(3)) or all(self.board[row][col] == "O" for row in range(3)):
                return True

        if all(self.board[i][i] == "X" for i in range(3)) or all(self.board[i][i] == "O" for i in range(3)):
            return True

        if all(self.board[i][2 - i] == "X" for i in range(3)) or all(self.board[i][2 - i] == "O" for i in range(3)):
            return True

        return False
    
    def check_draw(self):
        return all(cell != "" for row in self.board for cell in row)
    
    def show_winner(self):
        winner = "Player o" if self.current_player == "x" else "Player O"
        messagebox.showinfo("Winner!", f"{winner} wins!")
        self.reset_board()
    
    def show_draw(self):
        messagebox.showinfo("Draw!", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.buttons[row][col].config(text="")
        
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

