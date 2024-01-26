const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let sum = 0;

rl.on('line', (input) => {
  const [timeA, timeB] = input.split(' ').map((value) => value.split(':'));
  const hour = (timeB[0] - timeA[0]) * 60;
  const min = timeB[1] - timeA[1];
  sum += hour + min;
});

rl.on('close', () => {
  console.log(sum);
  process.exit();
});
