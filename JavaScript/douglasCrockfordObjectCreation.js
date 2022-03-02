var Car = function (spec) {
    const {maker, year} = spec;
    function ignite() {
        console.log('ignite.....');
    };

    function getMaker() {
        return maker;
    };

    function getAge() {
        return (new Date()).getFullYear() - year;
    };

    return {
        ignite,
        getMaker,
        getAge
    };
};

function Sedan(spec) {
    const type = 'Sedan';
    const car = new Car(spec);
    function drive() {
        console.log(`${car.getMaker()} ${type} drive with ${spec.wheels} weels`);
    }

    return {
        ...car,
        drive,
    };
};

// you can use new
var aCar = new Car({ maker: 'Toyota', year: 2004 });
console.log(aCar.getMaker());  // Toyota
console.log(aCar.getAge());   // 12

// you can exclude new
var honda = new Sedan({ maker: 'Honda', year: 2008, wheels: 4 });

honda.drive();    // "Honda Sedan drive with 4 weels"
honda.ignite();  // ignite....

console.log(honda.getAge()); // 8