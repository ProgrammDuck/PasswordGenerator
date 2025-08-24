import secrets
import string
import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("PassGenerator")
root.geometry("150x200")

def generate_password():
    chars=""
    if letters_enabled.get():
        chars += string.ascii_letters
    if digits_enabled.get():
        chars += string.digits
    if symbols_enabled.get():
        chars += string.punctuation

    if not chars:
        ValueError("Need 1 or more symbols")

    psw = "".join(secrets.choice(chars) for _ in range(int(lenght.get())))
    password.delete(0, tkinter.END)
    password.insert(0, psw)

num_var = tkinter.IntVar(value=10)

ttk.Label(root, text="Length:").grid(row=0, column=1)
lenght = tkinter.Spinbox(root, from_=1, to=1000, textvariable=num_var)
lenght.grid(row=1, column=1, padx=10)

letters_enabled = tkinter.BooleanVar(value=True)
letters = ttk.Checkbutton(root, text="use letters?", variable=letters_enabled)
letters.grid(row=2, column=1)

digits_enabled = tkinter.BooleanVar(value=True)
digits = ttk.Checkbutton(root, text="use digits?", variable=digits_enabled)
digits.grid(row=3, column=1)

symbols_enabled = tkinter.BooleanVar(value=False)
symbols = ttk.Checkbutton(root, text="use special symbols?", variable=symbols_enabled)
symbols.grid(row=4, column=1)

generate = ttk.Button(root, text="Generate", command=generate_password)
generate.grid(row=5, column=1, pady=(20, 0))

password = ttk.Entry(root)
password.grid(row=6, column=1)

root.mainloop()