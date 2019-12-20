let inquirer = require('inquirer');

questions = [
    {
        type: 'input',
        name: 'factorial',
        message:"What number do you want to factorial?",
    },
    {
        type: 'input',
        name: 'numberOfLoops',
        message:"how many times do you want to print the answer?",
    }
]

inquirer.prompt(questions).then(answers => {
        console.log(answers);
        const { factorial, numberOfLoops } = answers;

        result = 1;
        for(i = 1; i <= factorial; i++) {
            result *= i;
        }

        for(i = 0; i < numberOfLoops; i++) {
            console.log(result);
        }
    });

