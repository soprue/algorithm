// https://school.programmers.co.kr/learn/courses/30/lessons/12953

// 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
// 예를 들어 2와 7의 최소공배수는 14가 됩니다.
// 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
// n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

function getGcd (a, b) {
    return a % b == 0 ? b : getGcd(b, a % b);
}

function solution(arr) {
    return arr.reduce(function(acc, curr) {
        return acc * curr / getGcd(acc, curr);
    }, arr[0]);
}
