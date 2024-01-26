function solution(n) {
    var answer = [];
    
    for(let i=1; i<=Math.floor(n / 2); i++) {
        if(n % i == 0) answer.push(i);
    }
    
    return [...answer, n];
}