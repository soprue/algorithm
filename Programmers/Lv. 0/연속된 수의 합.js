function solution(num, total) {
    let answer = [];
    let middle = total / num; // 중간값
    
    if(num % 2 == 0) {
        answer[0] = Math.ceil(middle) - Math.floor(num / 2);
    } else {
        answer[0] = middle - Math.floor(num / 2);
    }
    
    for(let i=1; i<num; i++) {
        answer[i] = answer[i - 1] + 1;
    }
    return answer;
}