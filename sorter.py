from os import listdir
from os.path import isfile, join
from shutil import move

directory = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles"
onlyfiles = [i for i in listdir(directory) if isfile(join(directory, i))]

documentosExt = ["txt"]
documentosTar = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/documentos"

imagenesExt = ["jpg"]
imagenesTar = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/imagen"

musicaExt = ["mp3"]
musicaTar = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/musica"

videosExt = ["mp4"]
videosTar = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/video"

descargasExt = ["exe"]
descargasTar = "C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/ejecutables"

for i in onlyfiles:
    fileExtension = i.split(".")[1]

    if fileExtension in documentosExt:
        print(f"{i}Es un documentos")
        move(directory + "/" + i, documentosTar + "/" + i)
        print(f"Moviendo {i} a {documentosTar}")

    elif fileExtension in imagenesExt:
        print(f"{i}Es un imagenes")
        move(directory + "/" + i, imagenesTar + "/" + i)
        print(f"Moviendo {i} a {imagenesTar}")

    elif fileExtension in musicaExt:
        print(f"{i}Es un musica")
        move(directory + "/" + i, musicaTar + "/" + i)
        print(f"Moviendo {i} a {musicaTar}")  

    elif fileExtension in videosExt:
        print(f"{i}Es un videos")
        move(directory + "/" + i, videosTar + "/" + i)
        print(f"Moviendo {i} a {videosTar}")

    elif fileExtension in descargasExt:
        print(f"{i}Es un ejecutable")
        move(directory + "/" + i, descargasTar + "/" + i)
        print(f"Moviendo {i} a {descargasTar}")

    else:
        print(f"{i}No se que es")




# Objeto Teoria
# movementAction 
# Directorio
# Target 
# Extensiones Objetivos

# Lista de Archivos
    #cada Archivo
    #Extension