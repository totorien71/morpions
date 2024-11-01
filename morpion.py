import tkinter as tk

def on_button_click(button):
    button.config(text="X" if button["text"] == "" else "O")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=5, command=lambda i=i, j=j: on_button_click(buttons[i*3+j]))
        button.grid(row=i, column=j)
        buttons.append(button)

root.mainloop()