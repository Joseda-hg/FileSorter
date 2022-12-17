# Organizador de Archivos

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

Este es un organizador de archivos basado en Javascript/Typescript y empaquetado en Tauri

Para ejecutar una version de desarrollo basta con ejecutar el comando `npm run tauri dev`

El flujo del programa es el siguiente

1. Se selecciona un directorio para trabajar

2. Se ejecutan las reglas seleccionadas (Ninguna por defecto)

3. Se genera un log de los movimientos realizados 
   
   1. Posibilidad de un boton de deshacer el ultimo movimiento

4. La opcion de agregar una regla nueva permite agregar una nueva al listado existente, previa verificacion; Y esta lista se mantiene unicamente en rules.json

5. Permitie la opcion de editar las reglas directamente desde la lista

6. Permitir de agregar la opcion de renombrar archivos al moverlos

7. Permitir opcion de monitorear carpetas especificas

8. # TO DO
- [ ] Añadir reglas a .json 
- [ ] Editar reglas a .json
- [ ] Eliminar reglas del .json
- [ ] Generar lista de reglas desde el .json
- [ ] Añadir el movimiento 
- [ ] Añadir el logging
- [ ] Rediseño Visual
- [ ] Añadir el call a RUST para generar el seleccionador de directorios
