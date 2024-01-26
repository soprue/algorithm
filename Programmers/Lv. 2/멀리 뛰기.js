function solution(n) {
    let answer = Array.from({length: n + 1}, () => 0);
    answer[1] = 1;
    answer[2] = 2;
    
    for(let i=3; i<=n; i++) {
        answer[i] = answer[i - 1] + answer[i - 2] % 1234567;
    }
    
    return answer[n] % 1234567;    
}

// 참고: https://zzang9ha.tistory.com/138
// https://github.com/soprue/Programmers/blob/1ccd14d95c48675ec662954ea9d813a11862d8b0/Lv.%202/%EB%A9%80%EB%A6%AC%20%EB%9B%B0%EA%B8%B0.png 
