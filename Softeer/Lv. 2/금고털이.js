/*
https://softeer.ai/practice/6288

그리디 알고리즘은 각 단계에서 현재 상황에서 가장 좋아 보이는 선택을 하는 방식으로, 이 경우에는 가장 가치가 높은 귀금속을 선택하는 것이다.
주어진 상황에서 루팡은 전동톱을 가지고 있으며, 귀금속을 자를 수 있다. 이는 각 귀금속을 부분적으로만 가져갈 수 있다는 것을 의미한다. 따라서, 귀금속의 총 가치가 아닌 무게당 가치를 기준으로 귀금속을 평가해야 한다.

무게당 가치를 기준으로 귀금속을 내림차순으로 정렬한다. 가장 가치가 높은 귀금속부터 시작하여, 배낭에 넣을 수 있는 한도 내에서 최대한 많은 가치를 담는다.
무게가 많이 나가더라도 전동톱을 사용하여 필요한 만큼만 잘라서 가져갈 수 있기 때문에, 무게에 구애받지 않고 가치가 높은 순서대로 귀금속을 선택하는 것이 최적의 전략이다.
*/

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let totalWeight = 0;
const items = [];
let isFirstLine = true;

rl.on("line", (input) => {
    if (isFirstLine) {
        totalWeight = parseInt(input.split(" ")[0]);
        isFirstLine = false;
    } else {
        const [weight, pricePerKg] = input.split(" ").map(Number);
        items.push({ weight, pricePerKg });
    }
});

rl.on("close", (output) => {
    items.sort((a, b) => b.pricePerKg - a.pricePerKg);

    let totalValue = 0;
    let currentWeight = 0;

    for (const item of items) {
        if (currentWeight + item.weight <= totalWeight) {
            totalValue += item.weight * item.pricePerKg;
            currentWeight += item.weight;
        } else {
            let remainingWeight = totalWeight - currentWeight;
            totalValue += remainingWeight * item.pricePerKg;
            break;
        }
    }

    console.log(totalValue.toFixed(0));
})
