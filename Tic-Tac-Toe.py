import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root, mode):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.mode = mode
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
        
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
                
        if self.mode == 'computer' and self.current_player == 'O':
            self.computer_move()
    
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.mode == 'computer' and self.current_player == 'O':
                    self.computer_move()
    
    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)
    
    def check_win(self, player):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        ]
        
        for condition in win_conditions:
            if all(mark == player for mark in condition):
                return True
        return False
    
    def check_draw(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)
    
    def reset_board(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
                
        if self.mode == 'computer' and self.current_player == 'O':
            self.computer_move()

def start_game(mode):
    root = tk.Tk()
    game = TicTacToe(root, mode)
    root.mainloop()

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print("Choose a mode:")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice in ['1', '2']:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    mode = 'player' if choice == '1' else 'computer'
    start_game(mode)
