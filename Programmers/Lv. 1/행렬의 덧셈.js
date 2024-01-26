function solution(arr1, arr2) {
    return arr1.map((a, i) => {
        return a.map((b, j) => b + arr2[i][j]);
    });
}