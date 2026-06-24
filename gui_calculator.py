import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("440x500")
root.resizable(False, False)

result_shown = False

# Display screen
display = tk.Entry(
    root,
    width=25,
    font=("Arial", 20),
    borderwidth=5,
    justify="right"
)
display.pack(pady=20)


def button_click(value):
    global result_shown

    current = display.get()

    # Clear screen
    if value == "C":
        display.delete(0, tk.END)
        result_shown = False

    # Backspace
    elif value == "⌫":
        display.delete(0, tk.END)
        display.insert(0, current[:-1])

    # Calculate result
    elif value == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(0, result)
            result_shown = True

        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            result_shown = True

    # Operators
    elif value in ["+", "-", "*", "/"]:
        if current == "Error":
            display.delete(0, tk.END)

        result_shown = False
        display.insert(tk.END, value)

    # Numbers and decimal point
    else:
        if result_shown:
            display.delete(0, tk.END)
            result_shown = False

        if current == "Error":
            display.delete(0, tk.END)

        display.insert(tk.END, value)


# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "⌫", "+",
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(
        button_frame,
        text=button,
        width=6,
        height=2,
        font=("Arial", 14),
        command=lambda value=button: button_click(value)
    )

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1

# Equal button
equal_btn = tk.Button(
    button_frame,
    text="=",
    width=28,
    height=2,
    font=("Arial", 14),
    command=lambda: button_click("=")
)

equal_btn.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

# Run application
root.mainloop()