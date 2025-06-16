/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }

    // 여기까지 왔다는 건 전부 9였다는 뜻 → 맨 앞에 1 추가
    digits.unshift(1);
    return digits;
};
