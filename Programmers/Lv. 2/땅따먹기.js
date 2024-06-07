function solution(land) {
    const n = land.length;
    
    // 두 번째 행부터 시작해서 각 칸에서 얻을 수 있는 최대 점수를 계산
    for (let i = 1; i < n; i++) {
        land[i][0] += Math.max(land[i - 1][1], land[i - 1][2], land[i - 1][3]);
        land[i][1] += Math.max(land[i - 1][0], land[i - 1][2], land[i - 1][3]);
        land[i][2] += Math.max(land[i - 1][0], land[i - 1][1], land[i - 1][3]);
        land[i][3] += Math.max(land[i - 1][0], land[i - 1][1], land[i - 1][2]);
    }

    // 마지막 행에서의 최대 점수를 반환
    return Math.max(...land[n - 1]);
}
