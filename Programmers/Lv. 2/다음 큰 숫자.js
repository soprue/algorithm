function binaryOneLength(n) {
    return n.toString(2).match(/1/g).length;
}

function solution(n) {
    let answer = n + 1;
    while(true) {
        if(binaryOneLength(n) === binaryOneLength(answer)) break;
        answer++;
    }
    return answer;
}
