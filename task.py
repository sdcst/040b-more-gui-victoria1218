import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

label3 = tk.Label(window,text="Years")
label1 = tk.Label(window,text="Principal")
label2 = tk.Label(window,text="Interest Rate")
label4 = tk.Label(window, text="Amount")
label5 = tk.Label(window, text="-")
entry1 = tk.Entry(window, width=20)
entry2 = tk.Entry(window, width=20)
entry3 = tk.Entry(window, width=20)
combo1 = ttk.Combobox(window,values=["1","2","3"])


label1.grid(row=1, column=1)
label2.grid(row=1, column=2)
label3.grid(row=1, column=3)
label4.grid(row=4, column=1, sticky=E)
label5.grid(row=3, column=1)
entry1.grid(row=2, column=1)
entry2.grid(row=2, column=2)
entry3.grid(row=4, column=2)
combo1.grid(row=2, column=3)

window.mainloop()

