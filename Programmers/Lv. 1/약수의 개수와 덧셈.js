function solution(left, right) {
    let answer = 0;
    
    for(let i=left; i<=right; i++) {
        let divisor = 1;
        for(let j = 1; j <= i / 2; j++) {
            if(i % j == 0) divisor++;
        }
        
        answer = divisor % 2 == 0 ? answer + i : answer - i;
    }
    return answer;
}