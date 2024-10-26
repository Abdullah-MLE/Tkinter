import csv

import customtkinter as ctk
from CTkXYFrame import *

from mytools import PAD, FONT

class ShowAllWords:
    def __init__(self, root):
        self.root = root
        self.csv_file = "Book1.csv"

        self.ui_initialize()

    def ui_initialize(self):
        # Create a scrollable frame
        scrollable_frame = CTkXYFrame(master=self.root, width=1330, height=900)
        scrollable_frame.grid(padx=PAD, pady=PAD, row=0, column=0)

        # Open the CSV file and display the data
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            for row_idx, row in enumerate(reader):
                for col_idx, value in enumerate(row):
                    # Create labels for each cell
                    cell_label = ctk.CTkLabel(master=scrollable_frame, text=value, font=(f"{FONT} Regular", 18), width=150)
                    cell_label.grid(row=row_idx, column=col_idx, padx=5, pady=5)

if __name__ == "__main__":
    app = ctk.CTk()
    csv_file_path = 'words.csv'  # Replace with your CSV file path
    ShowAllWords(app)
    app.mainloop()
