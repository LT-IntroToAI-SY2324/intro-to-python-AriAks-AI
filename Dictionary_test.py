# fullname = input("what is your full name?")
# names = fullname.split()
# print(names)
# names.reverse()
# print(names)
# First_name = names.pop()
# print(names)
# print("Hello " + First_name + "!")
# ani = ["fox", "dog", "bunny"]

# Dict = {"Cities": ["chicago", "orlando", "san Francisco"], "states": ["Illinois", "florida", "California"], "Animal": ani}
# ans = input("Whta would you like to know about?")
# print(Dict[ans])
# x = [4, 3, 5, 5]
# y=1

# new = []
# for i in x:
#     new.append(x[y])
#     y = y + 2

import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(1.0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            screen.delete(1.0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(1.0, tk.END)
    else:
        screen.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

# Create the display screen
screen = tk.Text(root, font=('arial', 20), height=2, wrap=tk.WORD)
screen.pack(fill=tk.BOTH, expand=True)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0),
]

for (text, row, col) in button_texts:
    button = tk.Button(button_frame, text=text, font=('arial', 20), width=5, height=2)
    button.grid(row=row, column=col, padx=10, pady=10)
    button.bind("<Button-1>", on_button_click)

# Run the main loop
root.mainloop()
