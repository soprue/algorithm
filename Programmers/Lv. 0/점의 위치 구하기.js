function solution(dot) {
    let [x, y] = dot;
    if(y > 0) return x > 0 ? 1 : 2;
    else return x > 0 ? 4 : 3;
} 