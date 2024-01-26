function solution(polynomial) {
    let p = polynomial.split(" + ");
    let x = p.filter((v) => v.includes("x")).map((v) => v.replace("x", "") == "" ? 1 : Number(v.replace("x", "")));
    let n = p.filter((v) => !v.includes("x")).map(v => Number(v));
    
    let answer = [];
    if(x.length != 0) {
        let term = x.reduce((acc, cur) => acc + cur);
        term = term == "1" ? "x" : term + "x";
        answer.push(term);
    }
    if(n.length != 0) answer.push(n.reduce((acc, cur) => acc + cur));
    
    if(x.length == 0 && n.length == 0) return 0;
    return answer.join(" + ");
}