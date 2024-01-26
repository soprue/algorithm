function solution(array) {
    let hashmap = new Map();
    for(let x of array) {
        if(hashmap.has(x)) hashmap.set(x, hashmap.get(x) + 1);
        else hashmap.set(x , 1);
    }

    let max = Math.max(...hashmap.values());
    let answer = Array.from(hashmap).filter(item => item[1] === max);

    return (answer.length > 1) ? -1 : answer[0][0];
}