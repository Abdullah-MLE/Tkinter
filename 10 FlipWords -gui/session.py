import customtkinter as ctk
import random
import pandas as pd
from mytools import MyButton, PAD, FONT, BUTTONS_COLOR1, FRAME_BG_COLOR, word_dict


class Session:
    def __init__(self, root, state):
        self.wrong_b = None
        self.correct_b = None
        self.text2_l = None
        self.root = root
        self.state = state

        self.card_b = None
        self.spelling_e = None
        self.text1_l = None
        self.words_list_id = None
        self.counter = 0

        self.ui_initialize()
        self.set_state()
        self.start()

    def ui_initialize(self):
        self.card_b = MyButton(master=self.root, text="", width=840, command=self.pressed)
        self.card_b.configure(height=500)
        self.card_b.grid(padx=PAD, pady=PAD, row=0, column=0, columnspan=3, rowspan=2)

        self.text1_l = ctk.CTkLabel(master=self.root, text="text1", font=(f"{FONT} Regular", 50), width=700,
                               fg_color=BUTTONS_COLOR1, text_color=FRAME_BG_COLOR, bg_color=BUTTONS_COLOR1, wraplength=700)
        self.text1_l.grid(padx=PAD, pady=PAD, row=0, column=1)

        self.spelling_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the word ...", font=(f"{FONT} Regular", 50),
                                  width=700, fg_color=BUTTONS_COLOR1, text_color=FRAME_BG_COLOR, placeholder_text_color=FRAME_BG_COLOR,
                                  bg_color=BUTTONS_COLOR1, border_width=5)
        self.spelling_e.grid(padx=PAD, pady=PAD, row=0, column=1)
        self.spelling_e.grid_forget()

        self.text2_l = ctk.CTkLabel(master=self.root, text="", font=(f"{FONT} Regular", 50), width=700,
                               fg_color=BUTTONS_COLOR1, text_color=FRAME_BG_COLOR, bg_color=BUTTONS_COLOR1, wraplength=700)
        self.text2_l.grid(padx=PAD, pady=PAD, row=1, column=1)

        self.wrong_b = MyButton(master=self.root, text="✗", width=100,command=self.wrong_method)
        self.wrong_b.configure(height=100, corner_radius=50, font=(f"{FONT} Regular", 80), state="disabled")
        self.wrong_b.grid(pady=PAD, row=2, column=0)

        self.correct_b = MyButton(master=self.root, text="✔", width=100, command=self.correct_method)
        self.correct_b.configure(height=100, corner_radius=50, font=(f"{FONT} Regular", 80), state="disabled")
        self.correct_b.grid(pady=PAD, row=2, column=2)

    def set_state(self):
        if self.state == 'new':
            self.words_list_id = [i for i in word_dict["state"] if word_dict["state"][i]=="new"]
            print(self.words_list_id)
        elif self.state == 'old':
            self.words_list_id = [i for i in word_dict["state"] if word_dict["state"][i]=="old"]

    def start(self):
        examples = [word_dict[f"ex{i}"][self.words_list_id[self.counter]] for i in range(1, 6)]
        self.text1_l.configure(text=examples[random.randint(0,4)])

    def pressed(self):
        self.correct_b.configure(state="normal")
        self.wrong_b.configure(state="normal")

        if self.counter < len(self.words_list_id):
            self.card_b.configure(state="disabled")
            solution_def = word_dict["def"][self.words_list_id[self.counter]]
            solution_word = word_dict["word"][self.words_list_id[self.counter]]
            self.text1_l.configure(text=solution_word)
            self.text2_l.configure(text=solution_def)

        else:
            self.text1_l.configure(text="Session End!")
            self.card_b.configure(state="disabled")
            self.correct_b.configure(state="disabled")
            self.wrong_b.configure(state="disabled")


    def correct_method(self):
        self.correct_b.configure(state="disabled")
        self.wrong_b.configure(state="disabled")

        if word_dict["state"][self.words_list_id[self.counter]] == 'n':
            word_dict["state"][self.words_list_id[self.counter]] = 'o'
            df = pd.DataFrame.from_dict(word_dict)
            df.to_csv(path_or_buf="Book1.csv", index=False)

        if self.counter < len(self.words_list_id):
            self.counter += 1

            examples = [word_dict[f"ex{i}"][self.words_list_id[self.counter]] for i in range(1, 6)]

            self.text1_l.configure(text=examples[random.randint(0, 4)])
            self.text2_l.configure(text="")
            self.card_b.configure(state="normal")

        else:
            self.text1_l.configure(text="Session End!")
            self.card_b.configure(state="disabled")
            self.correct_b.configure(state="disabled")
            self.wrong_b.configure(state="disabled")

    def wrong_method(self):
        self.correct_b.configure(state="disabled")
        self.wrong_b.configure(state="disabled")

        if word_dict["state"][self.words_list_id[self.counter]] == 'o':
            word_dict["state"][self.words_list_id[self.counter]] = 'n'
            df = pd.DataFrame.from_dict(word_dict)
            df.to_csv(path_or_buf="Book1.csv", index=False)

        if self.counter < len(self.words_list_id):
            self.counter += 1

            examples = [word_dict[f"ex{i}"][self.words_list_id[self.counter]] for i in range(1, 6)]

            self.text1_l.configure(text=examples[random.randint(0, 4)])
            self.text2_l.configure(text="")
            self.card_b.configure(state="normal")

        else:
            self.text1_l.configure(text="Session End!")
            self.card_b.configure(state="disabled")
            self.correct_b.configure(state="disabled")
            self.wrong_b.configure(state="disabled")

if __name__ == "__main__":
    app = ctk.CTk()
    Session(app, 'n')
    app.mainloop()