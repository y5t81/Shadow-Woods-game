# I acknowledge the use of AI (ChatGPT – GPT-5) in the development of this project.

import tkinter as tk

# --- GAME LOGIC ---

def start_game():
    text.set("You are in Shadow Woods.\nDo you want to go left or right?")
    make_buttons(["Left", "Right"], [left_path, right_path])

def left_path():
    text.set("You discover an old cabin with a glowing door!\nDo you ENTER or IGNORE it?")
    make_buttons(["Enter", "Ignore"], [enter_cabin, ignore_cabin])

def right_path():
    text.set("A tall figure emerges from the trees...\nYou are never seen again.\nGAME OVER.")
    make_buttons(["Restart"], [start_game])

def enter_cabin():
    text.set("Inside, you see a dusty book on a table.\nDo you READ or LEAVE it?")
    make_buttons(["Read", "Leave"], [read_book, leave_book])

def ignore_cabin():
    text.set("You walk away, but something follows you...\nYou vanish into the darkness.\nGAME OVER.")
    make_buttons(["Restart"], [start_game])

def read_book():
    text.set("The book grants you forbidden knowledge.\nYou escape safely!\nYOU WIN!")
    make_buttons(["Restart"], [start_game])

def leave_book():
    text.set("A shadow rises from the book and consumes you!\nGAME OVER.")
    make_buttons(["Restart"], [start_game])

# --- GUI HELPERS ---

def make_buttons(labels, commands):
    for widget in button_frame.winfo_children():
        widget.destroy()

    for lbl, cmd in zip(labels, commands):
        tk.Button(button_frame, text=lbl, command=cmd, width=20).pack(pady=3)
          
    print("You feel a cold breeze as you enter...")

# --- WINDOW SETUP ---

window = tk.Tk()
window.title("Shadow Woods")

text = tk.StringVar()
label = tk.Label(window, textvariable=text, wraplength=400, height=6)
label.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack()

start_game()

window.mainloop()
