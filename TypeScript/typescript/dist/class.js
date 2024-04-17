"use strict";
var __classPrivateFieldGet = (this && this.__classPrivateFieldGet) || function (receiver, state, kind, f) {
    if (kind === "a" && !f) throw new TypeError("Private accessor was defined without a getter");
    if (typeof state === "function" ? receiver !== state || !f : !state.has(receiver)) throw new TypeError("Cannot read private member from an object whose class did not declare it");
    return kind === "m" ? f : kind === "a" ? f.call(receiver) : f ? f.value : state.get(receiver);
};
var __classPrivateFieldSet = (this && this.__classPrivateFieldSet) || function (receiver, state, value, kind, f) {
    if (kind === "m") throw new TypeError("Private method is not writable");
    if (kind === "a" && !f) throw new TypeError("Private accessor was defined without a setter");
    if (typeof state === "function" ? receiver !== state || !f : !state.has(receiver)) throw new TypeError("Cannot write private member to an object whose class did not declare it");
    return (kind === "a" ? f.call(receiver, value) : f ? f.value = value : state.set(receiver, value)), value;
};
var _Employee_id;
Object.defineProperty(exports, "__esModule", { value: true });
// if want to retain 'type' in javascript -> use class instead
// of interface (there's no interface in javascript -> type is gone)
// eg: write api -> use class, not interface
class Employee {
    get empId() {
        return __classPrivateFieldGet(this, _Employee_id, "f");
    }
    set empId(id) {
        __classPrivateFieldSet(this, _Employee_id, id, "f");
    }
    static getEmployeeCount() {
        return 50;
    }
    constructor(id, name, address) {
        _Employee_id.set(this, void 0); // private - can't access from outside
        __classPrivateFieldSet(this, _Employee_id, id, "f");
        this.name = name;
        this.address = address;
    }
    login() {
        return { name: "Iris", id: 1, email: "" };
    }
    getNameWithAddress() {
        return `${this.name} ${this.address}`;
    }
}
_Employee_id = new WeakMap();
let count = Employee.getEmployeeCount();
let john = new Employee(1, 'John', {
    street: 'ABC',
    city: 'Bangkok',
    state: 'Thailand',
    pin: '10240',
});
john.empId = 100;
class Manager extends Employee {
    constructor(id, name, address) {
        super(id, name, address);
    }
    getNameWithAddress() {
        return `${this.name} is a manager at the ${this.address}`;
    }
}
let mana = new Manager(1, 'Mana', {
    street: 'DEF',
    city: 'Bangkok',
    state: 'Thailand',
    pin: '10230',
});
// john.id = 1
// john.name = 'John'
// john.address = 'Highway 71'
console.log(john);
console.log(john.getNameWithAddress());
console.log(mana.getNameWithAddress());
console.log(count);
console.log('john ID is: ' + john.empId);
//# sourceMappingURL=class.js.map