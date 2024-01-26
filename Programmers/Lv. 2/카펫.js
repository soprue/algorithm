// https://school.programmers.co.kr/learn/courses/30/lessons/42842#

function solution(brown, yellow) {
    const S = brown + yellow; // 전체 면적
    
    for (let width = S - 1; width > 0; width--) {
        if (S % width) continue; // 나누어 떨어지지 않으면 넘어가기

        const height = S / width;
        const y = (width - 2) * (height - 2); // 노란 카펫의 면적
        const b = S - y; // 갈색 카펫의 면적

        // 정답을 찾았을 때
        if (y == yellow && b == brown) {
            return [width, height];
        }
    }
}

/*
S = 전체 면적, y = 노란색 면적, b = 갈색 면적

S = yellow + brown = width x height
y = (width - 2) x (height - 2)
b = S - y
*/
