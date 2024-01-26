function solution(n) {
    let answer = 0;
    const arr = new Array(n+1).fill(true);
      
    // 에라토스테네스의 체
    for(let i = 2; i <= Math.sqrt(n); ++i) {
        if(arr[i] === false) continue;
        
        for(let k = i * 2; k <= n; k += i) {
            arr[k] = false;
        }
    }
    
    for(let i = 2; i <= n; ++i) {
        if(arr[i] === true) answer++;
    }
    
    return answer;
}