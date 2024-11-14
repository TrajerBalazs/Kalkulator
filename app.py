import tkinter as tk
from tkinter import messagebox

# Függvények a műveletekhez
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Eredmény: " + str(result))
    except ValueError:
        messagebox.showerror("Hiba", "Kérlek, adj meg érvényes számokat!")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Eredmény: " + str(result))
    except ValueError:
        messagebox.showerror("Hiba", "Kérlek, adj meg érvényes számokat!")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Eredmény: " + str(result))
    except ValueError:
        messagebox.showerror("Hiba", "Kérlek, adj meg érvényes számokat!")

def divide():
    try:
        divisor = float(entry2.get())
        if divisor == 0:
            messagebox.showerror("Hiba", "Nem oszthatunk nullával!")
            return
        result = float(entry1.get()) / divisor
        result_label.config(text="Eredmény: " + str(result))
    except ValueError:
        messagebox.showerror("Hiba", "Kérlek, adj meg érvényes számokat!")

# Tkinter ablak beállítása
root = tk.Tk()
root.title("Egyszerű Kalkulátor")

# Beviteli mezők
tk.Label(root, text="Első szám:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Második szám:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Műveleti gombok
tk.Button(root, text="Összeadás", command=add).grid(row=2, column=0, sticky="ew")
tk.Button(root, text="Kivonás", command=subtract).grid(row=2, column=1, sticky="ew")
tk.Button(root, text="Szorzás", command=multiply).grid(row=3, column=0, sticky="ew")
tk.Button(root, text="Osztás", command=divide).grid(row=3, column=1, sticky="ew")

# Eredmény kiírása
result_label = tk.Label(root, text="Eredmény: ")
result_label.grid(row=4, column=0, columnspan=2)

# Tkinter ablak indítása
root.mainloop()
