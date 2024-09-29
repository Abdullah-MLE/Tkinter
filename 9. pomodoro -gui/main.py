import customtkinter as ctk
import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def scoreboard():
    score_label = ctk.CTkLabel(master=main_frame, text="", font=(f"{FONT_NAME} bold", 20))
    score_label.place(x=230, y=160)

    if score == 1:
        score_label.configure(text="✔")
    elif score == 2:
        score_label.configure(text="✔ ✔")
    elif score == 3:
        score_label.configure(text="✔ ✔ ✔")
    elif score == 4:
        score_label.configure(text="✔ ✔ ✔ ✔")






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    if time == -1:
        work_time_combobox.configure(state="normal")
        rest_time_combobox.configure(state="normal")
        break_button.configure(state="normal")
        global score
        if score == 3:
            score += 1
            scoreboard()
            state_label.configure(text="Break")
            score = 0
            state_label.configure(text="")
            work_time_combobox.configure(state="disabled")
            rest_time_combobox.configure(state="disabled")

            photo.config(file="break.png")
            canvas.create_image(200, 200, image=photo)

            count_down(20 * 60)
        else:
            score += 1
            scoreboard()

        return True
    elif timer_on is False:
        work_time_combobox.configure(state="normal")
        rest_time_combobox.configure(state="normal")
        break_button.configure(state="normal")
        return False
    app.after(1, count_down, time - 1)
    time_label.configure(text=f"{time // 60:02}:{time % 60:02}")

# ---------------------------- UI SETUP ------------------------------- #
def start_method():
    global timer_on, score
    timer_on = True
    state_label.configure(text="Work")
    work_time_combobox.configure(state="disabled")
    rest_time_combobox.configure(state="disabled")
    count_down(selected_time*60)


def start_break():
    global timer_on
    timer_on = True
    state_label.configure(text="Break")
    work_time_combobox.configure(state="disabled")
    rest_time_combobox.configure(state="disabled")

    photo.config(file="break.png")
    canvas.create_image(200, 200, image=photo)

    count_down(selected_break*60)

def reset_method():
    global timer_on
    timer_on = False
    state_label.configure(text="STOP")
    work_time_combobox.configure(state="normal")
    rest_time_combobox.configure(state="normal")

def set_time(x):
    global selected_time
    time = int(x[-2:])
    selected_time = time
    if time == 13:
        photo.config(file="carrot.png")
        time_label.configure(text="13:00")
        rest_time_combobox.set("fast : 2")
    elif time == 25:
        photo.config(file="pomodoro.png")
        time_label.configure(text="25:00")
        rest_time_combobox.set("good : 5")
    elif time == 55:
        photo.config(file="potato.png")
        time_label.configure(text="55:00")
        rest_time_combobox.set("good : 5")
    elif time == 80:
        photo.config(file="broccoli.png")
        time_label.configure(text="80:00")
        rest_time_combobox.set("long : 10")
    canvas.create_image(200, 200, image=photo)

def set_brake(x):
    global selected_break
    selected_break = int(x[-2:])

app = ctk.CTk()
width = 600
height = 600
app.geometry(f'{width}x{height}')

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
app.geometry(f"{width}x{height}+{x}+{y}")
app.title("Pomodoro")
app.config(background="#010311")

app.iconbitmap("pomodoro.ico")

main_frame = ctk.CTkFrame(master=app, width=550, height=550, fg_color="#090b1a", border_color="#00127a", border_width=2)
main_frame.place(relx=0.5, rely=0.5, anchor='center')

work_tile_label = ctk.CTkLabel(master=main_frame, text="work time", font=(f"{FONT_NAME} bold", 20), text_color="white")
work_tile_label.place(x=20, y=20)

work_time_combobox = ctk.CTkComboBox(master=main_frame, values=["Carrot : 13", "Pomodoro : 25", "Potato : 55", "Broccoli : 80"], command=set_time)
work_time_combobox.place(x=120, y=20)
work_time_combobox.set("Pomodoro : 25")

rest_tile_label = ctk.CTkLabel(master=main_frame, text="rest time", font=(f"{FONT_NAME} bold", 20), text_color="white")
rest_tile_label.place(x=300, y=20)

rest_time_combobox = ctk.CTkComboBox(master=main_frame, values=["fast : 2", "good : 5", "long : 10"], command=set_brake)
rest_time_combobox.place(x=390, y=20)
rest_time_combobox.set("good : 5")

state_label = ctk.CTkLabel(master=main_frame, text="Start", font=(f"{FONT_NAME} bold", 80), text_color="white")
state_label.place(x=180, y=80)

photo = tk.PhotoImage(file="pomodoro.png")
canvas = tk.Canvas(master=main_frame, width=400, height=400, bg="#090b1a", highlightthickness=0)
canvas.create_image(200, 200, image=photo)
canvas.place(x=150 , y=250)

time_label = ctk.CTkLabel(master=main_frame, text="25:00", font=(f"{FONT_NAME} bold", 60), text_color="white")
time_label.place(x=205, y=330)


start_button = ctk.CTkButton(master=main_frame, text="Start", corner_radius=32, fg_color="#008000", hover_color="#1abd1a", command=start_method)
start_button.place(x=20, y=500)

break_button = ctk.CTkButton(master=main_frame, text="Break", corner_radius=32, fg_color="transparent", border_width=2, command=start_break, state="disabled")
break_button.place(x=200, y=500)

reset_button = ctk.CTkButton(master=main_frame, text="Reset", corner_radius=32, fg_color="#c40c0c", hover_color="#de3737", command=reset_method)
reset_button.place(x=390, y=500)

selected_time = 25
selected_break = 5
timer_on = True
score = 0

app.mainloop()












