const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let A, B;

rl.on('line', (input) => {
    [A, B] = input.split(" ");
});

rl.on('close', () => {
    if(A > B) console.log("A");
    else if(A < B) console.log("B");
    else if(A === B) console.log("same");
});
