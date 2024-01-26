function solution(board, moves) {
    let answer = 0;
    let stack = [];
    
    for(let x of moves) {
        for(let i=0; i<board.length; i++) {
            if(board[i][x-1] != 0) {
                if(stack[stack.length-1] === board[i][x-1]){
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(board[i][x-1]);
                }
                board[i][x-1] = 0;
                break;
            }
        }
    }
    
    return answer;
}