function solution(n, m) {
    const getGCD = (a, b) => a % b == 0 ? b : getGCD(b, a % b);
    let gcd = getGCD(n, m);
    return [gcd, n * m / gcd];
}