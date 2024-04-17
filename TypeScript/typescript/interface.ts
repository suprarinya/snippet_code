export interface User {
    name: string
    age?: number // optional
    id: number
    email: string
}

let { name: userName, email: userLogin }: User = {name: "Iris", id: 1, email: ""}

// user.name;
// user.email;


interface Employees extends User {
    salary: number,
}


let employee: Employees = {name:"Kara", id: 1, email:"", salary:10000} 

export interface Login {
    login(): User;
}

let [user1, user2, ...otherusers]: User[] = [
    { name: "Renato", id: 1, email: ''},
    { name: "Seraphina", id: 2, email: ''},
    { name: "Mana", id: 3, email: ''},
    { name: "Shuri", id: 4, email: ''},
]

console.log(user1);
console.log(user2);
console.log(otherusers);

let result = otherusers.map(user =>  user.name)
let result2 = otherusers.filter(user => user.id > 3)
console.log(result);
console.log(result2);


// decorator - change property of class, interface at runtimes
// @Component({})
// class Component {
//     constructor(public name: string) {
        
//     }
// }




