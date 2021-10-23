# Python-Sorter
 A tool that lets you sort files into folders on command or automatically

El script sorter.py recibe como parametros un directorio y lo organiza con las reglas existentes dentro de config.py

Las reglas pueden crearse en config.py, con la estructura: RegladeMovimiento(nombre, extensiones afectadas, directorio target al cual mover los archivos)
Ejemplo = 
reglaImagenes = RegladeMovimiento("Imagenes", ["jpg","png"],"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/imagen")

La GUI aun no esta implementada, su uso habitual es mediante la linea de comandos

