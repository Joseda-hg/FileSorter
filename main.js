function añadirRegla() {
  const extensiones = document.getElementById("inputExtensiones").value
  const nombre = document.getElementById("inputTipo").value
  const destino = document.getElementById("inputDireccion").value
  alert(`La regla añadida es la siguiente ${extensiones}, ${nombre}, ${destino}`)
  return
}

let addButton = document.getElementById("addButton")
addButton.addEventListener('click', event => {
  añadirRegla()
})


class Regla {
  constructor(extensiones, nombre, destino) {
    this.active = False;
    this.nombre = nombre;
    this.extensiones = extensiones;
    this.destino = destino;
  }
}

let ruleList = []

fetch('./rules.json')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));


  

// Extract a logger Function
logger = document.getElementById("logger")
nOfLines = 4
i = 0
while (i < nOfLines) { 
  logger.innerHTML += "<p>Prueba de linea de Log</p>"
  i++
}
