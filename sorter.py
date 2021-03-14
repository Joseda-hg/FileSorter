from sys import argv
from config import *

# script, directory = argv

#Crear archivo config si no existe
if not os.path.exists("config.py"):
    c = open("config.py","x")
    c.write("")

def sortalg(directory):
    for i in ListadeReglas:
        i.mover(directory)

directory = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles"
sortalg(directory)

#Crear logging para mantener un control de todos los archivos
