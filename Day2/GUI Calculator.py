import tkinter as tk

def calculate():
    result.set(eval(entry.get()))

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root)
entry.pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
tk.Button(root, text="Calculate", command=calculate).pack()
root.mainloop()
