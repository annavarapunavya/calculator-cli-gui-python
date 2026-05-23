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

# Run application
root.mainloop()