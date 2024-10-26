import customtkinter as ctk
from mytools import PAD, FONT


class About:
    def __init__(self, root):
        self.root = root
        self.ui_initialize()

    def ui_initialize(self):
        # Title Label
        title_label = ctk.CTkLabel(
            master=self.root,
            text="About This App",
            font=(f"{FONT} Bold", 30),
            width=350
        )
        title_label.grid(padx=PAD, pady=(PAD, 0), row=0, column=0)

        # Description Text
        description_text = (
            "Welcome to FlipWords – your personalized vocabulary builder! "
            "This app is designed to make learning new words simple, structured, and effective.\n\n\n"
            "How to Use This App:\n\n"
            "1. Add New Words: Start by entering words you want to learn, with definitions or translations and 5 examples to practise your word thorough.\n\n"
            "2. Study and Review: Practice each word individually and test yourself to reinforce knowledge.\n\n"
            "3. Search, Update and Delete: Look up or edit or delete words you've saved.\n\n"
            "4. Show all words: show all words that you have in your database.\n\n\n"
            "it's open source app you can edit and run it in your local machine in the repo\n\n"
            "Happy Learning!"
        )

        description_label = ctk.CTkLabel(
            master=self.root,
            text=description_text,
            font=(f"{FONT} Regular", 18),
            justify="left",
            width=600,
            wraplength=600
        )
        description_label.grid(padx=PAD, pady=PAD, row=1, column=0)

        creator_label = ctk.CTkLabel(
            master=self.root,
            text="Created by @abdullah_Said",
            font=(f"{FONT} Italic", 20),
            width=350
        )
        creator_label.grid(padx=PAD, pady=PAD, row=2, column=0)


if __name__ == "__main__":
    app = ctk.CTk()
    About(app)
    app.mainloop()
