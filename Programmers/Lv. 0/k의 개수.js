function solution(i, j, k) {
    let answer = 0;
    for(; i<=j; i++) {
        answer += [...String(i)].filter((v) => v == k).length;
    }
    return answer;
}