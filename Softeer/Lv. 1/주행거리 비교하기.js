const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let A, B;

rl.on('line', (input) => {
    const [A, B] = input.split(" ").map(Number);

    if (A > B) console.log("A");
    else if (A < B) console.log("B");
    else console.log("same");

    rl.close();
});
