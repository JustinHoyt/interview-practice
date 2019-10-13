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

inquirer
    .prompt(questions)
    .then(answers => {
        const { factorial, numberOfLoops } = answers;
        for(i = 0; i < numberOfLoops; i++) {
            console.log(factorial * factorial);
        }
    });
