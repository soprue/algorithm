const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let isFirstLine = true;
let n;

rl.on("line", (input) => {
    if (isFirstLine) {
        n = parseInt(input.trim());
        isFirstLine = false;
    } else {
        let towns = input.split(" ").map(Number);
        let distances = towns.slice(1).map((value, index) => value - towns[index]);

        const minDistance = Math.min(...distances);
        let minCount = distances.filter(value => value === minDistance).length;

        console.log(minCount);
        
        rl.close();
    }
});
