function Person(saying) {
    this.saying = saying
}

Person.prototype.talk = function() {
    console.log('I say: ', this.saying)
}

function new1(constructor, ...args) {
    const obj = {}
    Object.setPrototypeOf(obj, constructor.prototype)
    return constructor.apply(obj, args) || obj
}

var crockford = new1(Person, 'semicolons')
crockford.talk()
