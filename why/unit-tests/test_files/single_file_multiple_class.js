class Animal {
    constructor(name, type) {
        this.name = name
        this.type = type
    }
    greet() {
        return `Hello, my name is ${this.name}`
    }
}

class Insect {
    constructor(name, legCount) {
        this.name = name
        this.legCount = legCount
    }
    greet() {
        return `Hello, my name is ${this.name}, I have ${this.legCount} legs.`
    }
}