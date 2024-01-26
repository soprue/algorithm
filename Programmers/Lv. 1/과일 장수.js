function solution(max_score, apple_count, score) {
    let answer = 0;
    score.sort((a, b) => a - b);
    
    while(score.length >= apple_count) {
        let box = [];
        for (let i = 0; i < apple_count; i++) {
          box.push(score.pop());
        }
        answer += Math.min(...box) * apple_count;
    }
    
    return answer;
}