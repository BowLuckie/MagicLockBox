import tkinter as tk
from tkinter import ttk

class MagicLockSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic Lock Simulator")

        self.grid_size = 4
        self.grid = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]  # Initialize with black squares

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        self.buttons = []
        for i in range(self.grid_size):
            row_buttons = []
            for j in range(self.grid_size):
                button = ttk.Button(self.root, width=5, command=lambda i=i, j=j: self.toggle_color(i, j))
                button.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def create_buttons(self):
        # Flip buttons for each row
        for i in range(self.grid_size):
            ttk.Button(self.root, text=f"Flip Row {i}", command=lambda i=i: self.flip_row(i)).grid(row=i, column=self.grid_size, padx=5, pady=2)

        # Flip buttons for each column
        for j in range(self.grid_size):
            ttk.Button(self.root, text=f"Flip Col {j}", command=lambda j=j: self.flip_column(j)).grid(row=self.grid_size, column=j, padx=2, pady=5)

        # Shift buttons for each row
        for i in range(self.grid_size):
            ttk.Button(self.root, text=f"Shift Left {i}", command=lambda i=i: self.shift_row_left(i)).grid(row=i, column=self.grid_size+1, padx=5, pady=2)
            ttk.Button(self.root, text=f"Shift Right {i}", command=lambda i=i: self.shift_row_right(i)).grid(row=i, column=self.grid_size+2, padx=5, pady=2)

        # Shift buttons for each column
        for j in range(self.grid_size):
            ttk.Button(self.root, text=f"Shift Up {j}", command=lambda j=j: self.shift_col_up(j)).grid(row=self.grid_size+1, column=j, padx=2, pady=5)
            ttk.Button(self.root, text=f"Shift Down {j}", command=lambda j=j: self.shift_col_down(j)).grid(row=self.grid_size+2, column=j, padx=2, pady=5)

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

    def shift_row_left(self, row):
        self.grid[row] = self.grid[row][1:] + [self.grid[row][0]]
        self.update_grid()

    def shift_row_right(self, row):
        self.grid[row] = [self.grid[row][-1]] + self.grid[row][:-1]
        self.update_grid()

    def shift_col_up(self, column):
        temp_col = [self.grid[i][column] for i in range(self.grid_size)]
        temp_col = temp_col[1:] + [temp_col[0]]
        for i in range(self.grid_size):
            self.grid[i][column] = temp_col[i]
        self.update_grid()

    def shift_col_down(self, column):
        temp_col = [self.grid[i][column] for i in range(self.grid_size)]
        temp_col = [temp_col[-1]] + temp_col[:-1]
        for i in range(self.grid_size):
            self.grid[i][column] = temp_col[i]
        self.update_grid()

    def update_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j]:
                    self.buttons[i][j].configure(style="White.TButton")
                else:
                    self.buttons[i][j].configure(style="Black.TButton")

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.configure("Black.TButton", background="black")
    style.configure("White.TButton", background="white")
    app = MagicLockSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
