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

#Button Frame
button_frame = tk.Frame(root)
button_frame.pack()
#Number buttons
button1 = tk.Button(button_frame, text="1", width=5, height =2)
button2 = tk.Button(button_frame, text="2", width=5, height =2)
button3 = tk.Button(button_frame, text="3", width=5, height =2)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
# Run application
root.mainloop()