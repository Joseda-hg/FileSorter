# Python-Sorter
 A tool that lets you sort files into folders on command or automatically

El script sorter.py recibe como parametros un directorio y lo organiza con las reglas existentes dentro de config.py

Las reglas pueden crearse en config.py, con la estructura: RegladeMovimiento(nombre, extensiones afectadas, directorio target al cual mover los archivos)
Ejemplo = 
reglaImagenes = RegladeMovimiento("Imagenes", ["jpg","png"],"C:/Users/mikut/Downloads/Prog/sorter/sorter/testFiles/imagen")

La GUI aun no esta implementada, su uso habitual es mediante la linea de comandos

Logica Movimiento
Lista de reglas
Editar reglas

Json Lista de reglas

### Card 
* Crear regla
* Editar
* Eliminar

for each regla{
    generate row
    Key ID/name
}


Log of movement, add in totality

JSON - Read, Write, Update, Create

Despues de terminar los pendientes empaquetar para Tauri y generar un ejecutable, eliminar Python una vez finalizado