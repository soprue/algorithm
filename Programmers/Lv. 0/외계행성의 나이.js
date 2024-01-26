function solution(age) {
    return [...('' + age)].map(v => String.fromCharCode(Number(v) + 97)).join("");
}