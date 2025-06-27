/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (!intervals.length) return [];

    // 시작값 기준 정렬
    intervals.sort((a, b) => a[0] - b[0]);
    
    const result = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        const last = result[result.length - 1];

        if (start <= last[1]) {
            // 겹치는 경우: 끝 값만 업데이트
            last[1] = Math.max(last[1], end);
        } else {
            // 안 겹치는 경우: 새로운 구간 추가
            result.push([start, end]);
        }
    }

    return result;
};
