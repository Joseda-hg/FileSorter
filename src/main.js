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
      this.active = false;
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
  // Write rows from
  
    
  
  // Extract a logger Function
let  logger = document.getElementById("logger")
  let nOfLines = 4
  let i = 0
  while (i < nOfLines) { 
    logger.innerHTML += "<p>Prueba de linea de Log</p>"
    i++
  }
  
  