const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let isFirstLine = true;
let N, stones;

rl.on("line", (input) => {
    if(isFirstLine) {
        N = parseInt(input.trim());
        isFirstLine = false;
    } else {
       stones = input.split(" ").map(Number); 
    }
});

rl.on("close", () => {
    const dp = new Array(N).fill(1);

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < i; j++) {
            if (stones[j] < stones[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    
    console.log(Math.max(...dp));
})
