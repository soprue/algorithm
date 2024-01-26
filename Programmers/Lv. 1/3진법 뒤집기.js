function solution(n) {
    // 10진수 -> 3진수 : n.toString(3)
    // 3진수 -> 10진수 : parseInt(n,3)
    let answer = [...n.toString(3)].reverse().join("");
    return parseInt(answer, 3);
}