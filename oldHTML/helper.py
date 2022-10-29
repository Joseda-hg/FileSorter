 import os
# Este archivo existe con la intencion de crear/eliminar los archivos movidos por el programar,
# asi como crear archivos para probar la funcionalidad del mismo

ListaExtensiones = ["txt", "mp3", "mp4", "jpg", "exe"]
ListaDirectorios = ["documentos", "ejecutables", "imagen", "musica", "video"]

Working_Directory = os.getcwd

for directorio in ListaDirectorios:
    for extension in ListaExtensiones:
        if os.path.exists(f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/{directorio}/myfile.{extension}"):
            os.remove(
                f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/{directorio}/myfile.{extension}")
        else:
            print("The file does not exist")


for i in ListaExtensiones:
    # Si el archivo no existe, open con el parametro "x" lo crea
    if not os.path.exists(f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/myfile.{i}"):
        f = open(
            f"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/myfile.{i}", "x")
