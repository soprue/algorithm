// https://school.programmers.co.kr/learn/courses/30/lessons/120876

// 빨간색, 초록색, 파란색 선분이 x축 위에 있습니다.
// 세 선분의 x좌표 시작과 끝이 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
// 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.



function solution(lines) {
    let totalOverlappedLength = 0;
    let min = Math.min(...lines.flat());
    let max = Math.max(...lines.flat());

    function isInclude(x, [start, end]){
        x += 0.5
        if ((start < x) && (x < end)) return true;
        else return false;
    }

    for(let x = min; x < max; x++){
        let overlappedOnX = 0;
        lines.forEach((el) => {
            if(isInclude(x, el)){
                overlappedOnX += 1;
            }
        });

        if(overlappedOnX > 1){
            totalOverlappedLength += 1;
        }
    }
    
    return totalOverlappedLength;
}
