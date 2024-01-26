function solution(k, tangerine) {
    let answer = 0;
    
    let size = new Map();
    tangerine.forEach(v => size[v] = (size[v] || 0) + 1);
    let sortedSize = Object.values(size).sort((a, b) => b - a);
    
    for(let v of sortedSize) {
        answer++;
        k -= v;
        if(k <= 0) break;
    }
    
    return answer;
}
