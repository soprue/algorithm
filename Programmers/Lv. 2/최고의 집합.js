function solution(n, s) {
    if(n > s) return [-1];
    
    let base = Math.floor(s / n); // s를 n으로 나누어 각 원소가 균등하게 분배될 수 있는 기본값 계산
    let remainder = s % n;
    let result = new Array(n).fill(base);
    
    // s를 n으로 나눈 나머지를 이용해 분배된 값에서 더해야 할 추가 값을 계산하여 균등하게 분배
    for(let i=0; i<remainder; i++) {
        result[i]++;
    }
    
    return result.sort((a, b) => a - b);
}
