const Person = {
    init(saying) {
        this.saying = saying
        return this
    },

    talk() {
        console.log(`I say: ${this.saying}`)
    }
}

function create(constructor) {
    const obj = {}
    Object.setPrototypeOf(obj, constructor)
    return obj
}

var crockford = create(Person).init("semicolons")
crockford.talk()

