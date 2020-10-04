const R = require('ramda');

/**
 * @param {*} props
 * @returns
 */
function retirement(props) {
    const { growthPercentage, initialSavings, yearsOfSavings, annualSavingsRate } = props;

    /** @type {(amountSavedYearly: number, growthPercentage: number, initialAmount: number) => number} */
    const growNetWorth = R.curry(
        (amountSavedYearly, growthPercentage, initialAmount) => initialAmount * growthPercentage + amountSavedYearly
    );

    /** @type {(fn: (a) => a, n: number) => fn: (a) => a} */
    const applyN = R.compose(R.reduceRight(R.compose, R.identity), R.repeat);

    /** @type {number} */
    const netWorth = applyN(growNetWorth(annualSavingsRate, growthPercentage), yearsOfSavings)(initialSavings);

    const formatter = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });

    return formatter.format(netWorth);
}

console.log(retirement({growthPercentage: 1.07, initialSavings: 100000, yearsOfSavings: 20, annualSavingsRate: 100000}));
