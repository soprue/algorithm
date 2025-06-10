/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || (x % 10 === 0 && x !== 0)) return false; // 회문수가 절대 될 수 없는 경우를 먼저 걸러냄

    let reversed = 0;

    while (x > reversed) {
        reversed = reversed * 10 + (x % 10);  // 끝자리 붙이기
        x = Math.floor(x / 10);               // 앞자리 줄이기
    }

    // x가 홀수 길이일 경우를 위해 중간자리 제거 비교
    return x === reversed || x === Math.floor(reversed / 10);
};
