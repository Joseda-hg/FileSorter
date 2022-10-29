from sys import argv
from config import *

script, directory = argv


def main():
  # Crear archivo config si no existe
    if not os.path.exists("config.py"):
        c = open("config.py", "x")
        # Todo, añadir valores default al config
        c.write("")
# Sortalg, recibe un directorio y lo ordena de acuerdo a una lista de reglas; 
# Todo, extraer ListadeReglas como otro parametro

    def sortalg(directory):
        for i in ListadeReglas:
            i.mover(directory)

    # directory = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles"
    # sortalg(directory)

# Crear logging para mantener un control de todos los archivos


if __name__ == "__main__":
    main()
