from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import sorter 

window = Tk()

window.title("Welcome to the Sorter app")
window.state('zoomed')


lbl = Label(window, text="This program sorts files into the folders that you pick", font=("Arial bold", 30))
lbl.grid(column=0, row=0)

lbl3 = Label(window, text="Seleccionar carpeta to sort", font=("Arial bold", 30))
lbl3.grid(column=0, row=2)

lbl4 = Label(window, text="Categorias y reglas para hacer Sorting", font=("Arial bold", 30))
lbl4.grid(column=0, row=5)

def sort():
    sorter.sortalg(directoryToSort)

btn2 = Button(window, text="Sort", command=sort)
btn2.grid(column=2, row=7)


# def clicked():
#     res = "Welcome to " + txt.get()
#     lbl.configure(text = res)

# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=2, row=0)

# txt = Entry(window,width=10,) #state = "disabled"
# txt.grid(column=1, row=0)
# txt.focus()

# combo = Combobox(window)
# combo['values']= (1, 2, 3, 4, 5, "Text")
# combo.current(1) #set the selected item
# combo.grid(column=3, row=0)

directoryToSort = filedialog.askdirectory(mustexist = True, initialdir = "C:/Users/",title = "Select directory")
print(directoryToSort)

directoryText = Entry(window,width=50) #state = "disabled"
directoryText.grid(column=1, row=2)
directoryText.insert(END, directoryToSort)
directoryText.focus()

# print(sorter.reglaImagenes.nombre)
window.mainloop()

