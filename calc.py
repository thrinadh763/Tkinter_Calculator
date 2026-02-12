import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
entry1 = tk.Entry(root, font=("Bold", 24), bg="black", fg="white", bd=0, justify="right")
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
def press(v):
    entry1.insert(tk.END, v)
def clear():
    entry1.delete(0, tk.END)
def cal():
    try:
        result = eval(entry1.get())
        entry1.delete(0, tk.END)
        entry1.insert(0, result)
    except:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Error")
tk.Button(root, text="Clear", font=("bold", 20), command=clear, width=10, height=2, bd=0, bg="gray", fg="white").grid(row=1, column=0, columnspan=4, padx=6, pady=6)
r, c = 2, 0
for i in buttons:
    if i == "=":
        cmd = cal  
    else:
        cmd = lambda x=i: press(x)
    color = "red" if i in {"+", "-", "*", "/", "="} else "black"
    tk.Button(root, text=i, font=("bold", 20), command=cmd, width=6, height=2, bd=0, bg=color, fg="white").grid(row=r, column=c, padx=6, pady=6)
    c += 1
    if c == 4:
        c = 0
        r += 1
root.mainloop()
