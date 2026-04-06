const nombreProducto = "Tablet 10 pulgadas";

let precio = 450.99;

let stock = 25; 

const envioGratis = true;

console.log(`Nombre del producto -> ${nombreProducto}`)
console.log(`Precio del producto -> ${precio}`)
console.log(`Cuantas hay disponibles -> ${stock}`)
console.log(`Envio gratis? -> ${envioGratis}`)



const cliente = 2;
let subtotal = precio * cliente;
let total = subtotal * 0.07;
console.log("Subtotal -> $" + subtotal.toFixed(2));
console.log("Total final -> $" + total.toFixed(2));

