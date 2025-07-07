/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    const dfs = (r, c) => {
        if (
        r < 0 || c < 0 ||
        r >= rows || c >= cols ||
        grid[r][c] === "0"
        ) return;

        grid[r][c] = "0"; // 방문 표시

        dfs(r - 1, c); // 위
        dfs(r + 1, c); // 아래
        dfs(r, c - 1); // 왼쪽
        dfs(r, c + 1); // 오른쪽
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === "1") { // 섬 발견 
                count++;
                dfs(r, c);
            }
        }
    }

    return count;
};
