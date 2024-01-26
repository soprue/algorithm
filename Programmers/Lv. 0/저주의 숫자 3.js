function solution(n) {
    let num = 0;
    
    while(n > 0) {
        num++;
        
        if(num % 3 == 0) continue;
        if(num.toString().includes("3")) continue;
        
        n--;
    }

    return num;
}