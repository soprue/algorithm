function solution(s) {
    let prev = [];
    return s.split(" ").reduce((acc, cur) => {
        if(cur == "Z") return acc - prev.pop();
        prev.push(Number(cur));
        return acc + Number(cur);
    }, 0);
}