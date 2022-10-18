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

// function writeRuletoJson(Regla){
// fs.writeFile


import { readFile } from "fs"
readFile("./rules.json", "utf8", (err, jsonString) => {
    if (err) {
        console.log("File read failed:", err);
        return;
    }
    console.log("File data:", jsonString);
});



const fs = require("fs");
fs.readFile("./customer.json", "utf8", (err, jsonString) => {
  if (err) {
    console.log("Error reading file from disk:", err);
    return;
  }
  try {
    const customer = JSON.parse(jsonString);
    console.log("Customer address is:", customer.address); // => "Customer address is: Infinity Loop Drive"
  } catch (err) {
    console.log("Error parsing JSON string:", err);
  }
});



const fs = require('fs')
const customer = {
    name: "Newbie Co.",
    order_count: 0,
    address: "Po Box City",
}
const jsonString = JSON.stringify(customer)fs.writeFile('./newCustomer.json', jsonString, err => {
    if (err) {
        console.log('Error writing file', err)
    } else {
        console.log('Successfully wrote file')
    }
})


const jsonString = JSON.stringify(customer)fs.writeFileSync('./newCustomer.json', jsonString)


jsonReader("./customer.json", (err, customer) => {
    if (err) {
      console.log("Error reading file:", err);
      return;
    }
    // increase customer order count by 1
    customer.order_count += 1;
    fs.writeFile("./customer.json", JSON.stringify(customer), err => {
      if (err) console.log("Error writing file:", err);
    });
  });
  