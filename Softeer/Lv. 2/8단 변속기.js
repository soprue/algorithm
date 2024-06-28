const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    const gears = input.split(' ').map(Number);
    
    if (gears.join(' ') === "1 2 3 4 5 6 7 8") {
        console.log("ascending");
    } else if (gears.join(' ') === "8 7 6 5 4 3 2 1") {
        console.log("descending");
    } else {
        console.log("mixed");
    }

    rl.close();
});
