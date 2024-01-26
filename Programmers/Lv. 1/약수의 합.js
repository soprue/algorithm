function solution(n) {
    let answer = 0;
    for(let i=0; i<=n / 2; i++) {
        if(n % i == 0) {
            answer += i;
        }
    }
    answer += n;
    return answer;
}