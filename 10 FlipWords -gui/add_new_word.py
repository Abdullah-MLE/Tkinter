import customtkinter as ctk
from mytools import MyButton, PAD, FONT, CUTER_COLOR, word_dict
import pandas as pd

classifications = list(set(word_dict["class"].values()))


class Add:
    def __init__(self, root):
        self.root = root

        self.new_classification_b = None
        self.new_classification_l = None
        self.word_e = None
        self.ex1_e = None
        self.ex2_e = None
        self.ex3_e = None
        self.ex4_e = None
        self.ex5_e = None
        self.definition_tb = None
        self.classification_cm = None
        self.new_classification_e = None

        self.ui_initialize()

    def ui_initialize(self):
        word_l = ctk.CTkLabel(master=self.root, text="word: ", font=(f"{FONT} Regular", 25), width=350)
        word_l.grid(padx=PAD, pady=PAD, row=0, column=0)
        self.word_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the word ...", font=(f"{FONT} Regular", 25),
                                   width=350)
        self.word_e.grid(padx=PAD, pady=PAD, row=0, column=1)

        cuter = ctk.CTkLabel(master=self.root,
                             text="--------------------------------------------------------------------------------------",
                             text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter.grid(padx=PAD, pady=PAD, row=1, column=0, columnspan=3)

        ex1_l = ctk.CTkLabel(master=self.root, text="First Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex1_l.grid(padx=PAD, pady=PAD, row=2, column=0)
        self.ex1_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the first example ...",
                                  font=(f"{FONT} Regular", 25), width=350)
        self.ex1_e.grid(padx=PAD, pady=PAD, row=2, column=1)

        ex2_l = ctk.CTkLabel(master=self.root, text="Second Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex2_l.grid(padx=PAD, pady=PAD, row=3, column=0)
        self.ex2_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the second example ...",
                                  font=(f"{FONT} Regular", 25), width=350)
        self.ex2_e.grid(padx=PAD, pady=PAD, row=3, column=1)

        ex3_l = ctk.CTkLabel(master=self.root, text="Third Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex3_l.grid(padx=PAD, pady=PAD, row=4, column=0)
        self.ex3_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the third example ...",
                                  font=(f"{FONT} Regular", 25), width=350)
        self.ex3_e.grid(padx=PAD, pady=PAD, row=4, column=1)

        ex4_l = ctk.CTkLabel(master=self.root, text="Fourth Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex4_l.grid(padx=PAD, pady=PAD, row=5, column=0)
        self.ex4_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the fourth example ...",
                                  font=(f"{FONT} Regular", 25), width=350)
        self.ex4_e.grid(padx=PAD, pady=PAD, row=5, column=1)

        ex5_l = ctk.CTkLabel(master=self.root, text="Fifth Example: ", font=(f"{FONT} Regular", 25), width=350)
        ex5_l.grid(padx=PAD, pady=PAD, row=6, column=0)
        self.ex5_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the fifth example ...",
                                  font=(f"{FONT} Regular", 25), width=350)
        self.ex5_e.grid(padx=PAD, pady=PAD, row=6, column=1)

        cuter2 = ctk.CTkLabel(master=self.root,
                             text="--------------------------------------------------------------------------------------",
                             text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter2.grid(padx=PAD, pady=PAD, row=7, column=0, columnspan=3)

        definition_l = ctk.CTkLabel(master=self.root, text="Definition: ", font=(f"{FONT} Regular", 25), width=350)
        definition_l.grid(padx=PAD, pady=PAD, row=8, column=0)
        self.definition_tb = ctk.CTkTextbox(master=self.root, corner_radius=10, width=350, height=100, fg_color=CUTER_COLOR,
                                            border_color="#565b5e", border_width=2)
        self.definition_tb.grid(padx=PAD, pady=PAD, row=8, column=1)

        cuter3 = ctk.CTkLabel(master=self.root,
                             text="--------------------------------------------------------------------------------------",
                             text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter3.grid(padx=PAD, pady=PAD, row=9, column=0, columnspan=3)

        classification_l = ctk.CTkLabel(master=self.root, text="Classifications: ", font=(f"{FONT} Regular", 25), width=350)
        classification_l.grid(padx=PAD, pady=PAD, row=10, column=0)
        self.classification_cm = ctk.CTkComboBox(master=self.root, values=classifications, width=350, height=35,
                                                 font=(f"{FONT} Regular", 25))
        self.classification_cm.grid(padx=PAD, pady=PAD, row=10, column=1)
        classification_b = MyButton(master=self.root, text="Add New", width=350, command=self.new_classification)
        classification_b.grid(padx=PAD, pady=PAD, row=10, column=2)

        self.new_classification_l = ctk.CTkLabel(master=self.root, text="New Classifications: ", font=(f"{FONT} Regular", 25),
                                            width=350)
        self.new_classification_l.grid(padx=PAD, pady=PAD, row=11, column=0)
        self.new_classification_l.grid_forget()

        self.new_classification_e = ctk.CTkEntry(master=self.root, placeholder_text="Enter the new Classifications...",
                                                 font=(f"{FONT} Regular", 25), width=350)
        self.new_classification_e.grid(padx=PAD, pady=PAD, row=11, column=1)
        self.new_classification_e.grid_forget()
        self.new_classification_b = MyButton(master=self.root, text="Save Classifications", width=350, command=self.save_new_class)
        self.new_classification_b.grid(padx=PAD, pady=PAD, row=11, column=2)
        self.new_classification_b.grid_forget()
        cuter3 = ctk.CTkLabel(master=self.root,
                             text="--------------------------------------------------------------------------------------",
                             text_color=CUTER_COLOR, font=(f"{FONT} Regular", 25))
        cuter3.grid(padx=PAD, pady=PAD, row=12, column=0, columnspan=3)

        save_b = MyButton(master=self.root, text="SAVE", width=1050, command=self.save)
        save_b.grid(padx=PAD, pady=PAD, row=14, column=0, columnspan=3)

    def new_classification(self):
        self.new_classification_l.grid(padx=PAD, pady=PAD, row=11, column=0)
        self.new_classification_e.grid(padx=PAD, pady=PAD, row=11, column=1)
        self.new_classification_b.grid(padx=PAD, pady=PAD, row=11, column=2)

    def save(self):
        word = self.word_e.get()
        ex1 = self.ex1_e.get()
        ex2 = self.ex2_e.get()
        ex3 = self.ex3_e.get()
        ex4 = self.ex4_e.get()
        ex5 = self.ex5_e.get()
        definition = self.definition_tb.get("1.0","end-1c")
        word_class = self.classification_cm.get()

        length = len(word_dict["word"])

        if word and ex1 and ex2 and ex3 and ex4 and ex5 and word_class and definition:
            word_dict["word"][length] = word
            word_dict["ex1"][length] = ex1
            word_dict["ex2"][length] = ex2
            word_dict["ex3"][length] = ex3
            word_dict["ex4"][length] = ex4
            word_dict["ex5"][length] = ex5
            word_dict["def"][length] = definition
            word_dict["class"][length] = word_class
            word_dict["state"][length] = 'new'

            df = pd.DataFrame.from_dict(word_dict)
            df.to_csv(path_or_buf="Book1.csv", index=False)

            self.word_e.delete(0, 'end')
            self.ex1_e.delete(0, 'end')
            self.ex2_e.delete(0, 'end')
            self.ex3_e.delete(0, 'end')
            self.ex4_e.delete(0, 'end')
            self.ex5_e.delete(0, 'end')
            self.definition_tb.delete('1.0', "end")

    def save_new_class(self):
        new_class = self.new_classification_e.get()
        if new_class not in classifications and new_class:
            classifications.append(new_class)

        self.classification_cm.configure(values=classifications)

        self.new_classification_l.grid_forget()
        self.new_classification_e.grid_forget()
        self.new_classification_b.grid_forget()




if __name__ == "__main__":
    app = ctk.CTk()
    Add(app)
    app.mainloop()