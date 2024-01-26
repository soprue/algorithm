function solution(number, limit, power) {
    let answer = 0;
    
    const getDivisor = (num) => {
        let count = 0;
        for(let i = 1 ; i <= Math.sqrt(num) ; i++){
            if(num % i === 0) {
                count++;
                if(num / i != i) count++;
            }
        }
        return count;
    }
    
    for(let i=1; i<=number; i++) {
        let divisor = getDivisor(i);
        if(divisor > limit) answer += power;
        else answer += divisor;
    }
    
    return answer;
}