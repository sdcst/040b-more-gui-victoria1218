import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("675x575")
compass = PhotoImage(file="compass.png")
logo = PhotoImage(file="logo.png")
main = PhotoImage(file="main.png")
minimap = PhotoImage(file="minimap.png")

button1 = tk.Button(window,text="MAP", anchor="center", relief="raised", width=13, height=2)
button2 = tk.Button(window,text="INVENTORY", anchor="center", relief="raised", width=13, height=2)
button3 = tk.Button(window,text="POKEDEX", anchor="center", relief="raised", width=13, height=2)
button4 = tk.Button(window,text="ROSTER", anchor="center", relief="raised", width=13, height=2)
button5 = tk.Button(window,text="JOURNAL", anchor="center", relief="raised", width=13, height=2)
button6 = tk.Button(window,text="HELP", anchor="center", relief="raised", width=13, height=2)
button7 = tk.Button(window,text="SHOP", anchor="center", relief="raised", width=13, height=2)
label1 = tk.Label(window, image = compass)
label2 = tk.Label(window, image=logo)
label3 = tk.Label(window, image=main)
label4 = tk.Label(window, image=minimap)
label5 = tk.Label(window, text="MINI MAP")

label3.place(x=5, y=0)
label1.place(x=5, y=450)
label2.place(x=260, y=475)
label4.place(x=530, y=40)
label5.place(x=555, y=15)
button1.place(x=528, y=150)
button2.place(x=528, y=190)
button3.place(x=528, y=230)
button4.place(x=528, y=270)
button5.place(x=528, y=310)
button6.place(x=528, y=350)
button7.place(x=528, y=390)

window.mainloop()