function euclidean(a, b) { // 유클리드 호제법
    return (a % b === 0) ? b : euclidean(b, a % b);
}

function solution(denum1, num1, denum2, num2) {
    let topNum = denum1*num2 + denum2*num1;
    let botNum = num1 * num2;
    let gcd = euclidean(topNum, botNum); // 최대공약수

    return [topNum/gcd, botNum/gcd];
}