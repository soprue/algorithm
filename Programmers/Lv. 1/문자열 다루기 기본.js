function solution(s) {
    return !s.match(/\D/g) && (s.length == 4 || s.length == 6);
}