function solution(board) {
    function nearby(x, y) {
        let dx = [-1, -1, 0, 1, 1, 1, 0, -1];
        let dy = [0, 1, 1, 1, 0, -1, -1, -1];
        
        for(let k=0; k<8; k++) {
            let nx = x + dx[k];
            let ny = y + dy[k];
            
            if(nx >= 0 && nx < board.length && ny >= 0 && ny < board.length && board[nx][ny] != 1) {
                board[nx][ny] = 2;
            }
        }
    }

    for(let i=0; i<board.length; i++) {
        for(let j=0; j<board.length; j++) {
            if(board[i][j] == 1) {
                nearby(i, j);
            }
        }
    }

    return board.flatMap((v) => v).filter((v) => v == 0).length;
}