from customtkinter import CTkButton
import pandas as pd

WIDTH = 1800
HEIGHT = 900
PAD = 10
FONT = "Bahnschrift"
BG_COLOR = "#242424"
FRAME_BG_COLOR = "#4C4C4C"
BUTTONS_COLOR1 = "#ff9900"
HOVER_COLOR = "#ffa52e"
CUTER_COLOR = "#343638"

df = pd.read_csv("Book1.csv")
word_dict = df.to_dict()
# print(word_dict)

words = list(word_dict["word"].values())
# print(words)

exs = [word_dict[f"ex{i}"][7] for i in range(1, 6)]
# print(exs)

# 'state': {0: 'n', 1: 'o', 2: 'o', 3: 'n', 4: 'n', 5: 'n', 6: 'n', 7: 'o', 8: 'o', 9: 'o'}
new_words_id = [i for i in word_dict["state"] if word_dict["state"][i]=="n"]
# print(new_words_id)





class MyButton(CTkButton):
    def __init__(self, text = None, command = None, master = None, width = 400):
        super().__init__(master)
        self.configure(text=text, command=command, corner_radius=32,
                       width=width, fg_color=BUTTONS_COLOR1, font=(f"{FONT} Regular", 25),
                       text_color=FRAME_BG_COLOR, hover_color=HOVER_COLOR)