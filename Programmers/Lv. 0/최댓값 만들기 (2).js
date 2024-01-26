function solution(numbers) {
    numbers.sort((a, b) => b - a);
    let plus = numbers[0] * numbers[1];
    let minus = numbers[numbers.length - 1] * numbers[numbers.length - 2];
    return Math.max(plus, minus);
}
