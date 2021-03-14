import os

ListaExtensiones = ["txt", "mp3", "mp4", "jpg", "exe"]

ListaDirectorios = ["documentos", "ejecutables", "imagen", "musica", "video"]
for directorio in ListaDirectorios:
    for extension in ListaExtensiones:
        if os.path.exists(f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/{directorio}/myfile.{extension}"):
            os.remove(f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/{directorio}/myfile.{extension}")
        else:
            print("The file does not exist")


for i in ListaExtensiones:
    if not os.path.exists(f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/myfile.{i}"):
        f = open(f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/myfile.{i}","x")