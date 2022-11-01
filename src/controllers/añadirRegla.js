export default function añadirRegla(e){
    e.preventDefault()
    const extensiones = document.getElementById("inputExtensiones").value
    const nombre = document.getElementById("inputTipo").value
    const destino = document.getElementById("inputDireccion").value
    alert(`La regla añadida es la siguiente ${extensiones}, ${nombre}, ${destino}`)
}