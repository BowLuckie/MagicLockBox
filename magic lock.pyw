
import tkinter as tk
class GridButton(tk.Button):
    def __init__(self, master, row, col, color='white', **kwargs):
        self.row = row
        self.col = col
        self.color = color
        # Bind toggle method to button click
        tk.Button.__init__(self, master, bg=color, width=3, height=1, command=self.toggle, **kwargs)
    def toggle(self):
        self.color = 'black' if self.color == 'white' else 'white'
        self.config(bg=self.color)
class GridApp:
    def __init__(self, root):
        self.root = root
        self.create_grid()
        self.create_controls()
    def create_grid(self):
        self.grid_buttons = []
        for row in range(4):
            row_buttons = []
            for col in range(4):
                button = GridButton(self.root, row, col)
                button.grid(row=row, column=col, padx=5, pady=5)
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)
        # Add row buttons
        for row in range(4):
            shift_left_btn = tk.Button(self.root, text="Shift Left", command=lambda r=row: self.shift_row_left(r))
            shift_left_btn.grid(row=row, column=4, padx=5, pady=5)
            shift_right_btn = tk.Button(self.root, text="Shift Right", command=lambda r=row: self.shift_row_right(r))
            shift_right_btn.grid(row=row, column=5, padx=5, pady=5)
            flip_btn = tk.Button(self.root, text="Flip", command=lambda r=row: self.flip_row(r))
            flip_btn.grid(row=row, column=6, padx=5, pady=5)
        # Add column buttons
        for col in range(4):
            shift_up_btn = tk.Button(self.root, text="Shift Up", command=lambda c=col: self.shift_col_up(c))
            shift_up_btn.grid(row=4, column=col, padx=5, pady=5)
            shift_down_btn = tk.Button(self.root, text="Shift Down", command=lambda c=col: self.shift_col_down(c))
            shift_down_btn.grid(row=5, column=col, padx=5, pady=5)
            flip_btn = tk.Button(self.root, text="Flip", command=lambda c=col: self.flip_col(c))
            flip_btn.grid(row=6, column=col, padx=5, pady=5)
    def create_controls(self):
        pass  # Remove global controls
    def shift_row_left(self, row):
        # Implement shifting row left
        first_color = self.grid_buttons[row][0].color
        for col in range(3):
            self.grid_buttons[row][col].color = self.grid_buttons[row][col+1].color
            self.grid_buttons[row][col].config(bg=self.grid_buttons[row][col].color)
        self.grid_buttons[row][3].color = first_color
        self.grid_buttons[row][3].config(bg=first_color)
    def shift_row_right(self, row):
        # Implement shifting row right
        last_color = self.grid_buttons[row][3].color
        for col in range(3, 0, -1):
            self.grid_buttons[row][col].color = self.grid_buttons[row][col-1].color
            self.grid_buttons[row][col].config(bg=self.grid_buttons[row][col].color)
        self.grid_buttons[row][0].color = last_color
        self.grid_buttons[row][0].config(bg=last_color)
    def shift_col_up(self, col):
        # Implement shifting column up
        first_color = self.grid_buttons[0][col].color
        for row in range(3):
            self.grid_buttons[row][col].color = self.grid_buttons[row+1][col].color
            self.grid_buttons[row][col].config(bg=self.grid_buttons[row][col].color)
        self.grid_buttons[3][col].color = first_color
        self.grid_buttons[3][col].config(bg=first_color)
    def shift_col_down(self, col):
        # Implement shifting column down
        last_color = self.grid_buttons[3][col].color
        for row in range(3, 0, -1):
            self.grid_buttons[row][col].color = self.grid_buttons[row-1][col].color
            self.grid_buttons[row][col].config(bg=self.grid_buttons[row][col].color)
        self.grid_buttons[0][col].color = last_color
        self.grid_buttons[0][col].config(bg=last_color)
    def flip_row(self, row):
        # Implement flipping row by toggling colors
        for col in range(4):
            self.grid_buttons[row][col].toggle()
    def flip_col(self, col):
        # Implement flipping column by toggling colors
        for row in range(4):
            self.grid_buttons[row][col].toggle()
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid Operations")
    app = GridApp(root)
    root.mainloop()
