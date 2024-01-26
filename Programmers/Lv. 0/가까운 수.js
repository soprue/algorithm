function solution(array, n) {
    let answer = Number.MAX_SAFE_INTEGER;
    for(let x of array) {
        if(Math.abs(x - n) < Math.abs(answer - n)) {
            answer = x;
        } else if(Math.abs(x - n) == Math.abs(answer - n)) {
            answer = Math.min(x, answer);
        }
    }
    return answer;
}