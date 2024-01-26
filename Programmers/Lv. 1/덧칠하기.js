function solution(n, m, section) {
    let answer = 0;
    let maxRange = -Infinity; // -Infinity -> 음의 무한대
    
    section.forEach(range => {
        if(maxRange < range){
            answer++;
            maxRange = range + m - 1;
        }
    })
    
    return answer;
}
