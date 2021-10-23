from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

# import sorter 

# def browse():
#     filename=filedialog.askdirectory(mustexist = True, initialdir = "C:/Users/",title = "Select directory")
    
# def sort():
#     sorter.sortalg(directoryToSort)

window = Tk()
directoryToSort = ""

window.title("Welcome to the Sorter app")
window.state('zoomed')


lbl = Label(window, text="This program sorts files into the folders that you pick", font=("Arial bold", 30))
lbl.grid(column=0, row=0)

lbl3 = Label(window, text="Seleccionar carpeta to sort", font=("Arial bold", 30))
lbl3.grid(column=0, row=2)

lbl4 = Label(window, text="Categorias y reglas para hacer Sorting", font=("Arial bold", 30))
lbl4.grid(column=0, row=5)

lbl5 = Label(window, text="Log of files", font=("Arial bold", 30))
lbl5.grid(column=0, row=6)

btn2 = Button(window, text="Sort",)
btn2.grid(column=2, row=7)



directorybutton = Button(window, text="...")
directorybutton.grid(column=3, row=3)
directoryText = Entry(window,width=50) 
directoryText.grid(column=1, row=2)
directoryText.insert(END, "browse.filename")
directoryText.focus()

window.mainloop()

