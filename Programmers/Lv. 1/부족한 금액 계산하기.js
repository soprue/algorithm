function solution(price, money, count) {
    let fee = Array.from({ length: count }).reduce((acc, _, idx) => acc + price * (idx + 1), 0);
    return money < fee ? fee - money : 0;
}