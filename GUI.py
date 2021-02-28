from tkinter import *

window = Tk()

window.title("Welcome to the Sorter app")
window.geometry("1400x100")


lbl = Label(window, text="This program sorts files into the folders that you pick", font=("Arial bold", 30))
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=0)

txt = 


window.mainloop()

