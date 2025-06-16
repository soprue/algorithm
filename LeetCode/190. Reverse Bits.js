/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        result = (result << 1) | (n & 1); // result 왼쪽으로 밀고, n의 마지막 비트 붙이기
        n = n >>> 1; // n을 오른쪽으로 1비트 밀기 (부호 없이)
    }

    return result >>> 0; // unsigned 32비트 정수로 변환
};
