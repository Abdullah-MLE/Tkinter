# ---------------------------- IMPORT ------------------------------- #
import tkinter as tk
import customtkinter as ctk
from mytools import MyButton, WIDTH, HEIGHT, PAD, BG_COLOR, FRAME_BG_COLOR

# ---------------------------- GLOBAL ------------------------------- #
app = ctk.CTk()
navigation_bar1 = ctk.CTkFrame(master=app)
navigation_bar = ctk.CTkFrame(master=navigation_bar1)
working_frame1 = ctk.CTkFrame(master=app)
working_frame = ctk.CTkFrame(master=working_frame1)
navigation_bar_photo = tk.PhotoImage(file="navigation_bar_photo.png")


def main_app():
    screen_initialize()
    navigation_bar_initialize()
    working_frame_initialize()
    app.mainloop()

def screen_initialize():
    app.config(background=BG_COLOR)

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width - WIDTH) // 2
    y = (screen_height - HEIGHT) // 2

    app.geometry(f"{WIDTH}x{HEIGHT}+{x + 120}+{y + 50}")

    app.title("FlipWords")
    app.iconbitmap("logo.ico")

def navigation_bar_initialize():
    navigation_bar1.configure(width=420, height=HEIGHT, fg_color=FRAME_BG_COLOR, corner_radius=10)
    navigation_bar1.pack(side=ctk.LEFT, pady=10)
    navigation_bar1.pack_propagate(False)
    navigation_bar.configure(fg_color=FRAME_BG_COLOR, corner_radius=10)
    navigation_bar.pack(side=ctk.LEFT)

    canvas = tk.Canvas(master=navigation_bar, width=500, height=300, bg=BG_COLOR, highlightthickness=0)
    canvas.create_image(250, 150, image=navigation_bar_photo)
    canvas.grid(column=0, row=0, pady=PAD, padx=PAD)

    study_button = MyButton(master=navigation_bar, text="Study", command=study_method)
    study_button.grid(column=0, row=1, pady=PAD, padx=PAD)

    review_button = MyButton(master=navigation_bar, text="Review", command=review_method)
    review_button.grid(column=0, row=2, pady=PAD, padx=PAD)

    add_word_button = MyButton(master=navigation_bar, text="Add New Word", command=add_method)
    add_word_button.grid(column=0, row=3, pady=PAD, padx=PAD)

    search_button = MyButton(master=navigation_bar, text="Search", command=search_method)
    search_button.grid(column=0, row=4, pady=PAD, padx=PAD)

    update_word_button = MyButton(master=navigation_bar, text="Update", command=update_method)
    update_word_button.grid(column=0, row=5, pady=PAD, padx=PAD)

    delete_word_button = MyButton(master=navigation_bar, text="Delete", command=delete_method)
    delete_word_button.grid(column=0, row=6, pady=PAD, padx=PAD)

    show_all_words_button = MyButton(master=navigation_bar, text="Show All Words", command=show_all_words)
    show_all_words_button.grid(column=0, row=7, pady=PAD, padx=PAD)

    about_button = MyButton(master=navigation_bar, text="About", command=about_method)
    about_button.grid(column=0, row=9, pady=PAD, padx=PAD)

def working_frame_initialize():
    working_frame1.configure(width=1200, height=HEIGHT, fg_color=FRAME_BG_COLOR, corner_radius=10)
    working_frame1.pack(side=ctk.LEFT, padx=10, pady=10)
    working_frame1.pack_propagate(False)

    working_frame.configure(fg_color=FRAME_BG_COLOR)
    working_frame.pack()

def add_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from add_new_word import Add
    Add(working_frame)

def search_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from search import Search
    Search(working_frame)

def update_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from update import Update
    Update(working_frame)

def delete_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from delete import Delete
    Delete(working_frame)

def study_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from session import Session
    Session(working_frame, 'new')

def review_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from session import Session
    Session(working_frame, 'old')

def show_all_words():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from show_all_words import ShowAllWords
    ShowAllWords(working_frame)

def about_method():
    for widget in working_frame.winfo_children():
        widget.destroy()
    from about import About
    About(working_frame)


if __name__ == "__main__":
    main_app()
