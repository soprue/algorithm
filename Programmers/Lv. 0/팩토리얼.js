function solution(n) {
    const factorial = (num) => {
        if(num == 1) return 1;
        else return num * factorial(num - 1);
    }
    
    for(let i=1; i<=11; i++){
        if (factorial(i) > n){
            return i-1;
        }
    }
}