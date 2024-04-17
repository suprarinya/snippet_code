function add(num1: number, num2: number, num3?: number) : number {
    return num3 ? num1 + num2 + num3 : num1 + num2
}

console.log(add(2, 3));
console.log(add(2, 3, 5));


const sub  = (num1: number, num2: number, num3 = 10) : number => num1 - num2 - num3

console.log(sub(2, 3));
console.log(sub(2, 3, 5));


const mult = (num1: number, num2: number) : number => num1 * num2

console.log(mult(2,3));

function add2(num1: number, num2: number, ...num3: number[]) : number {
    return num1 + num2 + num3.reduce((a, b) => a + b, 0)
}

let numbers = [2, 3, 4]
console.log(add2(2, 5, ...numbers));

// generic function - ccan take any type
function getItems<T>(items: T[]) :T[] {
    return new Array<T>().concat(items)
}

let concatResult = getItems<number>(numbers)
console.log(concatResult);

let concatString = getItems<string>(["a", "b", "c", "d", "e"])
console.log(concatString);


