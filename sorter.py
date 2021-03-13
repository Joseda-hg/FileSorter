from os import listdir
from os.path import isfile, join
from shutil import move
from sys import argv

# script, directory = argv

class RegladeMovimiento:
    def __init__(self, nombre, extensiones, target):
        self.nombre = nombre
        self.extensiones = extensiones
        self.target = target
    
    def mover(self, directory):
        onlyfiles = [i for i in listdir(directory) if isfile(join(directory, i))]
        for i in onlyfiles:
            fileExtension = i.split(".")[1]
            if fileExtension in self.extensiones:
                print(f"{i} Es un {self.nombre}")
                move(directory + "/" + i, self.target + "/" + i)
                print(f"Moviendo {i} a {self.target}")


reglaImagenes = RegladeMovimiento("Imagenes", ["jpg","png"],"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/imagen")
reglaDocumentos = RegladeMovimiento("Documentos", ["txt"], "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/documentos")
reglaMusicas = RegladeMovimiento("Musica",["mp3"], "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/musica")
reglaVideos = RegladeMovimiento("Videos", ["mp4"], "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/video")
reglaDescargas = RegladeMovimiento("Descargas", ["exe"], "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/ejecutables" )

ListadeReglas=[reglaImagenes, reglaDocumentos, reglaMusicas, reglaVideos, reglaDescargas]

directory = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles"

# for i in ListadeReglas:
#     i.mover(directory)
