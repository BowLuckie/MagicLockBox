import tkinter as tk
from tkinter import ttk

class MagicLockSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic Lock Simulator")

        self.grid_size = 4
        self.grid = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]  # False represents black, True represents white

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        self.buttons = []
        for i in range(self.grid_size):
            row_buttons = []
            for j in range(self.grid_size):
                button = ttk.Button(self.root, width=5, command=lambda i=i, j=j: self.toggle_color(i, j), style="Cell.TButton")
                button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        for i in range(self.grid_size):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        self.update_grid()

    def create_buttons(self):
        flip_frame = ttk.Frame(self.root)
        flip_frame.grid(row=self.grid_size, column=0, columnspan=4, pady=5, sticky="ew")
        for i in range(self.grid_size):
            ttk.Button(flip_frame, text=f"Flip Row {i}", command=lambda i=i: self.flip_row(i)).grid(row=0, column=i, padx=5)
            ttk.Button(flip_frame, text=f"Flip Col {i}", command=lambda i=i: self.flip_column(i)).grid(row=1, column=i, padx=5)

        shift_frame = ttk.Frame(self.root)
        shift_frame.grid(row=self.grid_size + 1, column=0, columnspan=4, pady=5, sticky="ew")
        for i in range(self.grid_size):
            ttk.Button(shift_frame, text=f"Shift Row {i} Left", command=lambda i=i: self.shift_left(i)).grid(row=0, column=i, padx=5)
            ttk.Button(shift_frame, text=f"Shift Row {i} Right", command=lambda i=i: self.shift_right(i)).grid(row=1, column=i, padx=5)
            ttk.Button(shift_frame, text=f"Shift Col {i} Up", command=lambda i=i: self.shift_up(i)).grid(row=2, column=i, padx=5)
            ttk.Button(shift_frame, text=f"Shift Col {i} Down", command=lambda i=i: self.shift_down(i)).grid(row=3, column=i, padx=5)

    def toggle_color(self, i, j):
        self.grid[i][j] = not self.grid[i][j]
        self.update_grid()

    def flip_row(self, row):
        for j in range(self.grid_size):
            self.grid[row][j] = not self.grid[row][j]
        self.update_grid()

    def flip_column(self, column):
        for i in range(self.grid_size):
            self.grid[i][column] = not self.grid[i][column]
        self.update_grid()

    def shift_left(self, row):
        self.grid[row] = self.grid[row][1:] + [self.grid[row][0]]
        self.update_grid()

    def shift_right(self, row):
        self.grid[row] = [self.grid[row][-1]] + self.grid[row][:-1]
        self.update_grid()

    def shift_up(self, column):
        temp_col = [self.grid[i][column] for i in range(self.grid_size)]
        temp_col = temp_col[1:] + [temp_col[0]]
        for i in range(self.grid_size):
            self.grid[i][column] = temp_col[i]
        self.update_grid()

    def shift_down(self, column):
        temp_col = [self.grid[i][column] for i in range(self.grid_size)]
        temp_col = [temp_col[-1]] + temp_col[:-1]
        for i in range(self.grid_size):
            self.grid[i][column] = temp_col[i]
        self.update_grid()

    def update_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j]:
                    self.buttons[i][j].configure(style="WhiteCell.TButton")
                else:
                    self.buttons[i][j].configure(style="BlackCell.TButton")

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.configure("BlackCell.TButton", background="#333333")
    style.configure("WhiteCell.TButton", background="#DDDDDD")
    app = MagicLockSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
