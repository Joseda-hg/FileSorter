from config import *

# print(reglaImagenes)
# print(ListadeReglas)


Working_Directory = os.getcwd()
Absolute_Path = os.path.realpath(__file__)
print(f" El Working directory es: { Working_Directory }")
print(f" El Path del script es: { Absolute_Path }")

origin_path = Absolute_Path + "\\origin"

ListaDirectorios = ["documentos", "ejecutables", "imagen", "musica", "video"]
# Destinos
for i in ListaDirectorios:
    if not os.path.exists(f"{Absolute_Path}\\destinos\\{i}"):
        f = open(
            f"{Absolute_Path}\\destinos\\{i}", "x")
