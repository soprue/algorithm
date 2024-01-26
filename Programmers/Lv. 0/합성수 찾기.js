function solution(n) {
    const isPrime = num => {
        for(let i=2; i<=Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    }
    
    let count = 0;
    for(let i=1; i<=n; i++) {
        if(!isPrime(i)) count++;
    }
    
    return count;
}