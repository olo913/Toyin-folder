# from customtkinter import *
# import customtkinter as ctk

# win = ctk()

# win.title("calculator")

# win.geometry("361x320")

# entry = ctk.Entry(win, width=350, font=("Arial", 16))
# entry.pack()

# buttom = ctk.Button(win, text="Submit", font=("Arial", 16))
# buttom.pack(pady=10)

# input_label = ctk.CTkLabel(win, text= "Enter your name", font=("Arial", 20))
# input_label.pack()





# win.mainloop()





import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def click(event):
    text = event.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, ctk.END)
            screen.insert(ctk.END, str(result))
        except Exception as e:
            screen.delete(0, ctk.END)
            screen.insert(ctk.END, "Error")
    elif text == "C":
        screen.delete(0, ctk.END)
    else:
        screen.insert(ctk.END, text)

root = ctk.CTk()
root.title("Simple Calculator")


screen = ctk.CTkEntry(root, font=("Arial", 20), width=300, justify="right")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for button_text in buttons:
    button = ctk.CTkButton(root, text=button_text, font=("Arial", 18), width=60, height=60)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()


