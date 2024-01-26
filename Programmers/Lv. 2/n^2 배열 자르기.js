function solution(n, left, right) {
    const answer = [];

    for (let idx = left; idx <= right; idx++) {
        answer.push(Math.max(idx % n, Math.floor(idx / n)) + 1);
    }

    return answer;
}

/*
문제에서 나온 방법대로 2차원 배열을 생성한 다음, 
각 행을 이어 붙여서 1차원화 하고 left ~ right의 숫자를 담아도 되지만,
n의 범위는 10^7까지이기 때문에 시간과 공간 효율성에서 통과하지 못할 것이다.

좌표로 전환해서 생각해 보았을 때, 좌표 (r, c)에 들어갈 숫자는 max(r, c) + 1이다.
left부터 right까지의 숫자를 좌표로 변환해서 계산해 보면 된다.

↓ left ~ right 범위의 임의의 숫자 num에 대해서 좌표 (r, c)를 구하는 공식 ↓
r = Math.floor(num / n)
c = num % n

자세한 이해는 https://velog.io/@hannahf97/프로그래머스-n2-배열-자르기 참고
*/
