// https://school.programmers.co.kr/learn/courses/30/lessons/120875

// 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
// [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
// 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.



function solution(dots) {
    const leans = []

    for(let i = 0; i < dots.length; i++) {
        const dotA = dots[i];
        for(let j = i + 1; j < dots.length; j++) {
            const dotB = dots[j]
            const lean = (dotB[1] - dotA[1])  / (dotB[0] - dotA[0]); // 직선 기울기 구하는 공식

            if(leans.includes(lean)) return 1;
            else leans.push(lean);
        }
    }

    return 0;
}
 
