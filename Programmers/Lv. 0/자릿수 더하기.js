function solution(n) {
    return [...(""+n)].map(num => Number(num)).reduce((acc, cur) => acc + cur);
}