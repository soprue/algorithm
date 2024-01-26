// https://school.programmers.co.kr/learn/courses/30/lessons/12945

// 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
// 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

function fibonacci(n) {
    let bottom_up = [];
    bottom_up[0] = 0;
    bottom_up[1] = 1;
    bottom_up[2] = 1;
    
    for (let i = 3; i <= n; i++) {
        bottom_up[i] = bottom_up[i-1] % 1234567 + bottom_up[i-2] % 1234567;
    }
    
    return bottom_up[n];
}

function solution(n) {
    return fibonacci(n) % 1234567;
}

/*
참고: https://www.youtube.com/watch?v=vYquumk4nWw&list=PLBZBJbE_rGRU5PrgZ9NBHJwcaZsNpf8yD
참고: https://school.programmers.co.kr/questions/16080

자바스크립트가 정수 계산을 보장하는 범위는 Number.MAX_SAFE_INTEGER -> 9007199254740991
그냥 피보나치 n 번째 수에 대해 바로 나머지를 구할 경우
78번째 이후부터는 표현은 되지만 '안전한 정수 계산'을 보장하지 못한다
따라서 (A+B) % C = ((A % C) + (B % C)) % C 라는 수의 속성을 통해
F(n) % 1234567 = ((F(n-1) % 1234567) + (F(n-2) % 1234567)) % 1234567
*/
