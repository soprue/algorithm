/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const m = matrix.length;
    const n = matrix[0].length;
    let left = 0;
    let right = m * n - 1;

    while(left <= right) {
        let mid = Math.floor((left + right) / 2);

        // mid 인덱스를 2차원 좌표로 환산
        let row = Math.floor(mid / n);
        let col = mid % n;

        let midValue = matrix[row][col];

        if (midValue === target) return true;
        else if (midValue < target) left = mid + 1;
        else right = mid - 1;
    }

    return false;
};
