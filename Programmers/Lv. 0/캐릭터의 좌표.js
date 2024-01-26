function solution(keyinput, board) {
    let answer = [0, 0];
    let end = [(board[0] - 1) / 2, (board[1] - 1) / 2];
    
    for(let x of keyinput) {
        if(x == "left") {
            answer[0] = answer[0] - 1 >= -end[0] ? answer[0] - 1 : answer[0];
        } else if(x == "right") {
            answer[0] = answer[0] + 1 <= end[0] ? answer[0] + 1 : answer[0];
        } else if(x == "up") {
            answer[1] = answer[1] + 1 <= end[1] ? answer[1] + 1 : answer[1];
        } else if(x == "down") {
            answer[1] = answer[1] - 1 >= -end[1] ? answer[1] - 1 : answer[1];
        }
    }
    return answer;
}