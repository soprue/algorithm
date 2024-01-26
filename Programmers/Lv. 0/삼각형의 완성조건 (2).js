function solution(sides) {
    // 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
    let answer = 0;
    let min = Math.min(...sides);
    let max = Math.max(...sides);
    
    // 가장 긴 변이 max인 경우
    for(let i = max + 1 - min; i <= max; i++) {
        answer++;
    }
    
    // 나머지 한 변이 가장 긴 변인 경우
    for(let i = max + 1; i <= min + max - 1; i++){
        answer++;
    }
    
    return answer;
}