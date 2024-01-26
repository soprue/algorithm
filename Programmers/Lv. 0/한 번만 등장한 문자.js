function solution(s) {
    let map = new Map();
    let result = [];
    
    for(let x of [...s]) {
        if(map.has(x)) map.set(x, map.get(x) + 1);
        else map.set(x, 1);
    }
    
    for (let [key, value] of map) {
        if(value == 1) result.push(key);
    }
    
    return result.sort().join("");
}