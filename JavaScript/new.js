function Person(saying) {
    this.saying = saying
}

Person.prototype.talk = function() {
    console.log('I say: ', this.saying)
}

function new1(constructor) {
    const obj = {}
    const args = [...arguments].slice(1)
    Object.setPrototypeOf(obj, constructor.prototype)
    console.log(constructor.apply(obj, args) )
    return constructor.apply(obj, args) || obj
}

var crockford = new1(Person, 'semicolons')
console.log(crockford)
crockford.talk()
