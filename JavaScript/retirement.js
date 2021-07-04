const R = require('ramda');

/**
 * @typedef {Object} Prop
 * @property {number} [growthPercentage]
 * @property {number} [yearsOfSavings]
 * @property {number} initialSavings
 * @property {number} annualSavingsRate
 */

/**
 * Calculates retirement net worth based on a simple set of params
 *
 * @param {Prop} props
 * @returns {number}
 */
function retirement(props) {
    const { growthPercentage=1.07, initialSavings, yearsOfSavings=10, annualSavingsRate } = props;

    /** @type {(amountSavedYearly: number, growthPercentage: number, initialAmount: number) => number} */
    const growNetWorth = R.curry(
        (amountSavedYearly, growthPercentage, initialAmount) => initialAmount * growthPercentage + amountSavedYearly
    );

    /** @type {(fn: (a) => a, n: number) => fn: (a) => a} */
    const applyN = R.compose(R.reduceRight(R.compose, R.identity), R.repeat);

    /** @type {number} */
    const netWorth = applyN(growNetWorth(annualSavingsRate, growthPercentage), yearsOfSavings)(initialSavings);

    /** @type {Intl.NumberFormatOptions} formatOptions */
    const formatOptions = {style: 'currency', currency: 'USD'}

    return Intl.NumberFormat(formatOptions).format(netWorth);
}

console.log(retirement({initialSavings: 350000, annualSavingsRate: 80000}));
