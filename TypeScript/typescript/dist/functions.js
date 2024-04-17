"use strict";
function add(num1, num2, num3) {
    return num3 ? num1 + num2 + num3 : num1 + num2;
}
console.log(add(2, 3));
console.log(add(2, 3, 5));
const sub = (num1, num2, num3 = 10) => num1 - num2 - num3;
console.log(sub(2, 3));
console.log(sub(2, 3, 5));
const mult = (num1, num2) => num1 * num2;
console.log(mult(2, 3));
function add2(num1, num2, ...num3) {
    return num1 + num2 + num3.reduce((a, b) => a + b, 0);
}
let numbers = [2, 3, 4];
console.log(add2(2, 5, ...numbers));
// generic function - ccan take any type
function getItems(items) {
    return new Array().concat(items);
}
let concatResult = getItems(numbers);
console.log(concatResult);
let concatString = getItems(["a", "b", "c", "d", "e"]);
console.log(concatString);
//# sourceMappingURL=functions.js.map