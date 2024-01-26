function solution(order) {
    return [...(order+"")].filter(v => v == 3 || v == 6 || v == 9).length;
}