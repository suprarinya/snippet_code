import { Login, User } from './interface';
// import * as UserLogin from './interface';

interface Address {
    street:  string;
    city: string;
    state: string;
    pin: string;
}

// if want to retain 'type' in javascript -> use class instead
// of interface (there's no interface in javascript -> type is gone)
// eg: write api -> use class, not interface
class Employee implements Login {
    #id: number; // private - can't access from outside
    
    protected name: string; // protected - can access only in class and its subclass (extends (inheritance))
    
    address: Address;

    get empId() : number {
        return this.#id
    }

    set empId(id: number) {
        this.#id = id
    }

    static getEmployeeCount() : number {
        return 50
    }
    
    constructor(id: number, name: string, address: Address){
        this.#id = id
        this.name = name
        this.address = address
    }

    login(): User {
        return {name: "Iris", id: 1, email: ""};
    }

    getNameWithAddress() : string {
        return `${this.name} ${this.address}`
    }
}

let count = Employee.getEmployeeCount()

let john = new Employee(1, 'John', {
    street:  'ABC',
    city: 'Bangkok',
    state: 'Thailand',
    pin: '10240',
})
john.empId = 100

class Manager extends Employee {
    constructor (id: number, name: string, address: Address) {
        super(id, name, address)
    }

    getNameWithAddress() : string {
        return  `${this.name} is a manager at the ${this.address}`
    }
}

let mana = new Manager(1, 'Mana',  {
    street:  'DEF',
    city: 'Bangkok',
    state: 'Thailand',
    pin: '10230',
})

// john.id = 1
// john.name = 'John'
// john.address = 'Highway 71'

console.log(john);
console.log(john.getNameWithAddress());
console.log(mana.getNameWithAddress());
console.log(count);
console.log('john ID is: ' + john.empId);



