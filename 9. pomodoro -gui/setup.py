import tkinter as tk
import customtkinter  # Import your custom tkinter library

def on_click():
    tk.messagebox.showinfo("Message", "Hello! This is a desktop app.")

# Create the main window
root = customtkinter.CTk()  # If you're using customtkinter for a custom look
root.title("My Desktop App")

# Create a button
button = customtkinter.CTkButton(root, text="Click Me!", command=on_click)
button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
