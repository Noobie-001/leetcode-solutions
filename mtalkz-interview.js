//change value to variables without using temp variable
let a = 5;
let b = 10;

a = a + b; 
b = a - b; 
a = a - b;

console.log("Value of a:", a); 
console.log("Value of b:", b);          