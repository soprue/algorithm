function solution(N, stages) {
    let stage = [];
    
    for(let i=1; i<=N; i++) {
        let curr = stages.filter(v => v == i).length;
        let reach = stages.filter(v => v >= i).length;
        stage.push([i, curr/reach]);
    }
    
    return stage.sort((a, b) => b[1] - a[1]).map(v => +v[0]);
}