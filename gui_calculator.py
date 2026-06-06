import tkinter as tk

# Create window
root = tk.Tk()

# Window title
root.title("Calculator")

# Window size
root.geometry("300x400")

#Display screen
display = tk.Entry(root, width=25, font=("Arial", 20), borderwidth=5)
display.pack(pady=20)

def button_click(value):

    current = display.get()

    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(0, result)

        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    else:
        display.insert(tk.END, value)

#Button Frame
button_frame = tk.Frame(root)
button_frame.pack()
#Number buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(
    button_frame,
    text=button,
    width=5,
    height=2,
    font=("Arial", 14),
    command=lambda value=button: button_click(value)
)

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1
# Run application
root.mainloop()