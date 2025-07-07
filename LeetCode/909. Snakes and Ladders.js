/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
    const N = board.length;

    // 번호 -> 좌표 변환 함수
    const getCoord = (num) => {
        let row = Math.floor((num - 1) / N);
        let col = (num - 1) % N;

        let r = N - 1 - row; // 보드 맨 아래가 1번이니까 뒤집어 줘야 함
        let c = row % 2 === 0 ? col : N - 1 - col; // 지그재그 반영
        return [r, c];
    }

    let queue = [[1, 0]]; // [시작 위치 1, 이동 횟수 0]
    let visited = Array(N * N + 1).fill(false);
    visited[1] = true;

    while (queue.length > 0) {
        let [pos, moves] = queue.shift();
        if (pos === N * N) return moves;

        for (let i = 1; i <= 6; i++) {
            let next = pos + i;
            if (next > N * N) continue;

            let [r, c] = getCoord(next); // next 좌표
            if (board[r][c] !== -1) next = board[r][c]; // 뱀 또는 사다리

            if (!visited[next]) {
                visited[next] = true;
                queue.push([next, moves + 1]);
            }
        }
    }

    return -1;
};
