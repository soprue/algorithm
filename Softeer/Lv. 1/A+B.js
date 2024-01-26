const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let sum;
let arr = [];

rl.on('line', (input) => {
  sum = input.split(' ').reduce((acc, cur) => {
    return acc + parseInt(cur);
  }, 0);
  arr.push(sum);
});

rl.on('close', () => {
  const n = arr[0];
  arr.shift();

  arr.map((_, idx) => {
    console.log(`Case #${idx + 1}: ${arr[idx]}`);
  });

  process.exit();
});
