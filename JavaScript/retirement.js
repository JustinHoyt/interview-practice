const R = require('ramda');

function retirement(props) {
    const { growthPercentage, initialSavings, yearsOfSavings, annualSavingsRate } = props;

    const growNetWorth = R.curry(function(amountSavedInPeriod, growthPercentage, initialAmount) {
        return initialAmount * growthPercentage + amountSavedInPeriod;
    });

    const growNetWorthYearly = growNetWorth(annualSavingsRate, growthPercentage);

    const netWorth = R.reduceRight(R.compose, R.identity, R.repeat(growNetWorthYearly, yearsOfSavings))(initialSavings);

    var formatter = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
    return formatter.format(netWorth);
}

console.log(retirement({growthPercentage: 1.07, initialSavings: 100000, yearsOfSavings: 20, annualSavingsRate: 100000}));