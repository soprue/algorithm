function solution(n) {
    var answer = 0;
    
    for(let i=1; i<=n/2; i++)
        if(n % i == 0) answer++;
    
    return answer + 1;
}