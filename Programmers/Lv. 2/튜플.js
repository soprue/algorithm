function solution(s) {
    let answer = new Set();
    
    const arr = JSON.parse(s.replace(/{/g, "[").replace(/}/g, "]"));
    arr.sort((a, b) => a.length - b.length);
    
    arr.forEach(col => {
        col.forEach(row => {
            answer.add(row);
        })
    })
    
    return Array.from(answer);
}
