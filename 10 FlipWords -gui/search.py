import customtkinter as ctk
from mytools import MyButton, PAD, FONT, CUTER_COLOR, word_dict

classifications = list(set(word_dict["class"].values()))
word_id = "--"


class Search:
    def __init__(self, root):
        self.word_id_l = None
        self.root = root

        self.word_e = None
        self.ex1_e = None
        self.ex2_e = None
        self.ex3_e = None
        self.ex4_e = None
        self.ex5_e = None
        self.definition_tb = None
        self.classification_cm = None

        self.ui_initialize()

    def ui_initialize(self):
        word_l = ctk.CTkLabel(master=self.root, text="word: ", font=(f"{FONT} Regular", 25), width=350)
        word_l.grid(padx=PAD, pady=PAD, row=0, column=0)
        self.word_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter a word to search for",
                                   font=(f"{FONT} Regular", 25),
                                   width=350)
        self.word_e.grid(padx=PAD, pady=PAD, row=0, column=1)
        self.word_id_l = ctk.CTkLabel(master=self.root, text=f"id:{word_id}", font=(f"{FONT} Regular", 25), width=350)
        self.word_id_l.grid(padx=PAD, pady=PAD, row=0, column=2)

        cuter = ctk.CTkLabel(master=self.root,
                             text="--------------------------------------------------------------------------------------",
                             text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter.grid(padx=PAD, pady=PAD, row=1, column=0, columnspan=3)

        ex1_l = ctk.CTkLabel(master=self.root, text="First Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex1_l.grid(padx=PAD, pady=PAD, row=2, column=0)
        self.ex1_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the first example ...",
                                  font=(f"{FONT} Regular", 25), width=350, state="disabled")
        self.ex1_e.grid(padx=PAD, pady=PAD, row=2, column=1)

        ex2_l = ctk.CTkLabel(master=self.root, text="Second Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex2_l.grid(padx=PAD, pady=PAD, row=3, column=0)
        self.ex2_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the second example ...",
                                  font=(f"{FONT} Regular", 25), width=350, state="disabled")
        self.ex2_e.grid(padx=PAD, pady=PAD, row=3, column=1)

        ex3_l = ctk.CTkLabel(master=self.root, text="Third Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex3_l.grid(padx=PAD, pady=PAD, row=4, column=0)
        self.ex3_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the third example ...",
                                  font=(f"{FONT} Regular", 25), width=350, state="disabled")
        self.ex3_e.grid(padx=PAD, pady=PAD, row=4, column=1)

        ex4_l = ctk.CTkLabel(master=self.root, text="Fourth Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex4_l.grid(padx=PAD, pady=PAD, row=5, column=0)
        self.ex4_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the fourth example ...",
                                  font=(f"{FONT} Regular", 25), width=350, state="disabled")
        self.ex4_e.grid(padx=PAD, pady=PAD, row=5, column=1)

        ex5_l = ctk.CTkLabel(master=self.root, text="Fifth Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex5_l.grid(padx=PAD, pady=PAD, row=6, column=0)
        self.ex5_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the fifth example ...",
                                  font=(f"{FONT} Regular", 25), width=350, state="disabled")
        self.ex5_e.grid(padx=PAD, pady=PAD, row=6, column=1)

        cuter2 = ctk.CTkLabel(master=self.root,
                              text="--------------------------------------------------------------------------------------",
                              text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter2.grid(padx=PAD, pady=PAD, row=7, column=0, columnspan=3)

        definition_l = ctk.CTkLabel(master=self.root, text="Definition: ", font=(f"{FONT} Regular", 25), width=350)
        definition_l.grid(padx=PAD, pady=PAD, row=8, column=0)
        self.definition_tb = ctk.CTkTextbox(master=self.root, corner_radius=10, width=350, height=100,
                                            fg_color=CUTER_COLOR,
                                            border_color="#565b5e", border_width=2, state="disabled")
        self.definition_tb.grid(padx=PAD, pady=PAD, row=8, column=1)

        cuter3 = ctk.CTkLabel(master=self.root,
                              text="--------------------------------------------------------------------------------------",
                              text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter3.grid(padx=PAD, pady=PAD, row=9, column=0, columnspan=3)

        classification_l = ctk.CTkLabel(master=self.root, text="Classifications: ", font=(f"{FONT} Regular", 25),
                                        width=350)
        classification_l.grid(padx=PAD, pady=PAD, row=10, column=0)
        self.classification_cm = ctk.CTkComboBox(master=self.root, values=classifications, width=350, height=35,
                                                 font=(f"{FONT} Regular", 25), state="disabled")
        self.classification_cm.grid(padx=PAD, pady=PAD, row=10, column=1)

        cuter3 = ctk.CTkLabel(master=self.root,
                              text="--------------------------------------------------------------------------------------",
                              text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter3.grid(padx=PAD, pady=PAD, row=12, column=0, columnspan=3)

        search_b = MyButton(master=self.root, text="Search", width=1050, command=self.search)
        search_b.grid(padx=PAD, pady=PAD, row=14, column=0, columnspan=3)

    def search(self):
        global word_id
        word = self.word_e.get()
        if word in list(word_dict["word"].values()):
            word_id = list(word_dict["word"].keys())[list(word_dict["word"].values()).index(word)]
            ex1 = word_dict["ex1"][word_id]
            ex2 = word_dict["ex2"][word_id]
            ex3 = word_dict["ex3"][word_id]
            ex4 = word_dict["ex4"][word_id]
            ex5 = word_dict["ex5"][word_id]
            defi = word_dict["def"][word_id]
            cla = word_dict["class"][word_id]

            self.word_id_l.configure(text=f"id: {word_id}")

            self.ex1_e.configure(state="normal")
            self.ex1_e.delete(0, ctk.END)
            self.ex1_e.insert(0, ex1)
            self.ex1_e.configure(state="disabled")

            self.ex2_e.configure(state="normal")
            self.ex2_e.delete(0, ctk.END)
            self.ex2_e.insert(0, ex2)
            self.ex2_e.configure(state="disabled")

            self.ex3_e.configure(state="normal")
            self.ex3_e.delete(0, ctk.END)
            self.ex3_e.insert(0, ex3)
            self.ex3_e.configure(state="disabled")

            self.ex4_e.configure(state="normal")
            self.ex4_e.delete(0, ctk.END)
            self.ex4_e.insert(0, ex4)
            self.ex4_e.configure(state="disabled")

            self.ex5_e.configure(state="normal")
            self.ex5_e.delete(0, ctk.END)
            self.ex5_e.insert(0, ex5)
            self.ex5_e.configure(state="disabled")

            self.definition_tb.configure(state="normal")
            self.definition_tb.delete("1.0","end")
            self.definition_tb.insert(ctk.INSERT, defi)
            self.definition_tb.configure(state="disabled")

            self.classification_cm.configure(state="normal")
            self.classification_cm.set(cla)
            self.classification_cm.configure(state="disabled")
        else:
            self.word_id_l.configure(text="no such word")



if __name__ == "__main__":
    app = ctk.CTk()
    Search(app)
    app.mainloop()
