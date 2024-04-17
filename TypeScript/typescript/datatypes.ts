let lname : string

lname = "Iris"

let newname = lname.toUpperCase()

console.log(newname);

let age : number

age = 25.5

let dob = "25"

let result = parseInt(dob)

console.log(result);

let isValid : boolean = true;

console.log(isValid);

let empList : string[]
empList = ["Iris", "Kara", "Renato"]

let numList : Array<number>
numList = [1,2,3,4,5]

let result1 = numList.filter((num) => num > 2)
console.log(result1);

let result2 = numList.find((num) => num > 3)
console.log(result2);

let result3 = empList.find((p) => p === 'Kara')
console.log(result3);

let sum = numList.reduce((acc, num) => acc + num)
console.log(sum);

const enum Color {
    Red,
    Green,
    Blue
}

// enum
let c : Color = Color.Blue

// tuple -> for return multiple values
let swapNumber: [number, number]

function swapNumbers(num1: number, num2: number) : [number, number] {
    return [num2, num1]
}

swapNumber = swapNumbers(10,20)
console.log(swapNumber[0]);
console.log(swapNumber[1]);

// any
let department: any
department = 'IT'
department = 30

