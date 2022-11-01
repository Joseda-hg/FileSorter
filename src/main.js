import añadirRegla from "./controllers/añadirRegla"

class Regla {
  constructor(extensiones, nombre, destino) {
    this.active = false;
    this.nombre = nombre;
    this.extensiones = extensiones;
    this.destino = destino;
  }
}

let ruleList = []

function fetchFun(){
  fetch('./rules.json')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
}
//   // Write rows from



//   Extract a logger Function

function loguer() {
  let logger = document.getElementById("logger")
  let nOfLines = 4
  let i = 0
  while (i < nOfLines) { 
    logger.innerHTML += "<p>Prueba de linea de Log</p>"
    i++
  }
}

