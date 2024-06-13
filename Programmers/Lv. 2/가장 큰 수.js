function solution(numbers) {
    const strings = numbers.map(num => num.toString());
    strings.sort((a, b) => (b + a) - (a + b));
    const result = strings.join('');
    return result[0] === '0' ? '0' : result;
}
