function solution(d, budget) {
    let money = 0, count = 0;
    
    d.sort((a, b) => a - b);
    for(let x of d) {
        money += x;
        if(money <= budget) count++;
        else break;
    }
    return count;
}