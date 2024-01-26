function solution(a, b) {
    let answer = 0;
    
    const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
    const month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    
    for(let i=1; i<a; i++) answer += month[i];
    answer += b;
    
    return day[(answer + 4) % 7];  // 금요일부터 1일이므로
}