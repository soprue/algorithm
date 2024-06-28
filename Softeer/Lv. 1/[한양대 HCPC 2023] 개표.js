const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let isFirstLine = true;
let testCaseCount;

rl.on("line", (input) => {
    if(isFirstLine) {
        testCaseCount = parseInt(input.trim());
        isFirstLine = false;
    } else {
        const n = parseInt(input.trim());
        const devision = Math.floor(n / 5);
        const remainder = n % 5;
        console.log("++++ ".repeat(devision) + "|".repeat(remainder));
    }
});

rl.on("close", () => {
    
});
