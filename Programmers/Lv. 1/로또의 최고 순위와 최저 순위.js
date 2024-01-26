function solution(lottos, win_nums) {
    let rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6};
    let correct = 0, zero = 0;
    
    lottos.map(v => {
        if(win_nums.includes(v)) correct++;
        if(v == 0) zero++;
    });
    
    return [rank[correct + zero], rank[correct]];
}