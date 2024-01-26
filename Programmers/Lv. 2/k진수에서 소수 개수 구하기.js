function solution(n, k) {
    const toStringArr = n.toString(k).split('0').map(str => Number(str)).filter(num => num !== 1 && num !== 0);
    
    let answer = 0;
    
    toStringArr.forEach((num) => {
        let isDivide = false;
        for(let i = 2; i <= Math.sqrt(num); i++) {
            if(num % i === 0) {
                isDivide = true;
                break;
            }
        }
        
        answer += isDivide ? 0 : 1;
    });
    
    return answer;
}
