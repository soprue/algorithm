function solution(my_string) {
    return [...my_string].filter((v) => !isNaN(v)).sort().map((v) => Number(v));
}